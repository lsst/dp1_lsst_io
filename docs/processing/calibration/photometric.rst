.. _photometric:

#######################
Photometric calibration
#######################

*Overview of what it means and the steps involved.*

* input: post-ISR exposure
* identify bright isolated stars
* cross-match to the monster
* other things happen
* output: ``visit_image``

Photometric calibration uses the Forward Global Calibration Method (FGCM; `Burke et al. 2018 <https://ui.adsabs.harvard.edu/abs/2018AJ....155...41B/abstract>`_).

.. _photometric-monster:

The Monster
===========

Both photometric and astrometric calibration make use of a custom reference catalog referred to as "`the Monster <https://dmtn-277.lsst.io/>`_".
The Monster is a whole-sky catalog built specifically for LSST, as no prior reference catalog had both the depth and coverage needed to calibrate LSST data.
The Monster combines data from multiple previous reference catalogs, including Dark Energy Survey, Pan-STARRS, and Gaia, and contains only stellar sources.


