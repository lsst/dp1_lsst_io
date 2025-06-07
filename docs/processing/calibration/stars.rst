.. _stars:

#################
Calibration stars
#################

On each post-ISR image, stars are detected to a 5-sigma threshold.

These detections are then associated to identify a consistent set of isolated stars with multiple observations suitable for use in PSF modeling, photometric calibration, and astrometric calibration.

An initial astrometric and photometric solution are fit using reference catalogs alone, and an initial PSF model is fit using PSFEx (`Bertin 2011 <https://ui.adsabs.harvard.edu/abs/2011ASPC..442..435B/abstract>`_) to serve as inputs to the calibration.
