.. _catalogs-mpcorb:

######
MPCORB
######

The orbit catalog produced by the `Minor Planets Center <https://minorplanetcenter.net/>`_ (MPC).

Columns: 10

Rows: 1,425,270

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

During Rubin Operations, Solar System Processing will link together the difference-image detections of moving objects and report discoveries to the MPC. The MPC will calculate the orbital parameters and these results will be passed back to Rubin. The returned result will be stored and made available to users as the ``MPCORB`` table.

Processing
----------

The MPCORB catalog is the result of :doc:`/processing/moving/index`.

Tutorials
---------

See the :ref:`200-level notebook <notebook-200>` or :ref:`200-level portal <portal-200>`
tutorials demonstrating how to access the MPCORB table.