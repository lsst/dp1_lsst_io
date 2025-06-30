.. _images-raw:

############
Raw exposure
############

Unprocessed exposure from camera readout.

|raw_doi|


Access
======

The raw exposures are accessible via the Butler, SIA, and TAP services.

Butler
------

* :ref:`Dataset type <products_butler_terminology>`\ : ('raw', {band, **instrument**, day_obs, **detector**, group, physical_filter, **exposure**}, Exposure)
* Format: FITS
* Number of Butler datasets: |raw_butler_count|

SIA and TAP
-----------

Schema: `ObsCore table <https://sdm-schemas.lsst.io/ivoa_obscore.html>`_

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

The raw exposures have only an image plane, with no variance or mask planes like the visit images, because those planes are a result of image processing and calibration.

Image: sky pixel data in units of ADU (analog-digital units).

Metadata
--------

The metadata for raw exposures retrieved from the Butler include
information about the observation (e.g., pointing, weather)
and an initial WCS estimated from the telescope boresight.

Tutorials
---------

See the :ref:`200-level notebook <notebook-200>` or :ref:`200-level portal <portal-200>`
tutorials demonstrating how to access the raw exposures.
