.. _catalogs-dia-object:

##########
DIA object
##########

Derived properties for transient and variable objects.

Schema: `DiaObject table <https://sdm-schemas.lsst.io/dp1.html#DiaObject>`_

Access
======

The DIA object catalog is accessible via the TAP and butler services.

**Recommended access service:** TAP

TAP
---

* |DiaObject_doi|
* Table name: ``DiaObject``
* Columns: |DiaObject_columns|
* Rows: |DiaObject_rows|

Butler
------

* |dia_object_doi|
* Dataset type: ``('dia_object', {skymap, tract}, ArrowAstropy)``
* Format: Parquet
* Number of Butler datasets: |dia_object_butler_count|

Description
===========

A "DIA object" is an astrophysical transient or variable object at a static sky coordinate.

The DIA object table is created by associating DIA sources within a 1 arcsecond radius.

The DIA object catalog contains derived per-filter variability parameters such as the minimum, mean,
maximum, standard deviation and skew in the difference-image fluxes, and the light curve’s slope, percentiles,
and StetsonJ parameter.


Processing
----------

The DIA object catalog is the result of :doc:`/processing/dia/index`.

Tutorials
---------

See the :ref:`200-level notebook <notebook-200>` or :ref:`200-level portal <portal-200>`
tutorials demonstrating how to access the DIA object table.
