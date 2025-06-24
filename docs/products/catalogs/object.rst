.. _catalogs-object:

######
Object
######

Measurements of objects detected in deep coadd images.

Schema: `Object table <https://sdm-schemas.lsst.io/dp1.html#Object>`_

Access
======

The object catalog is accessible via the TAP and Butler services.

**Recommended access service:** TAP

TAP
---

* |Object_doi|
* Table name: ``Object``
* Columns: |Object_columns|
* Rows: |Object_rows|

Butler
------

* DOI: |object_doi|
* Dataset type: ('object', {**skymap**, **tract**}, ArrowAstropy)
* Format: Parquet
* Number of Butler datasets: |object_butler_count|

Description
===========

An "object" is an astrophysical object at a static sky coordinate.

The object catalog contains forced measurements on the deep coadd images
at the coordinates of every object detected with signal-to-noise ratio >5
in a deep coadd image of any filter.

Measurements include PSF and extended fluxes, shapes, and sizes,
as well as processing pixel flags.
Photometry is calibrated, but not corrected for Milky Way dust extinction.

Processing
----------

The object catalog is the result of :doc:`/processing/detection/index`.

Tutorials
---------

See the :ref:`200-level notebook <notebook-200>` or :ref:`200-level portal <portal-200>`
tutorials demonstrating how to access the object table.
