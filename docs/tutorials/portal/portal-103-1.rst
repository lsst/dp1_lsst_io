.. _portal-103-1:

###################################
103.1. How to execute an ADQL query
###################################

For the Portal Aspect of the Rubin Science Platform at data.lsst.cloud.

**Data Release:** DP1

**Last verified to run:** 2025-06-11

**Learning objective:** This tutorial demonstrates how to prepare and execute an `Astronomy Data Query Language (ADQL) <https://www.ivoa.net/documents/latest/ADQL.html>`_ query in the Portal Aspect of the Rubin Science Platform.
This example will extract fluxes in multiple bands of all bright objects in a selected region of the sky.

**LSST data products:** dp1 catalogs and images

**Credit:** Originally developed by Greg Madejski and Melissa Graham. Please consider acknowledging them if this tutorial is used for the preparation of journal articles, software releases, or other tutorials.

**Get Support:** Everyone is encouraged to ask questions or raise issues in the `Support Category <https://community.lsst.org/c/support/6>`_ of the Rubin Community Forum. Rubin staff will respond to all questions posted there.

====================================
Option 1: Convert a UI query to ADQL
====================================
                                        
**1.1. Create a Portal UI query.**
Navigate to the "DP0.2 Catalogs" tab in the Portal UI.
In "Table Collection (Schema)" select "dp1_v29" and in the "Tables" select "dp1_v29.Object" table.
Set up a query in the user interface (UI), as shown in Figure 1.
Specifically, in the "Output Column Selection and Constraints" check boxes by the rows for ``coord_dec, coord_ra, detect_isIsolated, u_cModelFlux, g_cModelFlux, r_cModelFlux, i_cModelFlux, z_cModelFlux, y_cModelFlux``.
For all flux rows, enter a constraint ``>360``.
For the "detect_isIsolated" enter ``=1``.
Under "Enter Constraints" check "Spatial" and enter ``53.0, -28.0``.
For "Radius" enter 3 arc minutes.
Leave "Temporal" and Object ID Search" unchecked.
Restrict displaying the entries in the "Output Column Selection and Constraints" table to only those selected by you by clicking on the "funnel" icon on the upper left.

.. figure:: images/portal-103-1-1.png
    :name: portal-103-1-1
    :alt: The Portal UI with a spatial query for bright objects set up.

    Figure 1: The Portal UI set up for a simple cone search query for bright objects in the selected region.

**1.2. Convert UI to ADQL query.**
Click on the button labeled "Populate and edit ADQL", located bottom-center in Figure 1.
The UI will switch to the ADQL interface and will populate the ADQL Query box with an ADQL statement that represents the exact same query, as shown in Figure 2.

.. figure:: images/portal-103-1-2.png
    :name: portal-103-1-2
    :alt: The Portal UI with a spatial query for bright objects converted from the UI to ADQL.

    Figure 2: The Portal's ADQL interface, automatically populated with the UI query from Figure 1, converted into an ADQL statement.

**1.3. Execute query.**
Click the Search button at lower left.
The query will be executed and the results will appear in the Results tab (Figure 5).

**Warning!**
If changes are made to the ADQL statement and then the interface is toggled back to the "Single Table (UI assisted)" interface using the button at lower right in Figure 2, those changes will not be reflected in the UI.
The conversion only works in one direction: from the UI to ADQL.

=================================
Option 2: Enter an ADQL statement
=================================

**2.1. Go to the Portal's DP0.2 Catalogs tab.**
If needed, reload the webpage in the browser to clear any previously-entered constraints.
The interface should look like Figure 3.

.. figure:: images/portal-103-1-3.png
    :name: portal-103-1-3
    :alt: The Portal UI with no constraints set.

    Figure 3: The Portal UI with no query constraints entered.

**2.2. Switch to the ADQL interface.**
Select "Edit ADQL" at upper right in Figure 3 to go to the ADQL interface.
The ADQL Query box will be empty (Figure 4).
Scroll down to see example queries and visit the :doc:`/data-access-analysis-tools/adql-recipes` page for more.

.. figure:: images/portal-103-1-4.png
    :name: portal-103-1-4
    :alt: The ADQL interface with no query entered.

    Figure 4: The ADQL interface with no query entered.

**2.3. Enter an ADQL statement in the box.**
For example, copy paste the statement below.
It is the same query as was used above in Option 1.

.. code-block:: SQL

  SELECT coord_dec,coord_ra,detect_isIsolated,g_cModelFlux,i_cModelFlux,r_cModelFlux,u_cModelFlux,
       y_cModelFlux,z_cModelFlux 
  FROM dp1_v29.Object 
  WHERE CONTAINS(POINT('ICRS', coord_ra, coord_dec),CIRCLE('ICRS', 53, -28, 0.05))=1
      AND (detect_isIsolated =1
           AND g_cModelFlux >360
           AND i_cModelFlux >360
           AND r_cModelFlux >360
           AND u_cModelFlux >360
           AND y_cModelFlux >360
           AND z_cModelFlux >360)

**2.4. Execute the ADQL query.**
Click the Search button at lower left.
The query will be executed and the results will appear in the Results tab.

.. figure:: images/portal-103-1-5.png
    :name: portal-103-1-5
    :alt: Default search results from a query.

    Figure 5: The default results view layout obtained by executing of the query described above. Interacting with query results is covered in a separate tutorial.


Return to the list of DP0.2 :ref:`DP0-2-Tutorials-Portal`.
