.. _catalogs-mpcorb:

######
MPCORB
######

The orbit catalog produced by the `Minor Planet Center <https://minorplanetcenter.net/>`_ (MPC).

* Observatory Code: X05
* Columns: 10
* Rows: 1,425,270

Schema: `MPCORB table <https://sdm-schemas.lsst.io/dp1.html#MPCORB>`_

Access
======

The MPCORB catalog is accessible via the TAP service only.

TAP
---

Table name: ``MPCORB``

Butler
------

Not available.


Description
===========

The `Minor Planet Center <https://minorplanetcenter.net/>`_ (MPC) is the single worldwide location for receipt and distribution of positional measurements of small bodies. The MPC is responsible for the identification, designation, and orbit computation for all of these objects.

The ``MPCORB`` table contains the orbital parameters calculated by the MPC for all known solar system objects and the linked difference-image detections of moving objects submitted by Rubin. The DP1 ``MPCORB`` table includes a snapshot of all known solar system objects in the MPC database as of 24 March 2025, as well as the known object associations and discoveries submitted by Rubin for DP1.

Processing
----------

The MPCORB catalog is the result of :doc:`/processing/moving/index`.

Tutorials
---------

See the :ref:`200-level notebook <notebook-200>` or :ref:`200-level portal <portal-200>`
tutorials demonstrating how to access the MPCORB table.
