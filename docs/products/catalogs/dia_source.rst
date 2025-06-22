.. _catalogs-dia-source:

##########
DIA source
##########

Measurements for detected sources in difference images.

Schema: `DiaSource table <https://sdm-schemas.lsst.io/dp1.html#DiaSource>`_

Access
======

The DIA source catalog is accessible via the TAP and butler services.

**Recommended access service:** TAP

TAP
---

* DOI: |DiaSource_doi|
* Table name: ``DiaSource``
* Columns: |DiaSource_columns|
* Rows: |DiaSource_rows|

Butler
------

* DOI: |source_doi|
* Dataset type: ``('dia_source', {skymap, tract}, ArrowAstropy)``
* Format: Parquet
* Number of Butler datasets: |source_butler_count|

Description
===========

A "DIA source" is a signal-to-noise ratio > 5 detection in a difference image.

The DIA source catalog contains measurements on a difference image
at the coordinates of every source detected in that difference image.
These measurements include PSF-fit and forced PSF fluxes, and aperture and
trailed-source fluxes.
Forced PSF fluxes on the corresponding visit (i.e., "direct" or "science") image
at the coordinates of the DIA source are also included.


Processing
----------

The DIA source catalog is the result of :doc:`/processing/dia/index`.

Tutorials
---------

See the :ref:`200-level notebook <notebook-200>` or :ref:`200-level portal <portal-200>`
tutorials demonstrating how to access the DIA source table.
