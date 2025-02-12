# Data Preview 1 Documentation

This is the source for the Vera C. Rubin Observatory Documentation for Data Preview 1 (DP1), available at https://dp1.lsst.io.

This site is built with Rubin Observatory's [Documenteer User Guide theme](https://documenteer.lsst.io/guides/index.html).

## Building the site

To build this documentation site you need Python 3.11 or later.
To get started, clone this repository:

```bash
git clone https://github.com/lsst/dp1_lsst_io
cd dp1_lsst_io
```

Set up and activate a Python virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

### Dependencies

Install the dependencies:

```bash
make init
```

### Building the site

Build the site's HTML:

```bash
make html
```

The built HTML files will be in `_build/html`.

### Cleaning up a build

To clean up the build files:

```bash
make clean
```

It can be useful to clean up the build if you are having issues with the build.

### Linting issues

You can check for formatting issues with the Pre-commit hooks by running:

```bash
make lint
```

These pre-commit hooks are also run automatically on commit if you previously ran `make init`.

You can also check for broken links with:

```bash
make linkcheck
```

Some broken links may be false positives that need to be ignored by a configuration in `technote.toml`.
See the [Documenteer docs for the sphinx.linkcheck configuration](https://documenteer.lsst.io/guides/toml-reference.html#sphinx-linkcheck).

## GitHub Actions and Publishing

A GitHub Actions workflow (`.github/workflows.ci.yaml`) handles testing, building, and publishing the site.
Pushes to the `main` branch trigger a new build and deployment of the site.
Pull requests made from branches on this repository also trigger builds, with deployments to `dp1.lsst.io/v` for preview.

> [!NOTE]
> Deployments to dp1.lsst.io are currently disabled while the site is under development. To enable deployments, remove the `if: false` condition from the `upload` job in `.github/workflows/ci.yaml`. In the meantime, the built html files can either be viewed locally or downloaded as Artifacts in [Actions tab of the repository](https://github.com/lsst/dp1_lsst_io/actions) for specific builds.
