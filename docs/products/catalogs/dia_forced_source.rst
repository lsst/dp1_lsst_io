.. _catalogs-dia-forced-source:

#################
DIA forced source
#################

Forced measurements in visit and difference images, at the coordinates of all DIA objects.

Schema: `ForcedSourceOnDiaObject table <https://sdm-schemas.lsst.io/dp1.html#ForcedSourceOnDiaObject>`_

Access
======

The DIA forced source catalog is accessible via the TAP and Butler services.

**Recommended access service:** TAP

TAP
---

* |ForcedSourceOnDiaObject_doi| [:download:`BibTeX </bib/tap-ForcedSourceOnDiaObject.bib>`]
* Table name: ``ForcedSourceOnDiaObject``
* Columns: |ForcedSourceOnDiaObject_columns|
* Rows: |ForcedSourceOnDiaObject_rows|

Butler
------

* |dia_object_forced_source_doi| [:download:`BibTeX </bib/butler-dia_object_forced_source.bib>`]
* :ref:`Dataset type <products_butler_terminology>`\ : ('dia_object_forced_source', {**skymap**, **tract**, **patch**}, ArrowAstropy)
* Format: Parquet
* Number of Butler datasets: |dia_object_forced_source_butler_count|

Forced sources are sharded by ``patch``, not just ``tract``, because in regions with many epochs the size of a full ``tract`` catalog becomes unwieldy.

Description
===========

"Forced" photometry means a measurement made at a fixed coordinate in an image,
regardless of whether an above-threshold region was detected there in that particular image.

The DIA forced source table contains forced PSF flux photometry on both the visit (i.e., "direct" or "science")
and difference images at the coordinates of every object in the DIA object table.

Processing
----------

The DIA forced source catalog is the result of :doc:`/processing/dia/index`.

Tutorials
---------

See the :ref:`200-level notebook <notebook-200>` or :ref:`200-level portal <portal-200>`
tutorials demonstrating how to access the DIA forced source table.
