# See the documenteer.toml for overrides of the Rubin user guide presets

from documenteer.conf.guide import *  # noqa: F401, F403
nb_execution_mode = 'off'

linkcheck_ignore = [
    r'https://www\.lsst\.org/content/lsst-statement-regarding-increased-deployment-satellite-constellations',
]

