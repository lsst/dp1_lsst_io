.. _catalogs-visit-table:

#####
Visit
#####

Observation metadata for the full focal plane (date, time, band, coordinates).

Schema: `Visit table <https://sdm-schemas.lsst.io/dp1.html#Visit>`_

Access
======

The visit catalog is accessible via the TAP and Butler services.

**Recommended access service:** TAP

TAP
---

* |Visit_doi|
* Table name: ``Visit``
* Columns: |Visit_columns|
* Rows: |Visit_rows|

Butler
------

* |visit_table_doi|
* Dataset type: ('visit_table', {**instrument**}, ArrowAstropy)
* Format: Parquet
* Number of Butler datasets: |visit_table_butler_count|

Description
===========

A "visit" is an observation in a single filter, obtained at a given time and sky coordinate.
It refers to an observation with the full focal plane, with the boresight (center) as the
reference for the observational metadata (e.g., airmass).

Tutorials
---------

See the :ref:`200-level notebook <notebook-200>` or :ref:`200-level portal <portal-200>`
tutorials demonstrating how to access the visit table.
