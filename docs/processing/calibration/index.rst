.. _calibration:

#################
Image calibration
#################

Bright, isolated stars are detected in images and used for the photometric, astrometric, and PSF calibrations.

On each post-ISR image, bright, isolated stars are detected to a 5-sigma threshold.
These detections are then associated to identify a consistent set of isolated stars with multiple observations,
suitable for use in modeling the point-spread function (PSF), and for performing photometric and astrometric calibrations.



.. _calibration-monster:

The Monster catalog
===================


.. toctree::
    :maxdepth: 1
    :titlesonly:
    :glob:

    monster



.. _calibration-photmetric:

Photometric calibration
=======================

Photometric calibrations correct the counts (electrons) measured by the camera to the incident flux from a source at Earth before it enters the atmosphere.

.. toctree::
    :maxdepth: 1
    :titlesonly:
    :glob:

    photometric



.. _calibration-astrometric:

Astrometric calibration
=======================

Astrometric calibrations define the World Coordinate System (WCS) of an image, the relation between pixel coordinate and sky coordinate (Right Ascension and Declination).

.. toctree::
    :maxdepth: 1
    :titlesonly:
    :glob:

    astrometric



.. _calibration_psf:

Point spread function modeling
==============================

Characterizing how the optical system "blurs" a point source into a two-dimensional shape on the detector.

.. toctree::
    :maxdepth: 1
    :titlesonly:
    :glob:

    psf


.. _calibration_background:

Background subtraction
======================


.. toctree::
    :maxdepth: 1
    :titlesonly:
    :glob:

    backgrounds
