.. _catalogs-object:

######
Object
######

``object``: Forced measurements in deep coadd images.

DOI: |doi_object|

Columns: 1272

Rows: 2,299,757

Schema: `Object table <https://sdm-schemas.lsst.io/dp1.html#Object>`_

Access
======

The ``object`` catalog is accessible via the TAP and butler services.

**Recommended access service:** TAP

TAP
---

Table name: ``Object``

Butler
------

Dataset type: ``('object', {skymap, tract}, ArrowAstropy)``


Description
===========

An "object" is an astrophysical object at a static sky coordinate.

The ``object`` catalog contains forced measurements on the ``deep_coadd`` images
at the coordinates of every object detected in the ``deep_coadd``
and every source detected in the individual ``visit_images``
(except sources associated with moving objects).

Measurements include PSF and extended fluxes, shapes, and sizes,
as well as processing pixel flags.
Photometry is calibrated, but not corrected for Milky Way dust extinction.

Processing
----------

The ``object`` catalog is the result of :doc:`/processing/detection/index`.

Tutorials
---------

See the :ref:`200-level notebook <notebook-200>` or :ref:`200-level portal <portal-200>`
tutorials demonstrating how to access the ``object`` table.