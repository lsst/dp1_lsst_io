.. _psf:

#############################################
Point spread function modeling (PSF) modeling
#############################################

PSF modeling characterizes the shape of point sources after they have been "blurred" by the atmosphere and optical system into a two-dimensional shape on the detector.

PSF modeling in DP1 uses the Piff (`Jarvis et al. 2021 <https://ui.adsabs.harvard.edu/abs/2021MNRAS.501.1282J/abstract>`_) algorithm.

Overview
========

Bright, isolated stars are detected in post-ISR images and used for PSF modeling.

The Piff models represent the PSF on a pixel-by-pixel basis and interpolate its parameters across a single CCD using two-dimensional polynomials.
Piff utilizes its pixel grid model with a fourth-order polynomial interpolation per CCD, except in the u-band, where star counts are insufficient to support a fourth-order fit.
In this case, a second-order polynomial is used instead.

Two Piff features were not used.
First, PSF color dependence was not yet implemented but will be added in the future.
Second, although the current Rubin software allows Piff to operate in sky coordinates (including WCS transformations),
it does not yet correct for sensor-induced astrometric distortions (e.g., tree rings); this functionality will also be added in the future.