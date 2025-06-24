.. _catalogs-source:

######
Source
######

Measurements for sources detected in processed visit images.

Schema: `Source table <https://sdm-schemas.lsst.io/dp1.html#Source>`_

Access
======

The source catalog is accessible via the TAP and Butler services.

**Recommended access service:** TAP

TAP
---

* |Source_doi|
* Table name: ``Source``
* Columns: |Source_columns|
* Rows: |Source_rows|

Butler
------

* DOI: |source_doi|
* Dataset type: ('source', {band, **instrument**, day_obs, physical_filter, **visit**}, ArrowAstropy)
* Format: Parquet
* Number of Butler datasets: |source_butler_count|

Description
===========

A "source" is a signal-to-noise ratio > 5 detection in a visit image.

The source catalog contains measurements on a visit image
at the coordinates of every source detected in that image.

Measurements include PSF and Gaussian fluxes and sizes,
as well as processing pixel flags.

Processing
----------

The source catalog is the result of :doc:`/processing/detection/index`.

Tutorials
---------

See the :ref:`200-level notebook <notebook-200>` or :ref:`200-level portal <portal-200>`
tutorials demonstrating how to access the source table.
