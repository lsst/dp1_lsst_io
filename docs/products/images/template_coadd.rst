.. _images-template-coadd:

##############
Template coadd
##############

The combination of processed images with the best seeing, for a patch of sky and for each of the six LSST filters, to be used as a template for difference imaging.

|template_coadd_doi|

Access
======

The template coadd images are accessible via the Butler, SIA, and TAP services.

Butler
------

* :ref:`Dataset type <products_butler_terminology>`\ : ('template_coadd', {**band**, **skymap**, **tract**, **patch**}, ExposureF)
* Format: FITS
* Number of Butler datasets: |template_coadd_butler_count|

SIA and TAP
-----------

Schema: `ObsCore table <https://sdm-schemas.lsst.io/ivoa_obscore.html>`_

IVOA calibration level: 3

Dataproduct subtype: ``lsst.template_coadd``


Description
===========

For DP1 the one-third of all visit images with the best seeing were
used as input images (or the best 12, if there were fewer than 36 images total).
A mean stacking algorithm, weighted by inverse variance, combines selected exposures.

Each individual template coadd image covers a single patch of the sky:
a quadrilateral sub-region of the overall skymap that covers approximately 79 square arcminutes.
Patches slightly overlap at their edges.
Template coadd images are for a single filter.

Processing
----------

The template coadd images are the result of :doc:`/processing/coaddition/index`,
and they are used in :doc:`/processing/dia/index`.

Pixel data
----------

The template coadd images have three planes of pixel data.

Image: sky pixel data in flux units of nJy.

Variance: uncertainty (noise) in the flux in units of nJy^2.

Mask: an integer bitmask of representative flag values that indicate processing status or issues,
similar to the `SDSS bitmasks <https://www.sdss4.org/dr17/algorithms/bitmasks/>`_.

Metadata
--------

The metadata for template coadd images retrieved from the Butler include a list of the input visit images,
and the derived PSF, photometric calibration, and WCS.

Tutorials
---------

See the :ref:`200-level notebook <notebook-200>` or :ref:`200-level portal <portal-200>`
tutorials demonstrating how to access the template coadd images.
