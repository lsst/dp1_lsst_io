.. _photometric:

#######################
Photometric calibration
#######################

Photometric calibration involves determining how to convert raw "counts" recorded by the camera into images and catalogs reporting fluxes calibrated onto a standard system (in this case, in units of nanoJansky (nJy)). This includes correcting for effects in the detectors themselves (discussed in :doc:`/processing/isr`) as well as filter throughputs, and atmospheric transparency, which varies with airmass and time.


For a description of the photometric calibration steps and hardware to enable them, refer to the "Rubin Baseline Calibration Plan" (`sitcomtn-086.lsst.io <https://sitcomtn-086.lsst.io/>`_).

CHARACTERIZING THE INSTRUMENTAL/SYSTEM PROPERTIES: The initial steps toward measuring the full system throughput included:
* Measuring LSSTComCam's instrumental response as a function of wavelength and position on the focal plane (mostly measured in the lab prior to going on sky)
* Measuring the throughput of the filters (also as a function of position -- for DP1 this came from measurements performed by the vendors who manufactured the filters)
* ???measuring the optical system throughput as a function of wavelength (CBP? Not for ComCam, methinks?)

USING ON-SKY DATA TO MEASURE ATMOSPHERIC AND OTHER TIME-VARYING EFFECTS: After :doc:`/processing/isr`, the following steps are performed:
* flat-fielding (using twilight flats for DP1 because calibration screen wasn't ready in the dome yet)
* detect, estimate PSF, then perform initial solution to :doc:`/processing/calibration/monster` reference catalog. This step is really just used for associating multiple observations of stars.
* FGCM takes stars with S/N > 10 plus their matched counterparts from The Monster, and forward models all of it together to go from the instrumental fluxes to determine XXXXXXXXXXXXXXXXXXXXX
* checking against spectrophotometric flux standards (CALSPEC -- link!) to confirm/tweak(?) solution

The final, global photometric calibration uses the Forward Global Calibration Method (FGCM; `Burke et al. 2018 <https://ui.adsabs.harvard.edu/abs/2018AJ....155...41B/abstract>`_).

FGCM models repeated measurements of stars to determine parameters describing the atmospheric transmittance and instrumental response that minimize the scatter in the stars' magnitudes. The fits result in a measure of the wavelength-dependent observational passband at the time of each measurement.

FGCM constrains the atmospheric throughput and (OTHER PARAMS) per night, the absolute throughput, variations in the detector chromatic throughput, and the illumination correction, among other params. The repeatability after FGCM was typically YYYYYYY.

* chromatic corrections
* observed passbands
* instrumental response (quantum efficiency)
* opacity of the optical system
* chromatic throughput
* reference flux flats
* atmospheric response


Overview
========

Bright, isolated stars with signal-to-noise > 10 that are detected in post-ISR images,
and associated with the global absolute reference catalog referred to as :doc:`/processing/calibration/monster`,
are input into the FGCM solution.
The FGCM model constrains the atmospheric parameters per night, as well as the absolute throughput.

