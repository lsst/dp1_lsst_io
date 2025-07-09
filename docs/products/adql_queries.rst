.. _products_adql_queries:

####################################
Query best practices (TAP/ADQL tips)
####################################

ADQL is the `Astronomical Data Query Language <https://www.ivoa.net/documents/latest/ADQL.html>`_.
The language is used by the `IVOA <https://www.ivoa.net/>`_ to represent astronomy queries posted to Virtual Observatory (VO) services, such as the Rubin LSST Table Access Protocol (TAP) service.
ADQL is based on the 1992 ANSI-standard dialect of Structured Query Language (SQL92).

.. Important::
    If a query takes longer than expected, please :ref:`tutorials-getsupport` by asking for help in the `Rubin Community Forum <https://community.lsst.org/>`_.
    Rubin staff are happy to investigate and to help tweak queries for optimal execution.


Use asynchronous queries
========================

In the Notebook Aspect, execute TAP queries "asynchronously".

This means submit the query job separately from fetching the results, as demonstrated in Section 4 of Notebook tutorial :doc:`/tutorials/notebook/102/notebook-102-1`.

Where ``query`` is an ADQL statement, an asynchronous job can be run with the following code,
which will print the job phase and show the error traceback if the job did not complete.

.. code-block:: SQL

  job = service.submit_job(query)
  job.run()
  job.wait(phases=['COMPLETED', 'ERROR'])
  print('Job phase is', job.phase)
  if job.phase == 'ERROR':
      job.raise_if_error()


Then this code can be run separately to fetch the results, if the job completed.

.. code-block:: SQL

  assert job.phase == 'COMPLETED'
  results = job.fetch_result()

The RSP Portal automatically uses asynchronous mode for user queries.

Use spatial constraints
=======================

It is recommended to always include spatial constraints unless deliberately performing an all-sky analysis.
Even in that case we strongly recommend first prototyping the query with a spatial constraint included.

Qserv stores catalog data sharded by coordinate (RA, Dec).
This can be thought of as the database being divided up by spatial region (shard) and distributed across multiple servers.
ADQL query statements that include constraints by coordinate do not requre a whole-catalog search, minimize the number of shards that have to be searched through, and are typically faster (and can be much faster) than ADQL query statements that have no (or very wide) spatial constraints, or only include constraints for other columns.

Use ADQL's spherical geometry operators to perform either a Cone Search or a Polygon Search.
These are automatically translated into efficient spatial operations in Qserv.
**Do not** use direct column constraints (e.g., ``ra < value``) or ``WHERE`` ... ``BETWEEN`` statements to set boundaries on RA and Dec.


Retrieve forced photometry by identifier
========================================

It is recommended to query the ``ForcedSource`` (or ``ForcedSourceOnDiaObject``) table by ``objectId`` (or ``diaObjectId``), and **not by** coordinates.

The ``ForcedSource`` (or ``ForcedSourceOnDiaObject``) table should only be used to retrieve all forced photometry measurements in the direct and difference images (i.e., light curves) for one or more ``Object`` (or ``DiaObject``) record(s).

It is recommended to first query the ``Object`` (or ``DiaObject``) table with spatial constraints to obtain the ``objectId`` (or ``diaObjectId``) for the target(s) of interest, and then retrieve the forced photometry.

Alternatively, advanced TAP users may query the ``Object`` (or ``DiaObject``) table with spatial constraints and join on the ``ForcedSource`` (or ``ForcedSourceOnDiaObject``) tables to combine the two steps into one.


Specify the columns
===================

It is recommended to only retrieve the columns that are needed for a given analysis.

Most queries should specify columns by name and should **not use** ``SELECT * FROM``.
The ``Object`` table, for example, has over 1000 columns.


Use TOP instead of LIMIT
========================

For debugging and testing queries, the recommended way to restrict the number of rows returned is to use very small spatial regions, if possible, instead of TOP.
The TAP service first applies WHERE constraints, then ORDER BY, and then TOP.
If the query is not well constrained, i.e., if thousands or more objects meet the WHERE constraints, then they all must first be sorted before the top number are returned.

However, it can be useful to only retrieve a subset of the rows which meet the query constraints.
To do this, use ``SELECT TOP N`` where ``N`` is the number of rows.
(Note that other SQL dialects provide a ``LIMIT`` clause for this operation, but ``TOP`` is the ADQL word for it.)

For users with TAP experience, passing ``maxrec`` when the job is submitted will also work, but use of TOP is recommended.

Use caution if combining TOP and ORDER BY
-----------------------------------------

Combined use of TOP and ORDER BY in ADQL queries can be dangerous: it may take an unexpectedly long time because the database is trying to first sort, and then extract the top N elements.
It is best to only combine TOP and ORDER BY if the query's WHERE statements significantly cut down the number of objects that would need to be sorted.
