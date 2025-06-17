.. _portal-103-1:

#################################
103.1. Convert a UI query to ADQL
#################################

For the Portal Aspect of the Rubin Science Platform at data.lsst.cloud.

**Data Release:** DP1

**Last verified to run:** 2025-06-12

**Learning objective:** Convert a query with constraints set in the user interface (UI) into an `Astronomy Data Query Language (ADQL) <https://www.ivoa.net/documents/latest/ADQL.html>`_ statement.

**LSST data products:** ``Object`` table

**Credit:** Originally developed by the Rubin Community Science team.
Please consider acknowledging them if this tutorial is used for the preparation of journal articles, software releases, or other tutorials.

**Get Support:** Everyone is encouraged to ask questions or raise issues in the `Support Category <https://community.lsst.org/c/support/6>`_ of the Rubin Community Forum. Rubin staff will respond to all questions posted there.

----

**1. Create a Portal UI query.**
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

**2. Convert UI to ADQL query.**
Click on the button labeled "Populate and edit ADQL", located bottom-center in Figure 1.
The UI will switch to the ADQL interface and will populate the ADQL Query box with an ADQL statement that represents the exact same query, as shown in Figure 2.

.. figure:: images/portal-103-1-2.png
    :name: portal-103-1-2
    :alt: The Portal UI with a spatial query for bright objects converted from the UI to ADQL.

    Figure 2: The Portal's ADQL interface, automatically populated with the UI query from Figure 1, converted into an ADQL statement.

**3. Execute query.**
Click the Search button at lower left.
The query will be executed and the results will appear in the Results tab.

**Warning!**
If changes are made to the ADQL statement and then the interface is toggled back to the "Single Table (UI assisted)" interface using the button at lower right in Figure 2, those changes will not be reflected in the UI.
The conversion only works in one direction: from the UI to ADQL.

