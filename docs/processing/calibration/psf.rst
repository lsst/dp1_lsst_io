.. _psf:

##############
PSF estimation
##############

PSF modeling in DP1 uses the Piff (`Jarvis et al. 2021 <https://ui.adsabs.harvard.edu/abs/2021MNRAS.501.1282J/abstract>`_) algorithm.
Its models represent the PSF on a pixel-by-pixel basis and interpolate its parameters across a single CCD using two-dimensional polynomials.
Piff utilizes its pixel grid model with a fourth-order polynomial interpolation per CCD, except in the u-band, where star counts are insufficient to support a fourth-order fit. In this case, a second-order polynomial is used instead.
