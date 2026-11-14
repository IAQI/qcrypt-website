---
title: 'Invited Talk: Private Proofs of When and Where'
format: invited
type: sessions
year: 2026
speakers:
- Malkin
chair: None
videoId: null
presentation: null
draft: false
tags:
- invited
---

## Biography

Tal Malkin is a professor of Computer Science at Columbia University, where she directs the Cryptography Lab, and was the inaugural chair of the Cybersecurity Center at the Data Science Institute. She holds a BS in Math and Computer Science from Bar-Ilan University, an MS in Computer Science from the Weizmann Institute of Science, and a PhD in Computer Science from the Massachusetts Institute of Technology. Prior to joining Columbia, she worked as a research scientist at AT&T Labs Research.

Malkin's primary research interests are in cryptography and its connections to complexity theory, systems security, and machine learning.  Her work on evaluating and defending implementations against side channel attacks received an IACR Test-of-Time Award for lasting impact on cryptographic theory and practice, and her work on the complexity of adversarial noise models received a Best Paper Award at SODA. She is an IACR (International Association for Cryptologic Research) Fellow, and a recipient of the NSF CAREER Award, the Columbia University Presidential Teaching Award, and faculty awards from JP Morgan, IBM, Amazon, and Google. She has chaired leading conferences including CRYPTO, the ACM Conference on Computer and Communications Security (CCS), and the Theory of Cryptography Conference (TCC), and currently chairs the steering committee for TCC.

## Abstract

Position verification schemes are interactive protocols where entities prove their physical location to others; this enables interactive proofs for statements of the form "I am at a location ." Although secure position verification cannot be achieved with classical protocols (even with computational assumptions), they are feasible with quantum protocols.
In this paper we introduce the notion of zero-knowledge position verification, which generalizes position verification in two ways:
1. enabling entities to prove more sophisticated statements about their locations at different times (for example, "I was NOT near location  at noon yesterday").
2. maintaining privacy for any other detail about their true location besides the statement they are proving.
We construct zero-knowledge position verification from standard position verification and post-quantum one-way functions. The central tool in our construction is a primitive we call position commitments, which allow entities to privately commit to their physical position in a particular moment, which is then revealed at some later time. 
