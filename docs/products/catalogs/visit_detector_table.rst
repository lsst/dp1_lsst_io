.. _catalogs-visit-detector-table:

#########################
Visit detector (CcdVisit)
#########################

``visit_detector_table``: Observation metadata for individual detectors (CCDs; date, time, band, PSF, zeropoint).

DOI: |doi_visit_detector_table|

Columns: 51

Rows: 16071

Schema: `CcdVisit table <https://sdm-schemas.lsst.io/dp1.html#CcdVisit>`_

Access
======

The ``visit_detector_table`` catalog is accessible via the TAP and butler services.

**Recommended access service:** TAP

TAP
---

Table name: ``CcdVisit``

Butler
------

Dataset type: ``('visit_detector_table', {instrument}, ArrowAstropy)``


Description
===========

A "visit" is an observation in a single filter, obtained at a given time and sky coordinate.
A "detector" is one of the LSSTCam's 189 CCDs (charge-coupled device).
A "CcdVisit" refers to an observation with a single detector as the
reference for the observational metadata (e.g., airmass, seeing).

Tutorials
---------

See the :ref:`200-level notebook <notebook-200>` or :ref:`200-level portal <portal-200>`
tutorials demonstrating how to access the ``CcdVisit`` table.

