.. _catalogs-object:

######
Object
######

Measurements of objects detected in deep coadd images.

Schema: `Object table <https://sdm-schemas.lsst.io/dp1.html#Object>`_

Access
======

The object catalog is accessible via the TAP and Butler services.

**Recommended access service:** TAP


.. note::

    The Object catalog has many columns, and it is recommended to retrieve only a subset of the columns :ref:`with TAP <products_adql_queries>` or the :ref:`with the Butler <products_butler_terminology>`.

TAP
---

* |Object_doi| [:download:`BibTeX </bib/tap-Object.bib>`]
* Table name: ``Object``
* Columns: |Object_columns|
* Rows: |Object_rows|

Butler
------

* |object_doi| [:download:`BibTeX </bib/butler-object.bib>`]
* :ref:`Dataset type <products_butler_terminology>`\ : ('object', {**skymap**, **tract**}, ArrowAstropy)
* Format: Parquet
* Number of Butler datasets: |object_butler_count|



Description
===========

An "object" is an astrophysical object at a static sky coordinate.

The object catalog contains forced measurements on the deep coadd images
at the coordinates of every object detected with signal-to-noise ratio >5
in a deep coadd image of any filter.

Measurements include PSF and extended fluxes, shapes, and sizes,
as well as processing pixel flags.
Photometry is calibrated, but not corrected for Milky Way dust extinction.

Objects are detected and deblended in each patch independently, including the "outer" patch regions that overlap.
They are then filtered down to just those whose reference-band centroid falls within the inner (non-overlapping) patch bounds when per-patch catalogs are aggregated.

Processing
----------

The object catalog is the result of :doc:`/processing/detection/index`.

Tutorials
---------

See the :ref:`200-level notebook <notebook-200>` or :ref:`200-level portal <portal-200>`
tutorials demonstrating how to access the object table.
