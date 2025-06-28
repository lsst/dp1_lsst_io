.. _catalogs:

########
Catalogs
########

Tables of measurements made on sources and objects detected in the processed images,
and tables of survey metadata for the observations.

The `schema browser <https://sdm-schemas.lsst.io/>`_ includes column descriptions for all tables.

All catalog data products are available via TAP, and most are also available with the butler.

The "Butler Dataset type" entry on each catalog's page is of the format ('datasetTypeName', {dimension1, **dimension2**, **dimension3**}, StorageClass), where dimensions in bold are *required* dimensions for retrieving datasets of this type.
See :ref:`products_butler_terminology` for more information.

.. note::

    When reading catalogs with the butler, it can be *much* more efficient to load just a few columns, by adding::

        parameters={"columns": list_of_columns}

    to a `Butler.get <lsst.daf.butler.Butler.get>` call (where ``list_of_columns`` is a Python `list` of `str` column names).

Object
======

Measurements on the deep coadd images at the locations of all detected objects.

.. toctree::
    :maxdepth: 1
    :titlesonly:
    :glob:

    object



Source and forced source
========================

Measurements on the individual images at the locations of all objects.

.. toctree::
    :maxdepth: 1
    :titlesonly:
    :glob:

    source
    forced_source


Difference image analysis
=========================

Measurements on the difference and visit images at the locations of all variable or moving objects.

.. toctree::
    :maxdepth: 1
    :titlesonly:
    :glob:

    dia_object
    dia_source
    dia_forced_source


Moving objects
==============

Derived properties for moving objects detected in images.

.. toctree::
    :maxdepth: 1
    :titlesonly:
    :glob:

    ss_object
    ss_source
    mpcorb



Observations
============

Observational metadata for visits and detectors.

.. toctree::
    :maxdepth: 1
    :titlesonly:
    :glob:

    visit_table
    visit_detector_table
