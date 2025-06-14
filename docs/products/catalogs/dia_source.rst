.. _catalogs-dia-source:

##########
DIA source
##########

``dia_source``: Detections in difference images.

DOI: |doi_dia_source|

Columns: 87

Rows: 3,086,404

Schema: `DiaSource table <https://sdm-schemas.lsst.io/dp1.html#DiaSource>`_

Access
======

The ``dia_source`` catalog is accessible via the TAP and butler services.

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

The ``dia_source`` catalog contains measurements on a ``difference_image``
at the coordinates of every source detected in that difference image.
These measurements include PSF-fit and forced PSF fluxes, and aperture and
trailed-source fluxes.
Forced PSF fluxes on the corresponding ``visit_image`` ("science" image)
at the coordinates of the DIA source are also included.


Processing
----------

The ``dia_source`` catalog is the result of :doc:`/processing/dia/index`.

Tutorials
---------

See the :ref:`200-level notebook <notebook-200>` or :ref:`200-level portal <portal-200>`
tutorials demonstrating how to access the ``dia_source`` table.