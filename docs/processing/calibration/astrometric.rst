.. _astrometric:

#######################
Astrometric calibration
#######################

The astrometric calibrations define the World Coordinate System (WCS) of an image, the relation between pixel coordinates and sky coordinates (Right Ascension and Declination).

Astrometric calibration uses the ``gbdes`` package (`Bernstein et al. 2017 <https://ui.adsabs.harvard.edu/abs/2017PASP..129g4503B/abstract>`_).

For a description of the implementation of ``gbdes``, see "Astrometric Calibration in the LSST Pipeline" (`dmtn-266.lsst.io <https://dmtn-266.lsst.io/>`_).

Overview
========

Bright, isolated stars detected in the post-ISR images are used to obtain an initial astrometric solution.

The final astrometric solution is computed using the ensemble of visits in a given band, overlapping with a given tract.
Isolated point sources are associated between overlapping visits and the Gaia DR3 reference catalog in order to constrain the model fit.
The model used for DP1 consists of a static map from pixel-space to an intermediate frame (the per-detector model), followed by a per-visit map from the intermediate frame to the plane tangent to the telescope boresight (the per-visit model), then finally a deterministic mapping from the tangent plane to the sky.
The fit is done using the gbdes package (`Bernstein et al. 2017 <https://ui.adsabs.harvard.edu/abs/2017PASP..129g4503B/abstract>`_), as described in `Saunders (2024) <https://dmtn-266.lsst.io/>`_.

The per-detector model is intended to capture quasi-static characteristics of the telescope and camera.
During Rubin Operations, the astrometric solution will allow for separate epochs with different per-detector models, to account for changes in the camera due to warming and cooling and other discrete events.
However, for DP1, LSSTComCam was assumed to be stable enough that all visits use the same per-detector model.
The model itself is a separate two-dimensional polynomial for each detector.
For DP1, a degree 4 polynomial was used; the degree of the polynomial mapping is tuned for each instrument and may be different for LSSTCam.
Further improvements may be made by including a pixel-based astrometric offset mapping, which would be fit from the ensemble of astrometric residuals, but this is not included in the DP1 processing.

The per-visit model attempts to account for time-varying effects on the path of a photon from both atmospheric sources and those dependent on the telescope position.
This model is also a polynomial mapping, in this case a degree 6 two-dimensional polynomial.
Correction for differential chromatic refraction was not done for DP1, but will be included in LSSTCam processing during Operations.
Future processing will also likely include a Gaussian Processes fit to better account for atmospheric turbulence, as was demonstrated in `Fortino et al. (2021) <https://ui.adsabs.harvard.edu/abs/2021AJ....162..106F/abstract>`_ and `Léget et al. (2021) <https://ui.adsabs.harvard.edu/abs/2021A%26A...650A..81L/abstract>`_.

The last component of the astrometric calibration is the position of the isolated point sources included in the fit.
The positions consist of five parameters: position on the sky, proper motion, and parallax. The reference epoch for the fit positions is 2024.9.
