.. _catalogs-dia-source:

##########
DIA source
##########

Measurements for detected sources in difference images.

DOI: |doi_dia_source|

Columns: 87

Rows: 3,086,404

Schema: `DiaSource table <https://sdm-schemas.lsst.io/dp1.html#DiaSource>`_

Access
======

The DIA source catalog is accessible via the TAP and butler services.

**Recommended access service:** TAP

TAP
---

Table name: ``DiaSource``

Butler
------

Dataset type: ``('dia_source', {skymap, tract}, ArrowAstropy)``


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