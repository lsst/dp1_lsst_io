# See the documenteer.toml for overrides of the Rubin user guide presets

from documenteer.conf.guide import *  # noqa: F401, F403

# Content in the _static directory is copied into the HTML build without
# processing. Conventionally images should be placed alongside source files,
# but they can also be sourced from this directory too.
html_static_path.append("docs/_static")
