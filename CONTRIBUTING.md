# Contributing to the CodeMeta site

## Adding new Crosswalks

Crosswalks are developed in
[the main CodeMeta repository](https://github.com/codemeta/codemeta) and are
periodically synchronised into the website.

A markdown file must be created on this website before that synchronised
Crosswalk data is displayed. Refer to existing files for examples of the
format. The file must contain the following frontmatter fields:

- `title` in the format `Crosswalk for <target>` where `<target>` is the name
of the system the Crosswalk maps to. It can include spaces and symbols.
- `image` in the format `/img/<filename>` where `<filename>` is the name of
the logo filename, including extension. This file must be added to the
`/static/img/` directory. Do *not* use the source path.

The content after the frontmatter should include a short description of the
target system. A link to the system or its metadata documentation should be
included in this description.

The following code required on the last line of the file, where
`<source filename>` is the filename of
[the Crosswalk source file in the main repository](https://github.com/codemeta/codemeta.github.io/tree/master/content/crosswalk),
including spaces and symbols, but _without_ the extension:

```
{{% crosswalk name="<source filename>" %}}
```

Any other issues, requests, or contributions for the content of Crosswalks
should go to the main repository.

Please refer to the
[instructions for contributing](https://github.com/codemeta/codemeta/?tab=contributing-ov-file)
to that repository.

## Changes for the Codemeta Generator.

The CodeMeta Generator is developed in
[its own repository](https://github.com/codemeta/codemeta-generator). GitHub
deploys it under the same subdomain as this site.

Any issues, requests, or contributions for the Generator should go there.

Please refer to the
[instructions for contributing](https://github.com/codemeta/codemeta-generator/?tab=contributing-ov-file)
to that repository.

## Pull Requests

The following is the preferred process for submitting PRs regarding the
`https://codemeta.github.io` website:

Fork the `https://github.com/codemeta/codemeta.github.io` repository. This
creates your own copy of the repository. You have full control of this copy.

[![CodeMeta website forks](https://img.shields.io/github/forks/codemeta/codemeta.github.io)](https://github.com/codemeta/codemeta.github.io/fork)

Clone _*your copy*_ of the repository. Where `<user>` is your github username:

```
git clone git@github.com:<user>/codemeta.github.io.git
```

There should be an issue open that discusses this change. Open a new issue if
one does not already exist:

[![GitHub Issues or Pull Requests](https://img.shields.io/github/issues/codemeta/codemeta.github.io)](https://github.com/codemeta/codemeta.github.io/issues)

(Optional) Create a new branch for your change. This keeps your `master`
branch clear of changes, which can make it difficult to keep it in sync with
the original repository. The following would create a branch named for issue
#999:

```
git checkout -b "issue-999"
```

Make your changes as discussed, then run Hugo to make sure the changes are
correct and nothing has broken.
[Refer to the staging instructions](https://github.com/codemeta/codemeta.github.io?tab=readme-ov-file#staging-the-site)
for how to preview your changes locally.

Add and commit your changed files to your local repository copy. Include the
issue number somewhere in a commit message, prefixed with a `#`, eg, `#999`.
This will prompt GitHub to create a link back to the issue.

Try to stick to one functional change per commit. This makes it easy to revert
if something goes wrong.

Push the commits up to GitHub:

```
git push origin issue-999
```

GitHub will prompt you to open a Pull Request. Open the Pull Request against
the `master` branch.

If the maintainers agree with your change, it will be merged. If they do not,
it will be discussed and possibly edited in the Pull Request process.

### Updating Scripts

Scripts in the `/scripts/` directory of this repository process data synced
from the main CodeMeta repository.

Please check with [the main repository](https://github.com/codemeta/codemeta/)
before updating these.

### Updating Data Files

Some data files in the `/data/` directory must not be manually edited in this
repository; The `crosswalk` and `property_description` data files are
generated during deployment and protected by `/data/.gitignore`.

The files in `/data/feeds/` are checked for updates once a day. If they are
not updating, then fixes should be applied to `.github/workflow/news.yml`.

Other data files in `/data/` are discussed below.

### Updating the front page features

The front page layout, `landing` is divided into three sections containing
top-level partials:
  - `landing_left` contains the index page content,
  - `landing_right` is narrower and contains content that is likely to change,
  - `landing_wide` is a full-width section above the footer.

A *Partial* is a fragment of the theme that can be reused. Using partials for
complex pieces of the layout allows functionality to be moved, removed, or
duplicated easily. A *Shortcode* is the equivalent for within `/content/`
(instead of `/theme/`) and allow content and site functionality to be kept
separate.

Subsections that require generation from the Hugo template engine should be
contained in partials or shortcodes. Other static theming, such as buttons,
can be kept as inline HTML within these top-level partials.

#### News Feeds

The website's news feed is updated by a combination of GitHub Actions and
Javascript. The workflow fetches the RSS feeds each day, and commits a new
version if there are any updates. Javascript fetches any updates between
these snapshots. This avoids an ugly jump when loading the remote feeds.

To add a new feed:

- Add a `curl` command to `.github/workflows/news.yml` to fetch the feed's
URL. Use an existing command as an example.
- Add the URL as a value to the `feeds` array under `[params]` in the site's
`config.toml`.
- (Optional) Add a copy of the RSS feed to `/data/feeds/`

All feeds in `/data/feed/` will be merged and items are sorted by their
`pubDate` before display.

#### Supporter Acknowledgements

The supporter acknowledgement cards on the landing page are built from
`/data/supporters.json`. These cards give recognition to organisations and
other projects that have helped to further CodeMeta's mission.

To add a new supporter:

- Add an object to the array in `/data/supporters.json` that contains the
key-value pairs `name`, `logo`, and `url`.
  - `name` should be the full name of the entity.
  - `logo` can either be a full URL, or a path (_recommended_). As images are
consolidated to the `/img/` directory. The path is `/img/<filename>`, where
`<filename>` is only the filename. Do *not* use the source path.
  - `url` should be a website, an announcement link, or funding record link.
- If a path is provided as the value of `logo`, a file with the corresponding
filename must be added to the `/static/img/` directory.

The cards are generated sorted by name.

#### RSMD Carousel

If the [Research Software Metadata Guidelines](https://fair-impact.github.io/RSMD-guidelines/)
working group releases new Aspects promoting CodeMeta, they should be added
to carousel on the front page. The carousel is built from `/data/rsmd.json`.

To add a new Aspect:

- Add an object to the array in `/data/rsmd.json` that contains the key-value
pairs `aspect`, `description`, `class`, and `link`.
  - `aspect` is the number of the new guideline.
  - `description` is a substring of the full guideline text.
  - `class` is the importance classification, ie `Useful`.
  - `link` is a direct link to the page onthe RSMD site.

Keeping the JSON file ordered by the `aspect` number will make it easier to
identify which Aspects are represented already.

### Updating the Tools page

The [Tools page](https://codemeta.github.io/tools/) structure is defined in
two shortcodes: `/layouts/shortcodes/tools.md` and 
`/layouts/shortcodes/unsupported-tools`.

Those shortcodes pull data from the JSON in the `/data/tool_categories.json`
and `data/tools.json` files, and from `.Site.Params.supported` which tracks
the current versions the website considers to be "Supported".

To add a new supported version, add a new item to the array in the `supported`
array. It is in the `Params` section of `/config.toml`.

To add a new tool:

- Add a new object to the array in `data/tools.json`, with the following
key-value pairs:
  - `name` is the name of the tool or project,
  - `language` is the tool's primary language, schema, etc. Useful for choosing
  a tool within limitations of an existing tech stack.
  - `versions` is an array of the versions that the tool has been tested with
  and found to be functional.
  - `maintainers` is an array of the maintainers. It consists of:
    - `name` is the name of the maintainer. Both individuals and groups are
    acceptable.
    - `url` *(optional)* can be any appropriate contact page for reaching out
    to the maintainer about the tool, if needed. This is typically a code forge
    account page, which that party has committed to the project with.
  - `description` is a sentance or two that explains what the tool does.
  - `url` is a link to a website where people may acquire the tool.
  - `categories` is a list of the categories the tool falls into. If the
  category has not beeb added to `/data/tool_categories.json`, there will be no
  section or table created for it on the page.
  
  To add a new tool category:
  
  - Add a new object to the array in `/data/tool_categories.json` with the following
  key-value pairs:
    `name` is a descriptive name for the category,
    `description` is a few sentences of text that introduces the category to
    potential users.
