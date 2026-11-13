# QCrypt 2025+ website
[![Netlify Status](https://api.netlify.com/api/v1/badges/4fa2d41c-275c-4d5a-90ed-14db4a9accb5/deploy-status)](https://app.netlify.com/sites/qcrypt-website/deploys)

Hugo-powered QCrypt website for 2025 edition and later, live at at https://qcrypt.net. QCrypt is the yearly international scientific conference presenting last year’s top results in quantum cryptography. [Hugo](https://gohugo.io/) is a fast static website generator. https://qcrypt.net is generously hosted by [netlify](https://www.netlify.com/) under a [Open Source Plan](https://www.netlify.com/legal/open-source-policy/) :heart:!

Project initiated in 2020 and maintained since then by [Christian Schaffner](https://github.com/cschaffner).

## History
Originally based on the Hugo template from https://github.com/GDGToulouse/devfest-theme-hugo
adapted from the fork by the cloudnative-amsterdam people: https://github.com/cloudnative-amsterdam/public-website

Used to run https://2020.qcrypt.net, https://2021.qcrypt.net, https://2022.qcrypt.net.

Since 2023, the theme submodule was included directly in this git repository. Since 2026, the theme is shared with the TQC and QIP websites as the Hugo module [IAQI/conference-theme](https://github.com/IAQI/conference-theme).

The site has one main page per year, broadly modeled after the IACR flagship websites like https://eurocrypt.iacr.org/2024, https://crypto.iacr.org/2023/, https://asiacrypt.iacr.org/2024/.

Earlier editions are archived on https://qcrypt.iaqi.org; `/2011` to `/2024` on this site redirect there.

## Working on the site

**The [website guide](https://github.com/IAQI/conference-theme/blob/main/docs/website-guide.md)** (in the shared theme) explains everything that is the same for QCrypt, TQC and QIP: running the site locally, how the content is organised, shortcodes, menus, footer, home page, team, sponsors, speakers and sessions, setting up a new year, colours. In short:

```bash
git clone https://github.com/IAQI/qcrypt-website.git
cd qcrypt-website
hugo server        # needs Hugo (extended), Dart Sass and Go; see the guide
```

Push to a branch and open a pull request to get a Netlify deploy preview; merging into `main` publishes https://qcrypt.net. If you have the proper rights, you can see the deployment logs on [netlify](https://app.netlify.com/sites/qcrypt-website/deploys).

## Setting up the next year

Follow the guide's [new year](https://github.com/IAQI/conference-theme/blob/main/docs/website-guide.md#a-new-year) section (`new_year.py` copies the previous year's pages as drafts). QCrypt specifics:

### design
1. create a new logo, something with a sheep... see [here](https://qcrypt.net/2024/history/#websites--logos) for inspiration.
2. choose a background image for the main site and make a related banner, e.g. [2026](/static/images/2026/Ottawa-Banner.jpeg).
3. pick a related themecolor, like `#0099cc` or `#ac191c`.

### Steps you will need help with
1. on https://github.com/orgs/QCrypt/teams, create a new team ```QCrypt <year>```
2. add admins and repositories to that team
3. In netlify https://app.netlify.com/teams/qcrypt/members: add new admin as collaborator to qcrypt-website
4. on https://api.slack.com/apps/A01P06YNCCU/incoming-webhooks , create a new Webhook (on the bottom of the page)
5. paste the Webhook URL into netlify (for deploy succeeded and deploy failed)
6. add admins to Slack channel
7. We probably need new email addresses like <year>@qcrypt.net and pcchairs<year>@qcrypt.net.
8. connect new admins to admins from last year
9. Is it time to update the hugo version? check what needs to be updated.

### During the year
**All changes to the website should be mentioned in a table with "Website Updates" on the home page**, for the convenience of the website visitors.

## Accepted papers, schedule, presenters and videos
The shared theme's [README](https://github.com/IAQI/conference-theme#from-accepted-papers-to-the-schedule) describes the pipeline, from the HotCRP export to a schedule with linked papers, presenters and videos. In short (run from this folder, with `conference-theme` cloned next to it):

1. **Accepted papers and posters:** `python3 ../conference-theme/scripts/sanitize_hotcrp_json.py private_data/hotcrp.json --decision accept -o data/accepted-papers-2027.json` (same for `posters-2027.json`)
2. **Schedule:** fill in `program/program-2027.csv` (one row per slot; see [program/program-2026.csv](program/program-2026.csv)), then `python3 ../conference-theme/scripts/generate_schedule.py --year 2027 --program program/program-2027.csv`
3. **Presenters:** `python3 ../conference-theme/scripts/quantumdb_presenters.py --venue qcrypt --year 2027` (from QuantumDB, as for 2026), or `python3 ../conference-theme/scripts/mark_presenters.py --year 2027 --registrations private_data/<registration export>`
4. **Videos:** `python3 ../conference-theme/scripts/fetch_videos.py --year 2027 --playlist <YouTube playlist URL>`

Raw HotCRP exports and registration lists contain personal data: keep them in `private_data/` (git-ignored), never in `data/`.

## What this site does differently
The shared theme is used as it is; this site only sets its own colours (`assets/style/theme-<year>.scss`) and the names of its charter and history pages (`i18n/en.toml`).
