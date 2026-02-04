.. _catalogs-coadd-patches:

#############
Coadd patches
#############

Coordinates and regions for the patches of the all-sky map.

Schema: `CoaddPatches table <https://sdm-schemas.lsst.io/dp1.html#CoaddPatches>`_

Access
======

The coadd patches catalog is accessible via the TAP service only.

TAP
---

* Table name: ``CoaddPatches``
* Columns: 5
* Rows: 652

Description
===========

The LSST all-sky map is divided into "tracts" (about the size of the LSSTCam field of view, 9.6 square degrees).
Each tract is subdivided into "patches": quadrilateral sub-regions that each cover approximately 128 square arcminutes (about the size of one LSSTCam detector).

The tracts are numbered with unique four-digit numbers, and the patches with non-unique three-digit numbers.
To uniquely identify a patch, both the tract and patch numbers are required.

Tutorials
---------

See the :ref:`200-level notebook <notebook-200>` tutorial demonstrating how to access the coadd patches table.
