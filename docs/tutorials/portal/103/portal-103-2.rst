.. _portal-103-2:

#######################################
103.2. Query for catalog data with ADQL
#######################################

For the Portal Aspect of the Rubin Science Platform at data.lsst.cloud.

**Data Release:** DP1

**Last verified to run:** 2025-06-12

**Learning objective:** Prepare and execute an `Astronomy Data Query Language (ADQL) <https://www.ivoa.net/documents/latest/ADQL.html>`_ query in the Portal.

**LSST data products:** ``Object`` table

**Credit:** Originally developed by the Rubin Community Science team.
Please consider acknowledging them if this tutorial is used for the preparation of journal articles, software releases, or other tutorials.

**Get Support:** Everyone is encouraged to ask questions or raise issues in the `Support Category <https://community.lsst.org/c/support/6>`_ of the Rubin Community Forum. Rubin staff will respond to all questions posted there.

----

**1. Open Portal, from Calatogs tab, switch to ADQL interface.**
Select "Edit ADQL" at upper right in Figure 1 to go to the ADQL interface.
The ADQL Query box will be empty (Figure 1).

.. figure:: images/portal-103-2-1.png
    :name: portal-103-2-1
    :alt: The ADQL interface with no query entered.

    Figure 1: The ADQL interface with no query entered.

**2. Enter an ADQL statement in the box.**
For example, copy paste the statement below.
It is the same query as was used above in Option 1.

.. code-block:: SQL

  SELECT coord_dec,coord_ra,g_psfFlux,
       i_psfFlux,r_psfFlux,u_psfFlux,
       y_psfFlux,z_psfFlux
  FROM dp1.Object
  WHERE CONTAINS(POINT('ICRS', coord_ra, coord_dec),
      CIRCLE('ICRS', 53, -28, 0.05))=1
      AND (detect_isIsolated =1
           AND g_psfFlux >360
           AND i_psfFlux >360
           AND r_psfFlux >360
           AND u_psfFlux >360
           AND y_psfFlux >360
           AND z_psfFlux >360)

**3. Execute the ADQL query.**
Click the Search button at lower left.
The query will be executed and the results will appear in the Results tab.

.. figure:: images/portal-103-2-2.png
    :name: portal-103-2-2
    :alt: Default search results from a query.

    Figure 2: The default results view layout obtained by executing of the query described above. Interacting with query results is covered in a separate tutorial.

