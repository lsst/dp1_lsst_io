.. _images:

######
Images
######

Images of the sky in the six LSST filters with a variety of calibration levels.

The `schema browser <https://sdm-schemas.lsst.io/>`_ includes tables of image metadata (``ObsCore``).

The "Butler Dataset type" entry on each image type's page is of the format ('datasetTypeName', {dimension1, **dimension2**, **dimension3**}, StorageClass), where dimensions in bold are *required* dimensions for retrieving datasets of this type.


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

