################################
03. How to execute an ADQL query
################################

.. This section should provide a brief, top-level description of the page.

**RSP Aspect:** Portal

**Contact authors:** Greg Madejski and Melissa Graham

**Last verified to run:** 2025-02-03

**Targeted learning level:** beginner 

**Introduction:**
This tutorial demonstrates how to execute a simple Portal query for table data using the `Astronomy Data Query Language (ADQL) <https://www.ivoa.net/documents/latest/ADQL.html>`_.

                                        
====================================
Option 1: Convert a UI query to ADQL
====================================
                                        
**1.1. Create a Portal UI query.**
Navigate to the "DP0.2 Catalogs" tab in the Portal UI and set up a query in the user interface (UI), as shown in Figure 1.

.. figure:: /_static/portal-howto-adql-1.png
    :name: portal-howto-adql-1
    :alt: The Portal UI with a spatial query for bright, extended objects set up.

    Figure 1: The Portal UI set up for a simple cone search query for bright extended objects near the center of the DP0.2 region.



**1.2. Convert UI to ADQL query.**
Click on the button labeled "Populate and edit ADQL", located bottom-center in Figure 1.
The UI will switch to the ADQL interface and will populate the ADQL Query box with an ADQL statement that represents the exact same query, as shown in Figure 2.

.. figure:: /_static/portal-howto-adql-2.png
    :name: portal-howto-adql-2
    :alt: The Portal UI with a spatial query for bright, extended objects converted from the UI to ADQL.

    Figure 2: The Portal's ADQL interface, automatically populated with the UI query from Figure 1, converted into an ADQL statement.


**1.3. Execute query.**
Click the Search button at lower left.
The query will be executed and the results will appear in the Results tab (Figure 5).

**Warning!**
If changes are made to the ADQL statement and then the interface is toggled back to the "Single Table (UI assisted)" interface using the button at lower right in Figure 2,
those changes will not be reflected in the UI.
The conversion only works in one direction: from the UI to ADQL.


=================================
Option 2: Enter an ADQL statement
=================================

**2.1. Go to the Portal's DP0.2 Catalogs tab.**
If needed, reload the webpage in the browser to clear any previously-entered constraints.
The interface should look like Figure 3.

.. figure:: /_static/portal-howto-adql-3.png
    :name: portal-howto-adql-3
    :alt: The Portal UI with no constraints set.

    Figure 3: The Portal UI with no query constraints entered.


**2.2. Switch to the ADQL interface.** 
Select "Edit ADQL" at upper right in Figure 3 to go to the ADQL interface.
The ADQL Query box will be empty (Figure 4).
Scroll down to see example queries and visit the :doc:`/data-access-analysis-tools/adql-recipes` page for more.

.. figure:: /_static/portal-howto-adql-4.png
    :name: portal-howto-adql-4
    :alt: The ADQL interface with no query entered.

    Figure 4: The ADQL interface with no query entered.


**2.3. Enter an ADQL statement in the box.**
For example, copy paste the statement below.
It is the same query as was used above in Option 1.

.. code-block:: SQL

  SELECT coord_dec, coord_ra, detect_isPrimary, refExtendedness, 
         u_cModelFlux, g_cModelFlux, r_cModelFlux, 
         i_cModelFlux, z_cModelFlux, y_cModelFlux 
  FROM dp02_dc2_catalogs.Object 
  WHERE CONTAINS(POINT('ICRS', coord_ra, coord_dec), 
        CIRCLE('ICRS', 62, -37, 0.167)) =1 
        AND (detect_isPrimary =1 AND refExtendedness =1 
             AND u_cModelFlux >360 AND g_cModelFlux >360 
             AND r_cModelFlux >360 AND i_cModelFlux >360 
             AND z_cModelFlux >360 AND y_cModelFlux >360)


**2.4. Execute the ADQL query.**
Click the Search button at lower left.
The query will be executed and the results will appear in the Results tab.

.. figure:: /_static/portal-howto-uiquery-5.png
    :name: portal-howto-uiquery-5
    :alt: Default search results from a query.

    Figure 5: The default results view layout for the query described above. Interacting with query results is covered in a separate tutorial.


Return to the list of DP0.2 :ref:`DP0-2-Tutorials-Portal`.
