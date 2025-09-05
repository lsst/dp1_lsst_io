.. _calibrations:

############
Calibrations
############

Calibration products (e.g., combined bias, dark, and flat frames).


|calibrations_doi| [:download:`BibTeX </bib/butler-calibrations.bib>`]


Access
======

The calibration products are accessible via the Butler.

Unlike other data products, most calibrations are associated with a "validity range" as well as a :ref:`data ID <products_butler_terminology>` (e.g. ``detector`` and ``physical_filter``) in the butler, since different calibrations can be valid for different observations.
This is usually best provided by also passing an ``exposure`` or ``visit`` ID when looking up a calibration in addition to the calibration's regular data ID dimensions, since both ``exposure`` and ``visit`` are associated with a timespan in the butler database.

Butler
------

Number of Butler datasets: |calibrations_butler_count|

Examples of dataset types:

* ``('bias', {instrument, detector}, ExposureF, isCalibration=True)``
* ``('dark', {instrument, detector}, ExposureF, isCalibration=True)``
* ``('flat', {band, instrument, detector, physical_filter}, ExposureF, isCalibration=True)``

Other calibrations dataset types include ``ptc`` for Photon Transfer Curve and ``bfk`` for brighter-fatter kernel.

Description
===========

The process of Instrument Signature Removal (ISR; also called "image reduction") uses calibration products such as bias, dark, and flat field calibration frames as part of the process to transform raw images into visit images.

**Bias images**: An exposure obtained with zero exposure time to measure the pedestal level of counts applied during readout.

**Dark frames**: An exposure obtained with a nonzero exposure time but with no illumination (shutter closed) to measure the detector's response to the thermal energy in the camera.

**Flat fields**: An exposure taken with even illumination across the field to measure pixel response variations.

Processing
----------

The calibration products are created by processing calibration images and used in the :doc:`/processing/isr/index` pipeline.

Pixel data
----------

``ExposureF`` calibration products such as the combined bias, dark, and flat have an image plane and a variance plane.

The pixel data units are ADU (analog-to-digital units).

Metadata
--------

``ExposureF`` calibration frames have a header and bounding box but don't have a World Coordinate System (WCS) object.

Tutorials
---------

See the :ref:`200-level notebook <notebook-200>` tutorial demonstrating how to access the calibration products.
