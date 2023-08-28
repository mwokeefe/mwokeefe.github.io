# Introduction

Personal site compiled using [Pelican](https://getpelican.com) and [ghp-import](https://github.com/c-w/ghp-import).
To install these prerequisites simply do:

```bash
pip install pelican ghp-import
```

# Publishing changes
Changes are made on the `dev` branch and the output published to `main` by running `./compile.sh`.
This pushes the `output` directory to main, which triggers a Github action to build and deploy the site.
Changes to the actual markdown content will also be pushed to the dev branch at the same time.