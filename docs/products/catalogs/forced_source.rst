.. _catalogs-forced-source:

#############
Forced source
#############

Forced measurements in visit and difference images, at the coordinates of all objects.

Schema: `ForcedSource table <https://sdm-schemas.lsst.io/dp1.html#ForcedSource>`_

Access
======

The forced source catalog is accessible via the TAP and Butler services.

**Recommended access service:** TAP

TAP
---

* |ForcedSource_doi| [:download:`BibTeX </bib/tap-ForcedSource.bib>`]
* Table name: ``ForcedSource``
* Columns: |ForcedSource_columns|
* Rows: |ForcedSource_rows|

Butler
------

* |object_forced_source_doi| [:download:`BibTeX </bib/butler-object_forced_source.bib>`]
* :ref:`Dataset type <products_butler_terminology>`\ : ('object_forced_source', {**skymap**, **tract**, **patch**}, ArrowAstropy)
* Format: Parquet
* Number of Butler datasets: |object_forced_source_butler_count|

Forced sources are sharded by ``patch``, not just ``tract``, because in regions with many epochs the size of a full ``tract`` catalog becomes unwieldy.

Description
===========

"Forced" photometry means a measurement made at a fixed coordinate in an image,
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
