.. _portal-104-1:

##############################################
104.1. Navigate the catalog results interface
##############################################

For the Portal Aspect of the Rubin Science Platform at data.lsst.cloud.

**Data Release:** DP1

**Last verified to run:**

**Learning objective:** Navigate the multi-panel interface for catalog data results.

**LSST data products:**

**Credit:** Originally developed by the Rubin Community Science team.
Please consider acknowledging them if this tutorial is used for the preparation of journal articles, software releases, or other tutorials.

**Get Support:** Everyone is encouraged to ask questions or raise issues in the `Support Category <https://community.lsst.org/c/support/6>`_ of the Rubin Community Forum.
Rubin staff will respond to all questions posted there.

----

**Introduction:**
This tutorial demonstrates how to navigate the results of a simple Portal query.
The example below selects fluxes of bright objects within a radius around a specific point on the sky.


**1. Log in to the Portal Aspect of the RSP.**
Log in to the Rubin Science Platform, and select the Portal aspect.
There, go to the Portal's DP0.2 Catalogs tab, and switch to the ADQL interface.

**2. Execute a query.**

.. code-block:: SQL

  SELECT coord_dec, coord_ra, detect_isIsolated, refExtendedness,
         u_cModelFlux, g_cModelFlux, r_cModelFlux,
         i_cModelFlux, z_cModelFlux, y_cModelFlux
  FROM dp1_v29.Object
  WHERE CONTAINS(POINT('ICRS', coord_ra, coord_dec),
        CIRCLE('ICRS', 53.0, -28.0, 0.167)) =1
        AND (detect_isIsolated =1 AND refExtendedness =1
             AND u_cModelFlux >360 AND g_cModelFlux >360
             AND r_cModelFlux >360 AND i_cModelFlux >360
             AND z_cModelFlux >360 AND y_cModelFlux >360)

**2. Review the Results tab layout.**
The default layout of the Results tab is shown in Figure 1.

.. figure:: /_static/portal-howto-results-1.png
    :name: portal-howto-results-1
    :alt: The Results tab after a query has been executed defaults to a screens split three ways: coverage map at upper left, default plot at uppr right, and the tabular data below.

    Figure 1: The Results tab after a query has been executed defaults to a screens split three ways: coverage map at upper left, default plot at uppr right, and the tabular data below.

**3. Coverage chart** (A in Figure 1).
The default view is a `HEALPix <https://healpix.sourceforge.io/>`_ grid showing the number of returned objects per grid region.
Small red squares mark individual objects outside the grid.
The background is a color `HiPS <https://aladin.cds.unistra.fr/hips/>`_ map of the DP0.2 deepCoadd images.

**4. Active chart** (B in Figure 1).
The default plot will be the first two columns of the returned data table.
In Figure 1, this is the Declination coordinate on the y-axis and the Right Ascension coordinate on the x-axis.
This plot will switch to a two-dimensional histogram if so many objects are returned that individual points cannot be distinguished.

**5. Table results** (C in Figure 1).
A scrollable table of the returned data, with the first row selected by default and shown in orange.
Note that the orange point in the active chart corresponds to the selected row.

**6. View layout options.**
At upper left, click on the menu icon (three horizontal lines; D in Figure 1) to open the sidebar menu.
Under "Results Layout", click on the icon of the default layout (A in Figure 2) to see all layout options.

.. figure:: /_static/portal-howto-results-2.png
    :name: portal-howto-results-2
    :alt: The sidebar menu with options for the results view layout.
    :width: 200

    Figure 2: The sidebar menu with options for the results view layout.

**7. Change the layout.**
In the sidebar menu in Figure 2, choose the two-panel view of coverage charts on the left and tables on the right.
Notice that the active chart (the plot) is still available as a tab at upper left.
Reopen the sidebar menu to try other layouts and return to the default three-panel view.

**8. Execute another query.**
Click on the tab "DP0.2 Catalogs" to return to the ADQL interface.
Change the query to return objects with ``i_cModelFlux`` :math:`>` 3600 nJy (22.5 mag).
Execute the query.

.. figure:: /_static/portal-howto-results-3.png
    :name: portal-howto-results-3
    :alt: The Results tab after a second query has been executed.

    Figure 3: Similar to Figure 2, but with the results of two queries.

**9. View multiple query results.**
The Results tab components are now populated with the data from the new query (Figure 3).
The coverage chart includes HEALPix maps for both queries, with the new one in magenta (A in Figure 3).
The active chart uses data from the new query results (B in Figure 3).
The table now has two tabs, one for each query (C in Figure 3).
Click on the tab for the first query and note that the coverage chart, table, and active chart change.

**10. Delete unwanted query results.**
In the table (C in Figure 3), click on the X in the tab for the first query results to delete them.

