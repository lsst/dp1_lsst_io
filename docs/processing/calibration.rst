.. _calibration:

#################
Image calibration
#################

On each post-ISR image, stars are detected to a 5-sigma threshold. These detections are then associated to identify a consistent set of isolated stars with multiple observations suitable for use in PSF modeling, photometric calibration, and astrometric calibration. An initial astrometric and photometric solution are fit using reference catalogs alone, and an initial PSF model is fit using PSFEx (E. Bertin 2011)) to serve as inputs to the calibration. These initial solutions are replaced as follows.

.. _calibration-astrometric:

Astrometric
===========

*Briefly how the astrometric solution and WCS is done.*


.. _calibration-photmetric:

Photometric
===========

*Briefly how the visit images are photometrically calibrated.*


.. _calibration_psf:

Point spread function estimation
================================

PSF modeling in DP1 uses the Piff (M. Jarvis et al. 2021) algorithm. Its models represent the PSF on a pixel-by-pixel basis and interpolate its parameters across a single CCD using two-dimensional polynomials. Piff utilizes its pixel grid model with a fourth-order polynomial interpolation per CCD, except in the u-band, where star counts are insufficient to support a fourth-order fit. In this case, a second-order polynomial is used instead.


.. _calibration_background:

Background subtraction
======================

*How the background is estimated and subtracted.*
