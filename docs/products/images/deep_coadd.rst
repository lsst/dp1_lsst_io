.. _images-deep-coadd:

##########
Deep coadd
##########

The combination of multiple processed, calibrated, and background-subtracted images, for a patch of sky, for each of the six LSST filters.

|deep_coadd_doi|


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

Schema: `ObsCore table <https://sdm-schemas.lsst.io/dp1.html#ObsCore>`_

IVOA calibration level: 3

Dataproduct subtype: ``lsst.deep_coadd``


Description
===========

A DP1 visit image must have a PSF FWHM < 1.7 arcseconds to be selected as an input image to the coadd.
A mean stacking algorithm, weighted by inverse variance, combines selected exposures.

Each individual deep coadd image covers a single patch of the sky:
a quadrilateral sub-region of the overall skymap that covers approximately 79 square arcminutes.
Patches slightly overlap at their edges.
Deep coadd images are for a single filter.

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

Tutorials
---------

See the :ref:`200-level notebook <notebook-200>` or :ref:`200-level portal <portal-200>`
tutorials demonstrating how to access the deep coadd images.
