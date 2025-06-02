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

*PSF estimate algorithm.*


.. _calibration_background:

Background subtraction
======================

*How the background is estimated and subtracted.*
