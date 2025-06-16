.. _calibrations:

############
Calibrations
############

Calibration images (bias, dark, and flat frames).

DOI: |doi_calibrations|


Access
======

The calibration frames are accessible via the butler.

Butler
------

Dataset types:

* ``('bias', {instrument, detector}, ExposureF, isCalibration=True)``
* ``('dark', {instrument, detector}, ExposureF, isCalibration=True)``
* ``('flat', {band, instrument, detector, physical_filter}, ExposureF, isCalibration=True)``


Description
===========

The process of Instrument Signature Removal (ISR; also called "image reduction") uses bias, dark, and flat field calibration frames as part of the process to transform raw images into visit images.

**Bias images**: An exposure obtained with zero exposure time to measure the pedestal level of counts applied during readout.

**Dark frames**: An exposure obtained with a nonzero exposure time but with no illumination (shutter closed) to measure the detector's response to the thermal energy in the camera.

**Flat fields**: An exposure taken with even illumination across the field to measure pixel response variations.

Processing
----------

The calibration frames are used in the :doc:`/processing/isr/index` pipeline.

Pixel data
----------

The calibration frames have an image plane and a variance plane.

The pixel data units are ADU (analog-digital units).

Metadata
--------

Calibration frames have a header and bounding box, but no WCS.

Tutorials
---------

See the :ref:`200-level notebook <notebook-200>` tutorial demonstrating how to access the calibration frames.