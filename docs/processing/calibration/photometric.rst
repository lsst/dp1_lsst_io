.. _photometric:

#######################
Photometric calibration
#######################

Photometric calibration involves determining how to convert raw "counts" recorded by the camera into images and catalogs reporting fluxes calibrated onto a standard system (in this case, in units of nanoJansky (nJy)). This includes correcting for effects in the detectors themselves (discussed in :doc:`/processing/isr`) as well as filter throughputs, and atmospheric transparency, which varies with airmass and time.

For a description of the photometric calibration steps and hardware to enable them, refer to the "Rubin Baseline Calibration Plan" (`sitcomtn-086.lsst.io <https://sitcomtn-086.lsst.io/>`_).

**System characterization:** Initial steps *not requiring on-sky data* to characterize the instrumental and overall system properties included:
* Measuring LSSTComCam's instrumental response as a function of wavelength and position on the focal plane (mostly measured in the lab prior to going on sky).
* Measuring the throughput of the filters (also as a function of position -- for DP1 this came from measurements performed by the vendors who manufactured the filters).
* Eventually this will include measuring the optical system throughput as a function of wavelength using a collimated beam projector (CBP) and a tunable laser. This hardware was not available during the LSSTComCam on-sky campaign.

**Calibration using on-sky data:** On-sky images are used to characterize the system, and of course must be calibrated themselves to measure atmospheric and other time-varying effects. After :doc:`/processing/isr` has been performed on the images, additional photometric calibration steps include:
* Flat-fielding to normalize pixel-to-pixel response. For LSSTComCam observing, the calibration screen was not yet available in the dome, so dithered images of the sky were taken during twilight hours and combined to create twilight flats.
* Initial calibration is performed by detecting sources, estimating the point-spread function (PSF), then fitting an initial solution to :doc:`/processing/calibration/monster` reference catalog. The main purpose of this step is to provide a good enough photometric and astrometric calibration to enable associating multiple observations of stars.
* The final, global photometric calibration uses the Forward Global Calibration Method (FGCM; `Burke et al. 2018 <https://ui.adsabs.harvard.edu/abs/2018AJ....155...41B/abstract>`_). FGCM takes stars with S/N > 10 plus their matched counterparts from The Monster, and forward models repeated measurements of stars to determine parameters describing the atmospheric transmittance and instrumental response that minimize the scatter in the stars' magnitudes. The fits result in a measure of the wavelength-dependent observational passband at the time of each measurement. The intrinsic repeatability of DP1 photometry was typically about 1 mmag in *grizy* bands and roughly 5 mmag in *u* band.
* The ECDFS field observed in DP1 overlapped the spectrophotometric flux standard C26202 (a `CALSPEC <https://www.stsci.edu/hst/instrumentation/reference-data-for-calibration-and-tools/astronomical-catalogs/calspec>`_ standard). Comparison of DP1 photometry to synthetic photometry of C26202 was used to determine that our estimated absolute system throughputs were accurate to at least 5%, and the absolute calibration of DP1 data is accurate to better than 1% for all bands besides *u*-band.

