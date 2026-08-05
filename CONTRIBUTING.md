# Contributing to the CodeMeta site

## Adding new Crosswalks

Crosswalks are developed in
[the main CodeMeta repository](https://github.com/codemeta/codemeta) and are
periodically synchronised into the website. A markdown file is
automatically generated on the website for each Crosswalk when the `Makefile`
is run during deployment.

[!WARNING] Do *not* manually create these markdown files. They will be 
overwritten or duplicated.

By default, the generated markdown files are very basic and variations may
be desired. To allow for custom information, overrides can be defined in
`/data/crosswalk_pages.json`. Many Crosswalks have already been enhanced.

A complete set of the override fields would look like this:

```
    {
        "stem":"My Crosswalk",
        "name":"My Crosswalk metadata",
        "short":"mycrosswalk",
        "desc":"My Crosswalk metadata is very cool. [This field can have markdown](https://codemeta.github.io).",
        "foot":"See crosswalk for [My Other Crosswalk](https://codemeta.github.io).",
        "img":"codemeta.png",
        "date":"2026-07-04"
    },
```

[!NOTE] Remember to escape `"` if used.

  - `stem` _(required)_ must be *exactly* what the vocabulary's header is
[in its crosswalk .csv](https://github.com/codemeta/codemeta/blob/master/crosswalks).
It is the only individually required field, but there is no point to adding it if
no other fields are populated.
  - `name` is the full name of the crosswalk, if it is longer than in the header,
  - `short` is a short name for the crosswalk for a cleaner or shorter url,
  - `desc` is a more verbose description than the default provided by the script,
  - `foot` is an extension of the description that appears after the crosswalk table,
  - `img` is the filename and extension of the image. If it is not already in *this*
repository, you will need to include it in your Pull Request that adds it to this JSON.
Image files go in `static/img`,
  - `date` is the date that the vocabulary's crosswalk was added to CodeMeta.

Page generation can be triggered by running `python3 scripts/crosswalk_to_pages`.

If you add or change a `short` override, your local copy may retain the previously named
file in the directory. Rebuilding with `--cleanDestinationDir` may fix this.

Any issues with the automatic generation of the markdown files should be raised against this
repository.

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
