.. _products_adql_queries:

####################################
Query best practices (TAP/ADQL tips)
####################################

ADQL is the `Astronomical Data Query Language <https://www.ivoa.net/documents/latest/ADQL.html>`_.
The language is used by the `IVOA <https://www.ivoa.net/>`_ to represent astronomy queries posted to Virtual Observatory (VO) services, such as the Rubin LSST Table Access Protocol (TAP) service.
ADQL is based on the Structured Query Language (SQL).

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


Use spatial constraints
=======================

Qserv stores catalog data sharded by coordinate (RA, Dec).
This can be thought of as the database being divided up by spatial region (shard) and distributed across multiple servers.
ADQL query statements that include constraints by coordinate do not requre a whole-catalog search, minimize the number of shards that have to be searched through, and are typically faster (and can be much faster) than ADQL query statements that have no (or very wide) spatial constraints, or only include constraints for other columns.

Use either an ADQL Cone Search or a Polygon Search.
Do **not** use of column constraints (e.g., ``ra < value``) or ``WHERE`` ... ``BETWEEN`` statements to set boundaries on RA and Dec.


