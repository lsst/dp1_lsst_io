.. _images-raw:

#############
Raw exposures
#############

Unprocessed exposure from camera readout.

DOI: |doi_raw|


Access
======

The raw exposures are accessible via the butler, SIA, and TAP services.

Butler
------

Dataset type: ``('raw', {band, instrument, day_obs, detector, group, physical_filter, exposure}, Exposure)``

SIA and TAP
-----------

Schema: `ObsCore table <https://sdm-schemas.lsst.io/dp1.html#ObsCore>`_

IVOA calibration level: 1

Dataproduct subtype: ``lsst.raw``


Description
===========

Raw images from the camera are available exactly as they were read out of the camera.
The raw images should not be used for scientific analysis, and users should not attempt to rerun ISR.

Processing
----------

The raw exposures are first processed with the :doc:`/processing/isr/index` pipeline.

Pixel data
----------

The raw exposures have only an image plane, with no variance or mask planes like the visit images, because as those planes are a result of image processing and calibration.

Image: Sky pixel data in units of ADU (analog-digital units).

Metadata
--------

The metadata for raw exposures retrieved from the butler include
information about the observation (e.g., pointing, weather)
and an intial WCS.

Tutorials
---------

See the :ref:`200-level notebook <notebook-200>` or :ref:`200-level portal <portal-200>`
tutorials demonstrating how to access the raw exposures.
