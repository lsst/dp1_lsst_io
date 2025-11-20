.. _images-visit-image:

###########
Visit image
###########

Individual processed and calibrated sky images.

|visit_image_doi| [:download:`BibTeX </bib/butler-visit_image.bib>`]

Access
======

The visit images are accessible via the Butler, SIA, and TAP services.

Butler
------

* :ref:`Dataset type <products_butler_terminology>`\ : ('visit_image', {band, **instrument**, day_obs, **detector**, physical_filter, **visit**}, ExposureF)
* Format: FITS
* Number of Butler datasets: |visit_image_butler_count|

SIA and TAP
-----------

Schema: `ObsCore table <https://sdm-schemas.lsst.io/ivoa_obscore.html>`_

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
Visit images are rotated, and not aligned north-up east-left, such that RA, Dec do not correspond to x, y.

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

WCS
"""

The World Coordinate System objects for visit images are not exactly representable as FITS; the FITS headers have an approximation that is good enough only for visualization.
Transformations with the true WCS are currently only possible using LSST Science Pipelines libraries, and those can be easy to misuse.
See :ref:`products_wcs_known_issues` for more information.

Note also that the pixel scale in a visit image can vary with position.
If one wishes to use the pixel scale, it is recommended to extract it using the "getPixelScale" method associated with the visit images' WCS.
This function should *always* be given an argument with x, y coordinates, so that a typical call (for an x, y position of 1000, 1400) may look like: ``wcs.getPixelScale(lsst.geom.Point2D(1000, 1400)).asArcseconds()`` (where "wcs" is the WCS associated with a visit image, the "Point2D" function comes from the "lsst.geom" package, and the final portion converts the result to arcseconds).

Tutorials
---------

See the :ref:`200-level notebook <notebook-200>` or :ref:`200-level portal <portal-200>`
tutorials demonstrating how to access the visit images.
