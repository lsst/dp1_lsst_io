.. _catalogs-ss-object:

#########
SS object
#########

Derived parameters for moving (Solar System) objects.

Schema: `SSObject table <https://sdm-schemas.lsst.io/dp1.html#SSObject>`_

Access
======

The SS object catalog is accessible via the TAP and Butler services.

**Recommended access service:** TAP

TAP
---

* |SSObject_doi|
* Table name: ``SSObject``
* Columns: |SSObject_columns|
* Rows: |SSObject_rows|

Butler
------

* |ss_object_doi|
* :ref:`Dataset type <products_butler_terminology>`\ : ('ss_object', {}, ArrowAstropy)
* Format: Parquet
* Number of Butler datasets: |ss_object_butler_count|

Description
===========

A "Solar System object" is a moving object for which groupings of difference image detections (``DIASources``) have been linked together.

The SS object table contains the unique ``SSObjectId`` identifier, number of observations, and the date of the discovery submission (if a new discovery) for each solar system object detected with signal-to-noise ratio >5.

The DP1 version of the SS object table is very minimal, with only 3 columns.
Future versions of this table will include, for example, the best fit absolute magnitude and slope (G and H) parameters per band and associated statistics.

Processing
----------

The SS object catalog is the result of :doc:`/processing/moving/index`.

Tutorials
---------

See the :ref:`200-level notebook <notebook-200>` or :ref:`200-level portal <portal-200>`
tutorials demonstrating how to access the SS object table.
