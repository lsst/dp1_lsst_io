.. _catalogs-visit-detector-table:

#########################
Visit detector (CcdVisit)
#########################

Observation metadata for individual detectors (CCDs; date, time, band, PSF, zeropoint).

Schema: `CcdVisit table <https://sdm-schemas.lsst.io/dp1.html#CcdVisit>`_

Access
======

The visit detector catalog is accessible via the TAP and butler services.

**Recommended access service:** TAP

TAP
---

* |CcdVisit_doi|
* Table name: ``CcdVisit``
* Columns: |CcdVisit_columns|
* Rows: |CcdVisit_rows|

Butler
------

* |visit_detector_table_doi|
* Dataset type: ``('visit_detector_table', {instrument}, ArrowAstropy)``
* Format: Parquet
* Number of Butler datasets: |visit_detector_table_butler_count|

Description
===========

A "visit" is an observation in a single filter, obtained at a given time and sky coordinate.
A "detector" is one of the LSSTCam's 189 CCDs (charge-coupled device).
A "CcdVisit" refers to an observation with a single detector as the
reference for the observational metadata (e.g., airmass, seeing).

Tutorials
---------

See the :ref:`200-level notebook <notebook-200>` or :ref:`200-level portal <portal-200>`
tutorials demonstrating how to access the visit detector (``CcdVisit``) table.
