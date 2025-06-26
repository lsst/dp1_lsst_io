.. _catalogs-ss-source:

#########
SS source
#########

Instantaneous physical parameters for moving objects at the time of every observation.

Schema: `SSSource table <https://sdm-schemas.lsst.io/dp1.html#SSSource>`_

Access
======

The SS source catalog is accessible via the TAP and butler services.

**Recommended access service:** TAP

TAP
---

* |SSSource_doi|
* Table name: ``SSSource``
* Columns: |SSSource_columns|
* Rows: |SSSource_rows|

Butler
------

* |ss_source_doi|
* Dataset type: ``('ss_source', {}, ArrowAstropy)``
* Format: Parquet
* Number of Butler datasets: |ss_source_butler_count|

Description
===========

A "Solar System source" is ...

The SS source table is created by ...

*Details TBD.*

Processing
----------

The SS source catalog is the result of :doc:`/processing/moving/index`.

Tutorials
---------

See the :ref:`200-level notebook <notebook-200>` or :ref:`200-level portal <portal-200>`
tutorials demonstrating how to access the SS source table.
