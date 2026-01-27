.. _images:

######
Images
######

Images of the sky in the six LSST filters with a variety of calibration levels.

The `schema browser <https://sdm-schemas.lsst.io/>`_ includes tables of image metadata (``ObsCore``).

Image data products are available via the butler, SIA, and TAP services.
See the following resources to get started with these services:

* :doc:`/tutorials/index`
* :doc:`/products/adql_queries`
* :doc:`/products/butler_terminology`


Coadd images
============

Combinations of multiple calibrated images of the same region of the sky to achieve
greater depth (to detect fainter objects),
or for use as templates in difference image analysis.


.. toctree::
    :maxdepth: 1
    :titlesonly:
    :glob:

    deep_coadd
    template_coadd



Visit images
============

Processed and calibrated images from individual visits (single observations).

.. toctree::
    :maxdepth: 1
    :titlesonly:
    :glob:

    visit_image



Difference images
=================

Created by subtracting a template image from a visit image.

.. toctree::
    :maxdepth: 1
    :titlesonly:
    :glob:

    difference_image


Raw exposures
=============

The unprocessed images received directly from the camera.

.. toctree::
    :maxdepth: 1
    :titlesonly:
    :glob:

    raw_exposure

Mask planes
===========

Image mask planes.

.. toctree::
    :maxdepth: 1
    :titlesonly:
    :glob:

    mask_planes
