.. _calibration:

#################
Image calibration
#################

On each post-ISR image, stars are detected to a 5-sigma threshold. These detections are then associated to identify a consistent set of isolated stars with multiple observations suitable for use in PSF modeling, photometric calibration, and astrometric calibration. An initial astrometric and photometric solution are fit using reference catalogs alone, and an initial PSF model is fit using PSFEx (E. Bertin 2011)) to serve as inputs to the calibration. These initial solutions are replaced as follows.

.. _calibration-astrometric:

Astrometric
===========

Starting from the astrometric solution calculated in single frame processing, the final astrometric solution is computed using the ensemble of visits in a given band, overlapping with a given tract. Isolated point sources are associated between overlapping visits and the Gaia DR3 reference catalog in order to constrain the model fit. The model used for DP1 consists of a static map from pixel-space to an intermediate frame (the per-detector model), followed by a per-visit map from the intermediate frame to the plane tangent to the telescope boresight (the per-visit model), then finally a deterministic mapping from the tangent plane to the sky. The fit is done using the gbdes package (Bernstein et al. 2017), and a full description is given in Saunders (2024).

The per-detector model is intended to capture quasi-static characteristics of the telescope and camera. During Rubin Operations, the astrometric solution will allow for separate epochs with different per-detector models, to account for changes in the camera due to warming and cooling and other discrete events. However, for DP1, LSSTComCam was assumed to be stable enough that all visits use the same per-detector model. The model itself is a separate two-dimensional polynomial for each detector. For DP1, a degree 4 polynomial was used; the degree of the polynomial mapping is tuned for each instrument and may be different for LSSTCam. Further improvements may be made by including a pixel-based astrometric offset mapping, which would be fit from the ensemble of astrometric residuals, but this is not included in the DP1 processing.

The per-visit model attempts to account for time-varying effects on the path of a photon from both atmospheric sources and those dependent on the telescope position. This model is also a polynomial mapping, in this case a degree 6 two-dimensional polynomial. Correction for differential chromatic refraction was not done for DP1, but will be included in LSSTCam processing during Operations. Future processing will also likely include a Gaussian Processes fit to better account for atmospheric turbulence, as was demonstrated in Fortino et al. (2021) and Léget et al. (2021).

The last component of the astrometric calibration is the position of the isolated point sources included in the fit. The positions consist of five parameters: position on the sky, proper motion, and parallax. The reference epoch for the fit positions is 2024.9.

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
