.. _calibrations:

############
Calibrations
############

Calibration products (e.g., combined bias, dark, and flat frames).


DOI: |calibrations_doi|


Access
======

The calibration products are accessible via the butler.

Butler
------

Number of Butler datasets: |calibrations_butler_count|

Examples of dataset types:

* ``('bias', {instrument, detector}, ExposureF, isCalibration=True)``
* ``('dark', {instrument, detector}, ExposureF, isCalibration=True)``
* ``('flat', {band, instrument, detector, physical_filter}, ExposureF, isCalibration=True)``

Other calibrations dataset types include ``ptc`` for Photon Transfer Curve and ``bfk`` for brighter-fatterkernel.

Description
===========

The process of Instrument Signature Removal (ISR; also called "image reduction") uses calibration products such as bias, dark, and flat field calibration frames as part of the process to transform raw images into visit images.

**Bias images**: An exposure obtained with zero exposure time to measure the pedestal level of counts applied during readout.

**Dark frames**: An exposure obtained with a nonzero exposure time but with no illumination (shutter closed) to measure the detector's response to the thermal energy in the camera.

**Flat fields**: An exposure taken with even illumination across the field to measure pixel response variations.

Processing
----------

The calibration products are used in the :doc:`/processing/isr/index` pipeline.

Pixel data
----------

``ExposureF`` calibration products such as the combined bias, dark, and flat have an image plane and a variance plane.

The pixel data units are ADU (analog-to-digital units).

Metadata
--------

``ExposureF`` calibration frames have a header and bounding box, but don't have a World Coordinate System (WCS) object.

Tutorials
---------

See the :ref:`200-level notebook <notebook-200>` tutorial demonstrating how to access the calibration products.
