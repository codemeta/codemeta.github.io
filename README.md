# CodeMeta Website

This website is written in [Hugo](https://hugodocs.info).  Hugo is the static website engine behind the wonderful RStudio package `blogdown`, and is fast, popular, and easy to install and theme. See the [Hugo docs](https://hugodocs.info) for a quick orientation on how the site is organized.  `blogdown` makes it easy to run Hugo from the RStudio editor and include R code in `.Rmd` content in Hugo sites.  

To build and preview the site from RStudio, just use `blogdown::serve_site()`.  `blogdown::install_hugo()` will get you set up the first time.  

Hugo source files are located on the `hugo` branch of the `codemeta.github.io` repository (now the default branch on GitHub).  So far we haven't set up automated builds, so deploying static sites on `*.github.io` repos is still a nuciance since the website must be on `master` branch.  Building this repo will create and write the static site to `../website`.  I recommend setting the upstream origin of `website` to `codemeta.github.io` master branch (e.g. checkout the master branch and copy `.git` dir into `website/` to deploy.)s