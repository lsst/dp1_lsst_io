.. _catalogs-source:

######
Source
######

``source``: Detections in processed visit images.

DOI: |doi_source|

Columns: 156

Rows: 45,565,632

Schema: `Source table <https://sdm-schemas.lsst.io/dp1.html#Source>`_

Access
======

The ``source`` catalog is accessible via the TAP and butler services.

**Recommended access service:** TAP

TAP
---

Table name: ``Source``

Butler
------

Dataset type: ``('source', {band, instrument, day_obs, physical_filter, visit}, ArrowAstropy)``


Description
===========

A "source" is a signal-to-noise ratio > 5 detection in a visit image.

The ``source`` catalog contains measurements on a ``visit_image``
at the coordinates of every source detected in that image.

Measurements include PSF and Gaussian fluxes and sizes,
as well as processing pixel flags.

Processing
----------

The ``source`` catalog is the result of :doc:`/processing/detection/index`.

Tutorials
---------

See the :ref:`200-level notebook <notebook-200>` or :ref:`200-level portal <portal-200>`
tutorials demonstrating how to access the ``source`` table.