.. _catalogs-dia-forced-source:

#################
DIA forced source
#################

``dia_object_forced_source``: Forced measurements in visit and difference images, at the coordinates of all DIA objects.

DOI: |dia_object_forced_source|

Columns: 28

Rows: 196,911,566

Schema: `ForcedSourceOnDiaObject table <https://sdm-schemas.lsst.io/dp1.html#ForcedSourceOnDiaObject>`_

Access
======

The ``dia_object_forced_source`` catalog is accessible via the TAP and butler services.

**Recommended access service:** TAP

TAP
---

Table name: ``ForcedSourceOnDiaObject``

Butler
------

Dataset type: ``('dia_object_forced_source', {skymap, tract, patch}, ArrowAstropy)``


Description
===========

"Forced" photometry means a measurement is made at a fixed coordinate in an image,
regardless of whether an above-threshold region was detected there in that particular image.

The ``ForcedSourceOnDiaObject`` catalog contains forced PSF flux photometry on both the ``visit_image``
and ``difference_image`` at the coordinates of every object in the ``DiaObject`` table.

Processing
----------

The ``ForcedSourceOnDiaObject`` catalog is the result of :doc:`/processing/dia/index`.

Tutorials
---------

See the :ref:`200-level notebook <notebook-200>` or :ref:`200-level portal <portal-200>`
tutorials demonstrating how to access the ``ForcedSourceOnDiaObject`` table.
