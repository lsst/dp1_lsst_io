.. _catalogs-visit-table:

#####
Visit
#####

``visit_table``: Observation metadata for the full focal plane (date, time, band, coordinates).

DOI: |doi_visit_table|

Columns: 16

Rows: 1786

Schema: `Visit table <https://sdm-schemas.lsst.io/dp1.html#Visit>`_

Access
======

The ``visit_table`` catalog is accessible via the TAP and butler services.

**Recommended access service:** TAP

TAP
---

Table name: ``Visit``

Butler
------

Dataset type: ``('visit_table', {instrument}, ArrowAstropy)``


Description
===========

A "visit" is an observation in a single filter, obtained at a given time and sky coordinate.
It refers to an observation with the full focal plane, with the boresight (center) as the
reference for the observational metadata (e.g., airmass).

Tutorials
---------

See the :ref:`200-level notebook <notebook-200>` or :ref:`200-level portal <portal-200>`
tutorials demonstrating how to access the ``Visit`` table.
