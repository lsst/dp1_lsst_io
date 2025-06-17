.. _calibrations:

############
Calibrations
############

Calibration products (e.g., combined bias, dark, and flat frames).


DOI: |doi_calibrations|


Access
======

The calibration products are accessible via the butler.

Butler
------

Examples of dataset types:

* ``('bias', {instrument, detector}, ExposureF, isCalibration=True)``
* ``('dark', {instrument, detector}, ExposureF, isCalibration=True)``
* ``('flat', {band, instrument, detector, physical_filter}, ExposureF, isCalibration=True)``


Description
===========

The process of Instrument Signature Removal (ISR; also called "image reduction") uses calibration products such as bias, dark, and flat field calibration frames as part of the process to transform raw images into visit images.

**Bias images**: An exposure obtained with zero exposure time to measure the pedestal level of counts applied during readout.

**Dark frames**: An exposure obtained with a nonzero exposure time but with no illumination (shutter closed) to measure the detector's response to the thermal energy in the camera.

**Flat fields**: An exposure taken with even illumination across the field to measure pixel response variations.

For descriptions of the ISR steps and the generation, verification, certification, approval, and distribution of the calibration products necessary for ISR, refer to the paper `Instrument Signature Removal and Calibration Products for the Rubin Legacy Survey of Space and Time <https://ui.adsabs.harvard.edu/abs/2025JATIS..11a1209P/abstract>`_, the "Rubin Baseline Calibration Plan" (`SITCOMTN-086 <https://sitcomtn-086.lsst.io/>`_), and the "Verifying LSST Calibration Data Products" (`DMTN-101 <https://dmtn-101.lsst.io/>`_) and "Calibration Generation, Verification, Acceptance, and Certification" (`DMTN-222 <https://dmtn-222.lsst.io/>`_) technical notes.

Processing
----------

The calibration products are used in the :doc:`/processing/isr/index` pipeline.

Pixel data
----------

The "afw ExposureF" calibration products such as the combined bias, dark, and flat have an image plane and a variance plane.

The pixel data units are ADU (analog-digital units).

Metadata
--------

"afw ExposureF" calibration frames have a header and bounding box, but no WCS.

Tutorials
---------

See the :ref:`200-level notebook <notebook-200>` tutorial demonstrating how to access the calibration products.
