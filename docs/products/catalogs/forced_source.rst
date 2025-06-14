.. _catalogs-forced-source:

#############
Forced source
#############

Forced measurements in visit and difference images, at the coordinates of all objects.

DOI: |doi_forced_source|

Columns: 28

Rows: 268,796,943

Schema: `ForcedSource table <https://sdm-schemas.lsst.io/dp1.html#ForcedSource>`_

Access
======

The forced source catalog is accessible via the TAP and butler services.

**Recommended access service:** TAP

TAP
---

Table name: ``ForcedSource``

Butler
------

Dataset type: ``('object_forced_source', {skymap, tract, patch}, ArrowAstropy)``


Description
===========

"Forced" photometry means a measurement is made at a fixed coordinate in an image,
regardless of whether an above-threshold region was detected there in that particular image.

The forced source catalog contains forced PSF flux photometry on both the visit (i.e., "science" or "direct")
and difference images at the coordinates of every object in the object table.

Processing
----------

The forced source catalog is the result of :doc:`/processing/detection/index`.

Tutorials
---------

See the :ref:`200-level notebook <notebook-200>` or :ref:`200-level portal <portal-200>`
tutorials demonstrating how to access the forced source table.