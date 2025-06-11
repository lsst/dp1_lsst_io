.. _photometric:

#######################
Photometric calibration
#######################

Photometric calibration corrects the observed flux for attenuation from the atmosphere, filters, optics, and detector quantum efficiency.

Photometric calibration uses the Forward Global Calibration Method (FGCM; `Burke et al. 2018 <https://ui.adsabs.harvard.edu/abs/2018AJ....155...41B/abstract>`_).

For a description of the photometric calibration steps, refer to the "Rubin Baseline Calibration Plan" (`sitcomtn-086.lsst.io <https://sitcomtn-086.lsst.io/>`_).

The steps of photometric calibration include:

* chromatic corrections
* observed passbands
* instrumental response (quantum efficiency)
* opacity of the optical system
* chromatic throughput
* reference flux flats
* atmospheric response


Overview
========

All stars with observations with signal-to-noise greater than 10 are input into the FGCM solution,
and associated stars from the global absolute reference catalog refered to as :doc:`/processing/calibration/monster`.
The FGCM model constrains the atmospheric parameters per night, as well as the absolute throughput.



