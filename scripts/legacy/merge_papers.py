#!/usr/bin/env python3
"""
Merge two paper JSON files based on title matching.

This script merges accepted-papers-2025.json (source of PIDs) with accepted-2025.json 
(source of detailed data) by matching paper titles. The output preserves the PIDs from 
the first file while enriching the data with abstracts, full author information, and 
topics from the second file.
"""

import json
import argparse
import sys
from pathlib import Path

def normalize_title(title):
    """Normalize title for comparison by removing extra whitespace, (Remote) suffix, and converting to lowercase."""
    # Remove (Remote) suffix if present
    normalized = title.strip()
    if normalized.endswith('(Remote)'):
        normalized = normalized[:-8].strip()  # Remove "(Remote)" and any trailing whitespace
    return normalized.lower()

def merge_papers(pid_file, data_file, output_file):
    """
    Merge two paper JSON files based on title matching.
    
    Args:
        pid_file (str): Path to JSON file containing papers with desired PIDs
        data_file (str): Path to JSON file containing papers with detailed data
        output_file (str): Path for the merged output JSON file
    """
    # Load both files
    try:
        with open(pid_file, 'r', encoding='utf-8') as f:
            pid_papers = json.load(f)
        print(f"Loaded {len(pid_papers)} papers from {pid_file}")
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading {pid_file}: {e}", file=sys.stderr)
        sys.exit(1)
    
    try:
        with open(data_file, 'r', encoding='utf-8') as f:
            data_papers = json.load(f)
        print(f"Loaded {len(data_papers)} papers from {data_file}")
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading {data_file}: {e}", file=sys.stderr)
        sys.exit(1)
    
    # Create title-to-paper mapping for data file
    data_by_title = {}
    for paper in data_papers:
        normalized_title = normalize_title(paper.get('title', ''))
        if normalized_title:
            data_by_title[normalized_title] = paper
    
    # Merge papers
    merged_papers = []
    matched_count = 0
    unmatched_titles = []
    
    for pid_paper in pid_papers:
        pid_title = normalize_title(pid_paper.get('title', ''))
        
        if pid_title in data_by_title:
            # Found match - merge data
            data_paper = data_by_title[pid_title]
            
            # Start with the detailed data paper
            merged_paper = data_paper.copy()
            
            # Override with the PID from the pid_file
            merged_paper['pid'] = pid_paper['pid']
            
            # Remove the 'object' field if it exists (not needed in final output)
            if 'object' in merged_paper:
                del merged_paper['object']
            
            merged_papers.append(merged_paper)
            matched_count += 1
        else:
            # No match found - keep original from pid file but note it
            merged_papers.append(pid_paper)
            unmatched_titles.append(pid_paper.get('title', 'Unknown title'))
    
    # Write merged result
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(merged_papers, f, indent=4, ensure_ascii=False)
        print(f"Successfully merged {matched_count} papers to {output_file}")
    except PermissionError:
        print(f"Error: Permission denied writing to '{output_file}'", file=sys.stderr)
        sys.exit(1)
    
    # Report results
    print(f"\nMerge Summary:")
    print(f"  Total papers in PID file: {len(pid_papers)}")
    print(f"  Total papers in data file: {len(data_papers)}")
    print(f"  Successfully matched: {matched_count}")
    print(f"  Unmatched papers: {len(unmatched_titles)}")
    
    if unmatched_titles:
        print(f"\nUnmatched papers (kept with original minimal data):")
        for i, title in enumerate(unmatched_titles, 1):
            print(f"  {i}. {title}")

def main():
    """Main function to parse arguments and run the merge."""
    parser = argparse.ArgumentParser(
        description="Merge two paper JSON files based on title matching.",
        epilog="""
Examples:
  %(prog)s accepted-papers-2025.json accepted-2025.json merged-papers.json
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        'pid_file',
        help='JSON file containing papers with the desired PIDs'
    )
    
    parser.add_argument(
        'data_file', 
        help='JSON file containing papers with detailed data (abstracts, authors, topics)'
    )
    
    parser.add_argument(
        'output_file',
        help='Output JSON file for the merged results'
    )
    
    args = parser.parse_args()
    
    # Validate input files exist
    for file_path in [args.pid_file, args.data_file]:
        if not Path(file_path).exists():
            print(f"Error: Input file '{file_path}' does not exist.", file=sys.stderr)
            sys.exit(1)
    
    # Create output directory if it doesn't exist
    output_path = Path(args.output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Run the merge
    merge_papers(args.pid_file, args.data_file, args.output_file)

if __name__ == "__main__":
    main()
