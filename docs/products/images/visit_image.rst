.. _images-visit-image:

###########
Visit image
###########

Individual processed and calibrated sky images.

|visit_image_doi|

Access
======

The visit images are accessible via the Butler, SIA, and TAP services.

Butler
------

* Dataset type: ('visit_image', {band, **instrument**, day_obs, **detector**, physical_filter, **visit**}, ExposureF)
* Format: FITS
* Number of Butler datasets: |visit_image_butler_count|

SIA and TAP
-----------

Schema: `ObsCore table <https://sdm-schemas.lsst.io/dp1.html#ObsCore>`_

IVOA calibration level: 2

Dataproduct subtype: ``lsst.visit_image``


Description
===========

Raw images from the camera undergo processing that includes
instrument signature removal (ISR),
image calibration (photometric and astrometric),
and PSF estimation.
The result is a fully calibrated visit image.

Each individual visit image contains data from one of the camera's detectors.

Processing
----------

The visit images are the result of :doc:`/processing/calibration/index`.

Pixel data
----------

The visit images have three planes of pixel data.

Image: Sky pixel data in flux units of nJy.

Variance: Uncertainty (noise) in the flux in units of nJy^2.

Mask: An integer bitmask of representative flag values that indicate processing status or issues,
similar to the `SDSS bitmasks <https://www.sdss4.org/dr17/algorithms/bitmasks/>`_.

Metadata
--------

The metadata for visit images retrieved from the Butler include
information about the observation (e.g., pointing, weather),
and the derived PSF, photometric calibration, and WCS.

Tutorials
---------

See the :ref:`200-level notebook <notebook-200>` or :ref:`200-level portal <portal-200>`
tutorials demonstrating how to access the visit images.
