.. _catalogs-visit-detector-table:

#########################
Visit detector (CcdVisit)
#########################

Observation metadata for individual detectors (CCDs; date, time, band, PSF, zeropoint).

Schema: `CcdVisit table <https://sdm-schemas.lsst.io/dp1.html#CcdVisit>`_

Access
======

The visit detector catalog is accessible via the TAP and Butler services.

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
* :ref:`Dataset type <products_butler_terminology>`\ : ('visit_detector_table', {**instrument**}, ArrowAstropy)
* Format: Parquet
* Number of Butler datasets: |visit_detector_table_butler_count|

Description
===========

A "visit" is an observation in a single filter, obtained at a given time and sky coordinate.
A "detector" is one of the 9 CCDs (charge-coupled devices) that make up LSSTComCam.
A "CcdVisit" refers to an observation with a single detector as the
reference for the observational metadata (e.g., airmass, seeing).
This table includes image characterization information measured from the image, including things such as the PSF size, sky background, and image zeropoint.

Tutorials
---------

See the :ref:`200-level notebook <notebook-200>` or :ref:`200-level portal <portal-200>`
tutorials demonstrating how to access the visit detector (``CcdVisit``) table.
