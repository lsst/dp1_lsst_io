.. _images-deep-coadd:

##########
Deep coadd
##########

The combination of multiple processed, calibrated, and background-subtracted images, for a patch of sky, for each of the six LSST filters.

|deep_coadd_doi| [:download:`BibTeX </bib/butler-deep_coadd.bib>`]


Access
======

The deep coadd images are accessible via the Butler, SIA, and TAP services.

Butler
------

* :ref:`Dataset type <products_butler_terminology>`\ : ('deep_coadd', {**band**, **skymap**, **tract**, **patch**}, ExposureF)
* Format: FITS
* Number of Butler datasets: |deep_coadd_butler_count|

SIA and TAP
-----------

Schema: `ObsCore table <https://sdm-schemas.lsst.io/ivoa_obscore.html>`_

IVOA calibration level: 3

Dataproduct subtype: ``lsst.deep_coadd``


Description
===========

A DP1 visit image must have a PSF FWHM < 1.7 arcseconds to be selected as an input image to the coadd.
A mean stacking algorithm, weighted by inverse variance, combines selected exposures.

Each individual deep coadd image covers a single patch of the sky:
a quadrilateral sub-region of the overall skymap that covers approximately 128 square arcminutes, with 3400x3400 pixels at a pixel scale of 0.2 arcseconds per pixel.
Patches slightly overlap at their edges.
Deep coadd images are for a single filter and are aligned north-up, east-left such that RA, Dec correspond to x, y.

Processing
----------

The deep coadd images are the result of :doc:`/processing/coaddition/index`.

Pixel data
----------

The deep coadd images have three planes of pixel data.

Image: sky pixel data in flux units of nJy.

Variance: uncertainty (noise) in the flux in units of nJy^2.

Mask: an integer bitmask of representative flag values that indicate processing status or issues,
similar to the `SDSS bitmasks <https://www.sdss4.org/dr17/algorithms/bitmasks/>`_.

Metadata
--------

The metadata for deep coadd images retrieved from the Butler include a list of the input visit images,
and the derived PSF, photometric calibration, and WCS.

WCS
"""

The World Coordinate System objects for coadd images are exactly representable as FITS (they are simple TAN projections), but each ``tract`` has its own WCS that is shared by all ``patches``, with an integer offset that must be applied for each patch manually to index the pixel arrays.

See :ref:`products_wcs_known_issues` for more information.

Tutorials
---------

See the :ref:`200-level notebook <notebook-200>` or :ref:`200-level portal <portal-200>`
tutorials demonstrating how to access the deep coadd images.
