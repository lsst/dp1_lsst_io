.. _catalogs-dia-object:

##########
DIA object
##########

``dia_object``: Derived properties for transient and variable objects.

DOI: |doi_dia_object|

Columns: 137

Rows: 1,089,818

Schema: `DiaObject table <https://sdm-schemas.lsst.io/dp1.html#DiaObject>`_

Access
======

The ``dia_object`` catalog is accessible via the TAP and butler services.

**Recommended access service:** TAP

TAP
---

Table name: ``DiaObject``

Butler
------

Dataset type: ``('dia_object', {skymap, tract}, ArrowAstropy)``


Description
===========

A "DIA object" is an astrophysical transient or variable object at a static sky coordinate.

The ``dia_object`` table is created by associating ``dia_sources`` within a 1 arcsecond radius.

The ``dia_object`` catalog contains derived per-filter variability parameters such as the minimum, mean,
maximum, standard deviation and skew in the difference-image fluxes, and the light curve’s slope, percentiles,
and ``StetsonJ`` parameter.


Processing
----------

The ``dia_object`` catalog is the result of :doc:`/processing/dia/index`.

Tutorials
---------

See the :ref:`200-level notebook <notebook-200>` or :ref:`200-level portal <portal-200>`
tutorials demonstrating how to access the ``dia_object`` table.