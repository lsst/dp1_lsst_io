.. _products_butler_terminology:

##################
Butler terminology
##################

As the system used to organize Rubin datasets both for users and behind the scenes, the terminology used to describe a data product within the data butler is often used more broadly in tutorials and documentation, even in contexts where data access does not use the butler directly.

See :ref:`daf_butler_organizing_datasets` in the `~lsst.daf.butler.Butler` documentation for a more complete description of butler concepts.

Datasets
========

A *dataset* in the butler is a singular entity, usually corresponding to a single file and a single in-memory Python object.
The ``visit_image`` for a single ``{visit, detector}`` and an ``object`` table for a single ``{tract, patch}`` are each a dataset.

Dataset types
=============

A category of datasets is a *dataset type*.
Dataset types have a name (e.g. "visit image", "object") that uniquely identifies them, a *storage class*, and a set of *dimensions*.

Storage classes
===============

The storage class connects the dataset type with both the Python type used to represent datasets in memory and an abstract specification of how it is stored (not necessarily a file format, which the butler generally tries to hide from users).
Storage classes can sometimes be converted on read or write.
In particular, butler dataset types stored as Parquet files are almost always defined with ``ArrowAstropy`` as their storage class, which reads in as an `astropy.table.Table` instance, but passing ``storageClass="DataFrame"`` to `Butler.get <lsst.daf.butler.Butler.get>` will make it return a `pandas.DataFrame` instead.

Dimensions and data IDs
=======================

The *dimensions* of a dataset type are the keys of the mapping-like *data IDs* (also known as *data coordinates*) that identify datasets of that type.
For example, the ``visit_image`` dataset type has dimensions ``{instrument, visit, detector}``, because its datasets have data IDs like ``{instrument: "LSSTComCam", visit: 2024110800246, detector=2}``.
In addition to being used as keys in data IDs, dimensions are associated with metadata (*dimension records*) in the butler database, and can have other dimensions as *required* and *implied* dependencies that often allow data IDs to be written more concisely.
For example, the ``visit`` dimension *requires* the ``instrument`` dimension, which means that a visit ID like ``2024110800246`` must be accompanied by an instrument name like ``"LSSTComCam"`` to be fully-qualified.\ [#data_id_defaults]_
On the other hand, the ``visit`` dimension *implies* the ``physical_filter`` and ``day_obs`` dimensions, which means you never have to pass values for these dimensions when specifying a visit ID; the butler can just look them up from the visit ID.

Collections
===========

Different versions of the same dataset (e.g. from different processing runs) are organized into different *collections*.
Since DP1 has a single version of each dataset, the top-level ``LSSTComCam/DP1`` collection is the starting point for all DP1 work.
This collection is a special collection type (`~lsst.daf.butler.CollectionType.CHAINED`) that is actually just a list of other collections to search in a particular order.

.. [#data_id_defaults] In the ``LSSTComCam/DP1`` butler collection, there is only one ``instrument`` (``LSSTComCam``) and one ``skymap`` (``lsst_cells_v1``) in use, so `~lsst.daf.butler.Butler` instances constructed with that collection can infer the ``instrument`` and ``skymap`` names, making it *usually* unnecessary to include them in data IDs.
