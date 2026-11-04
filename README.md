# QCrypt 2025+ website
[![Netlify Status](https://api.netlify.com/api/v1/badges/4fa2d41c-275c-4d5a-90ed-14db4a9accb5/deploy-status)](https://app.netlify.com/sites/qcrypt-website/deploys)

Hugo-powered QCrypt website for 2025 edition and later, live at at https://qcrypt.net. QCrypt is the yearly international scientific conference presenting last year’s top results in quantum cryptography. [Hugo](https://gohugo.io/) is a fast static website generator. https://qcrypt.net is generously hosted by [netlify](https://www.netlify.com/) under a [Open Source Plan](https://www.netlify.com/legal/open-source-policy/) :heart:!

Project initiated in 2020 and maintained since then by [Christian Schaffner](https://github.com/cschaffner).

## History
Originally based on the Hugo template from https://github.com/GDGToulouse/devfest-theme-hugo
adapted from the fork by the cloudnative-amsterdam people: https://github.com/cloudnative-amsterdam/public-website

Used to run https://2020.qcrypt.net, https://2021.qcrypt.net, https://2022.qcrypt.net.

Since 2023, the theme submodule is included directly in this git repository.

In preparation of the 2025 edition, a more permanent solution is envisioned with one main page, where more years can be added, broadly modeled after the IACR flagship websites like https://eurocrypt.iacr.org/2024, https://eurocrypt.iacr.org/2025, https://crypto.iacr.org/2023/, https://asiacrypt.iacr.org/2024/, and the *odd one out (in terms of design)* https://crypto.iacr.org/2024/.


## Building this conference site from scratch
> [!WARNING]
> This has only been tested on macOS so far, so sharing your experience with other platforms here is very appreciated!

1. Install [Hugo](https://gohugo.io/installation/) and [Dart Sass](https://gohugo.io/functions/css/sass/#dart-sass)
2. Clone this repo:

```bash
$ git clone https://github.com/IAQI/qcrypt-website.git
```

3. It's done. Just start Hugo server to see the site live!

```bash
$ cd qcrypt-website
$ hugo server
``` 

You can use `--ignoreCache` to ignore local cache files, and `--disableFastRender` to disable fast render mode (this mode will not rebuild all files on every change), which is useful for debugging.

5. Edit the markdown source files with ending `.md` in the [/content/](/content/) subdirectories to make changes to the site. You might also have to edit `.json` and `.yml` files in the [/data/](/data/) subdirectory. As long as the hugo server is running, your changes should be visible immediately at http://localhost:1313/.

You can change this default behavior by adding `--bing ip.addr.1.1` and `--port 1234` to the command line.

6. Using a suitable editor like [Visual Studio Code](https://code.visualstudio.com/) allows to easily search across all source files, and will help finding the correct file to edit if you want to make specific changes.

7. When you are happy with the result, commit the changes to the master branch. The site is then automatically deployed to https://qcrypt-website.netlify.com/ and accessible under https://qcrypt.net. If you have the proper rights, you can see the deployment logs on [netlify](https://app.netlify.com/sites/qcrypt-website/deploys).


## Customizing the theme
Is described in the [README.md ](https://github.com/IAQI/qcrypt-website/blob/main/themes/devfest-theme-hugo/README.md) of the theme.

## High-level overview
This site is built with modern web technologies:

* **Hugo**: [Hugo](https://gohugo.io/) is a fast website builder that turns simple text files into a complete website. It watches for changes in your content and instantly updates the site while you work.

* **JamStack Architecture**: The website follows a modern approach where all pages are created ahead of time. This makes the site fast, secure, and reliable since there's no need to generate pages when visitors arrive. Learn more about [JamStack](https://jamstack.org/).

* **Content Management**: Content is written in [Markdown](https://www.markdownguide.org/) files that are easy to edit and track changes. Multiple people can work on the site together through [GitHub](https://github.com/), and all changes are safely stored and can be reviewed.

* **Styling with CSS/SASS**: The website's appearance is controlled through [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) and [SASS](https://sass-lang.com/) style files that make it easy to maintain a consistent look. Each conference year can have its own visual theme, and the site works well on all screen sizes.

* **Netlify Hosting**: [Netlify](https://www.netlify.com/) automatically builds and publishes the website whenever changes are made and committed to this repository. It ensures the site is secure, fast, and available worldwide through its global network.

This combination of tools creates a website that's fast, secure, and easy to maintain by the conference organizers. Sounds great? Check out [this guided walk](https://github.com/IAQI/qcrypt-website/tree/main/themes/devfest-theme-hugo#a-guided-walk-through-the-ingredients) to learn how it actually works in more detail.

## Setting up the next year 2025 based on previous years

### design 
1. create a new logo, something with a sheep... see [here](https://qcrypt.net/2024/history/#websites--logos) for inspiration.
2. choose a background image for the main site, e.g. [2024](/static/images/2024/background-2024.jpg) or [2023](/static/images/2023/background-2023.jpg) 
3. and make a related banner, e.g. [2024](/static/images/2024/banner-2024.jpg) or [2023](/static/images/2023/banner-2023.jpg) 
4. pick a related themecolor, like `#0099cc` or `#ac191c`.

### create new subdirectories for content
1. It's probably easiest to copy the entire content folder from a previous year like [/content/2024](/content/2024) and start adjusting from there
2. create 2025 subfolder in [/static/images](/static/images)
3. put the images (logo, background image, banner) from above to this folder

### add info to main config file [/hugo.toml](/hugo.toml) 
4. In `[params]`, LEAVE the currentYear and date as it is right now. Change this only when the new 2025 site is ready.
5. add a section `[params.2025]` and supply the required information
6. the timeanddate_cityid can be inferred from https://www.timeanddate.com/worldclock/personal.html by looking at the link after clicking on "Share This Personal World Clock" 
7. Under `[menu]`, create a new `[[menu.2025]]` structure as for 2023 and 2024.

### adjust content files
1. Go through all .md files in [/content/2025](/content/2025) and the `_index.md` files in the subdirectories, and adjust the front matter. 
2. Adjust the `menu:` sub-entry to say `2025` instead of `2024`.
3. put `draft: true` in case you want to disable the page for the time being.
4. In general, whenever the year is passed on as parameter, you might have to update it. So, searching under [/content/2025](/content/2025) for all occurrences of 2024 and replacing the correct ones with 2025 is probably a good strategy.

### create new style file
1. In [/themes/devfest-theme-hugo/assets/style/], duplicate [theme-2024.css](/themes/devfest-theme-hugo/assets/style/theme-2024.css) and rename it to `theme-2025.css`
2. adjust the last line to set the `--primary:` variable in `root` to the themecolor picked above.


### Steps you will need help with
1. on https://github.com/orgs/QCrypt/teams, create a new team ```QCrypt 2025```
2. add admins https://github.com/orgs/QCrypt/teams/qcrypt-2025/members
3. add repositories https://github.com/orgs/QCrypt/teams/qcrypt-2025/repositories
5. In netlify https://app.netlify.com/teams/qcrypt/members: add new admin as collaborator to qcrypt-website
1. on https://api.slack.com/apps/A01P06YNCCU/incoming-webhooks , create a new Webhook (on the bottom of the page)
1. paste the Webhook URL into netfliy:  https://app.netlify.com/sites/qcrypt2024/settings/deploys (for deploy succeesful and deploy failed)
1. add admins to Slack channel
3. We probably need new email addresses like 2025@qcrypt.net and pcchairs2025@qcrypt.net.
3. connect new admins to admins from last year
4. Is it time to update the hugo version? check what needs to be updated.

### bump year
Once the new site is ready to be "promoted" to be the current year, make the following changes:
1. In hugo.toml, in [params], change the currentYear and date
2. In [[server.redirects]], change the forward to = "/2025/"
3. In https://github.com/IAQI/qcrypt-website/blob/main/netlify.toml , adjust the redirect as well


## Later Updates

### call for papers, venue updates, registration
1. adjust the according `.md` file in [/content/2025/](/content/2025/), possibly by switching back "draft: false" and adjusting the content from previous year
2. **all changes to the website should be mentioned in a table with "Website Updates" like on https://qcrypt.net/2023/**, for the convenience of the website visitors
3. The call-to-action buttons on the main site can be adjusted depending on the news.

### tutorial, invited speakers, panelists are known
1. update the `.md` files in https://github.com/IAQI/qcrypt-website/tree/main/content/2025/speakers
2. remove previous images from the images subdirectory, upload new ones, and make sure the `photoURL` field of the speaker is pointing there.
3. Use sensible names for the `.md` files, like `eleni_diamanti.md` 
4. Per speaker, create an according session in https://github.com/IAQI/qcrypt-website/tree/main/content/2025/sessions , using the examples from previous years.

### accepted papers, schedule, presenters and videos
The schedule, session pages and accepted papers / posters lists come from the
shared module [IAQI/conference-program](https://github.com/IAQI/conference-program),
which is also used by the TQC and QIP websites. Its README describes the whole
pipeline, from the HotCRP export to a schedule with linked papers, presenters
and videos. In short (run from this folder, with `conference-program` cloned
next to it):

1. **Accepted papers and posters:** `python3 ../conference-program/scripts/sanitize_hotcrp_json.py private_data/hotcrp.json --decision accept -o data/accepted-papers-2027.json` (same for `posters-2027.json`)
2. **Schedule:** fill in `program/program-2027.csv` (one row per slot; see [program/program-2026.csv](program/program-2026.csv)), then `python3 ../conference-program/scripts/generate_schedule.py --year 2027 --program program/program-2027.csv`
3. **Presenters:** `python3 ../conference-program/scripts/mark_presenters.py --year 2027 --registrations private_data/<registration export>`
4. **Videos:** `python3 ../conference-program/scripts/fetch_videos.py --year 2027 --playlist <YouTube playlist URL>`

Raw HotCRP exports and registration lists contain personal data: keep them in
`private_data/` (git-ignored), never in `data/`.

The templates are vendored in `_vendor/`. To pick up a new version of the module:
`hugo mod get -u github.com/IAQI/conference-program && hugo mod vendor`.


## More detailed explanations of the different content sections

Have a look at the [Hugo Documentation](https://gohugo.io/documentation/), ChatGPT is also quite knowledgable.

Hugo's favorite [Content format](https://gohugo.io/content-management/formats/) is markdown, and that's what we use throughout. For [data sources](https://gohugo.io/content-management/data-sources/) and config files, Hugo understands TOML, YAML, JSON, CSV, XML. We use the first three only.

Every content file contains a [front matter](https://gohugo.io/content-management/front-matter/), specifying metadata for the content, usually in yaml format. Important parameters are title, year, type, draft, menu. They influence how content is displayed.

> [!WARNING]
> In this site, we are deviating from the Hugo-recommended [Organization of content source](https://gohugo.io/content-management/organization/#organization-of-content-source), because our top levels in the `content/<DIRECTORIES>` are years, instead of topics. Therefore, the `.Section` variable is often our `$currentYear`.

The original Hugo template had multilingual support (French / English), but we have dropped this in the meanwhile, some reminders of these times are still around, though.

### Hugo Shortcodes
> [!NOTE]
> We often use [Hugo shortcodes](https://gohugo.io/content-management/shortcodes/) in this project. There are two different types:
> * `{{%  %}}` produces markdown content like the `jumbo` element on the main page.
> * `{{<  >}}` produces HTML output, e.g. used to produce links with `button-link` inside the `jumbo` element on the main page.
> Some shortcodes have closing brackets, using the markdown content enclosed between them (like `jumbo`), others don't (like `button-link`).

### file names
> [!IMPORTANT]
> Even though Hugo is quite forgiving, please use sensible and consistent file names for content pages, pictures etc. [This page](https://docs.hugoblox.com/reference/site-structure/) recommends to:
> - Stick to lowercase for all file names, including content files (`about.md`), layouts, and static assets (`images/logo.png`).
> - Use hyphens (`-`) or underscores (`_`) to separate words instead of spaces or capital letters (e.g., `my-article.md` or `my_article.md`).


### Menus in the header
See [Menus](https://gohugo.io/content-management/menus/) in the Hugo documentation. We are using a mix of "In side configuration" and "in front matter" menu definitions.

The basic structure of the top menu is copied from the IACR flagship conference websites (like https://eurocrypt.iacr.org/2024). The basic menu structure is defined in [/hugo.toml](/hugo.toml) under [menu]. We have a menu hierarchy for each year, but these basic entries should basically be the same every year. The items "Technical Program" and "Attend" do not correspond to actual pages, they are used as parent menu items for other pages.

The other items in the menu are defined in the front matter of content pages.

### Footer
The content of the footer is specified in [/data/footer.yml](/data/footer.yml). The "social share" options are currently disabled, the "social follow" options are Twitter and YouTube. 
> [!NOTE]
> Maybe we want to move away from Twitter soon?

The footer rarely needs to be changed. It automatically links to the charter, history and code of conduct of the current year. Just make sure that the content directory of the currentYear also contains these three files:
* `charter.md`
* `history.md`
* `code-of-conduct.md`
  
Copy them over from the previous year and make sure they are up to date!

It is a requirement by the Netlify Open Source plan to link to a code of conduct, so do not remove that part!

### Main page
The main home page per year is the `/content/YEAR/_index.html`, like [/content/2024/_index.html](/content/2024/_index.html). It has `type: home` and `layout: home` in the front matter.

It is the only page without a banner on top, as it starts with a [jumbo element](https://github.com/IAQI/qcrypt-website/blob/main/themes/devfest-theme-hugo/README.md#jumbo-bloc) which takes as arguments the background image, label and logo. The content of it is the date, and various call to actions using button-links, which in turn take arguments like label, url, icon.

The following elements are:
* home-info: some basic information about QCrypt
* home-keydates: the two most important tables: one with key dates, one with website updates, see [2023](https://qcrypt.net/2023/) for an example. Again, this is inspired by [the IACR pages](https://eurocrypt.iacr.org/2023/)). 
* home-location: image, address, and coordinates of the venue
* partners: list of sponsors, or call for sponsors

### Team
One of the first content pages to update and display. Follow the example of previous years.

All committees get their own subfolder, and there is an image folder for all portrait pictures. Ensure the photoURL front matter item points to the correct picture. When creating and naming new files, follow [reasonable conventions](#file-names).

### Partners / Sponsors
The subdirectory is called `partners` but on the website, we commonly refer to them as "Sponsors". There are subfolders for the different categories. Logos should go into the `logos/` subfolders, and the `logo` front matter entry should refer to that logo file.

### Speakers & Sessions
Very similar to the administration of the [team](#Team).

Make sure to create [sessions](/content/2024/sessions/) for all speakers. In front matter of the session (e.g. [this one](/content/2023/sessions/tutorial_yuen.md)), specify one or more speaker, referring to the `key` entry in the speaker front matter (e.g. `yuen` in [this one](/content/2023/speakers/tutorial/yuen.md)).

The front matter of sessions should specify the `year`, `format` (like `contributed`, `invited`, `industry`, `tutorial` etc.). The `type` has to be `sessions` in order to render the session properly.

For sessions with contributed talks, specify the paper ids once they are known
(`papers:`); `generate_schedule.py` does this for you from the program spreadsheet.

There is an [overview of speakers](/content/2025/speakers/_index.html) (e.g. [2024](https://qcrypt.net/2024/speakers/)), and and [overview of sessions](/content/2025/sessions/_index.html) (e.g. [2024](https://qcrypt.net/2024/sessions/), both should be added to the "Technical Program" menu when ready.

### Schedule
The schedule is generated from `data/schedule-YEAR.yml`, which
`generate_schedule.py` writes from `program/program-YEAR.csv` (see above).
Each session in it refers to a page `content/YEAR/sessions/<key>.md`. Set
`draft: false` in `content/YEAR/schedule/_index.md` to publish the schedule.

The schedule page consists of several sessions. Each session has following elements:

|element|Required|description|
|---|---|---|
|title|yes|The title of the session|
|format|no|The format of the session, like `contributed`, `invited`, `industry`, `tutorial` etc.|
|type|yes|Should be `sessions`|
|year|yes|The year of the session|
|papers|no|The paper id/ids of the accepted papers or posters. Stuff sessions can leave this blank|
|chair|no|The chair for this session|
|draft|yes|Should be `false` for a unpublished session and `true` for a published session|
|tags|no|The tags of the session, which will affect the class for the session element in website|