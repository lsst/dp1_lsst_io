.. _portal-104-2:

################################################
104.2. Use the results coverage chart (HiPS map)
################################################

For the Portal Aspect of the Rubin Science Platform at data.lsst.cloud.

**Data Release:** DP1

**Last verified to run:** 6/17/2025.  HIPS map does not work as yet for DP1.

**Learning objective:** Learn how to iuse the coverage chart and HiPS map panel in the Portal results tab.
This query will retrieve a small sample of point-like objects (stars) brighter than 25th magnitude.

**LSST data products:** DP1 catalogs

**Credit:** Originally developed by the Rubin Community Science team.
Please consider acknowledging them if this tutorial is used for the preparation of journal articles, software releases, or other tutorials.

**Get Support:** Everyone is encouraged to ask questions or raise issues in the `Support Category <https://community.lsst.org/c/support/6>`_ of the Rubin Community Forum.
Rubin staff will respond to all questions posted there.

**Terminology:**

* `HiPS <https://aladin.cds.unistra.fr/hips/>`_: Hierarchical Progressive Surveys 
* `MOC <https://www.ivoa.net/documents/MOC/>`_: Multi-Order Coverage map 
* `ADQL <https://www.ivoa.net/documents/latest/ADQL.html>`_: Astronomy Query Data Language
* `HEALPix <https://healpix.sourceforge.io/>`_: Hierarchical Equal Area isoLatitude Pixelation of a sphere
* `2MASS <https://irsa.ipac.caltech.edu/Missions/2mass.html>`_: Two Micron All Sky Survey 
* `regions <https://ds9.si.edu/doc/ref/region.html>`_ file: a standard format for marking regions in an image
* `WCS <https://fits.gsfc.nasa.gov/fits_wcs.html>`_: World Coordinate System (the convention that defines the coordinates per pixel)
* PNG: Portable Network Graphic

----

**1. Log in to the Portal Aspect of the RSP, and execute a query.**
Go to the Portal's DP0.2 Catalogs tab, switch to the ADQL interface, and execute the query below.

.. code-block:: SQL

  SELECT coord_dec, coord_ra, detect_isIsolated, refExtendedness,
       u_cModelFlux, g_cModelFlux, r_cModelFlux,
       i_cModelFlux, z_cModelFlux, y_cModelFlux
  FROM dp1.Object
  WHERE CONTAINS(POINT('ICRS', coord_ra, coord_dec),
      CIRCLE('ICRS', 53.0, -28.0, 0.167)) =1
      AND (detect_isIsolated =1 AND refExtendedness =1
           AND u_cModelFlux >360 AND g_cModelFlux >360
           AND r_cModelFlux >360 AND i_cModelFlux >360
           AND z_cModelFlux >360 AND y_cModelFlux >360) 


**2. View the default coverage chart** (Figure 1).
The default view is a HEALPix grid showing the number of returned objects per grid region.
Small red squares mark individual objects outside the grid.
The background is a color HiPS map of the DP1 deepCoadd images.

.. figure:: images/portal-104-2-1.png
    :name: portal-104-2-1
    :alt: The default view of the coverage chart.

    Figure 1: The coverage chart panel in the Results tab, with default settings, for the query above. When the screenshot was taken the mouse was positioned on the green crosshair symbol, so the WCS Coordinates at lower left (item D) show the mouse position.


**3. Mouse-over for pop-up notes.**
In the coverage chart panel (Figure 1) use the mouse to hover over the menus and icons to see pop-up explanations of the functionality.

**4. Explore menus and icons.**
In the coverage chart panel (Figure 1) click on each of the drop-down menus and icons listed below, and see the pop-up windows of options and tools.

* A: **HiPS/MOC** options to change the underlying HiPS map or add a MOC layer.
* B: **WCS** options to choose the orientation and projection of the underlying HiPS map.
* C: **Zoom** in, out, or to fit the window. (It is also possible to use the mouse to zoom.)
* D: **WCS Coordinates** of the mouse position. Click the box-and-arrow icon at left to view coordinates in a separate window.
* E: **Toggle lock** to "on" to lock the WCS Coordinates to the location of the last mouse click, and "off" for continuous position.
* F: **Tools** menu with options to save, reset, or orient the display; add compass, ruler, points, etc.
* G: **Color table** menu to choose a different color map.
* H: **Recenter** by entering coordinates for the desired display center.
* I: **Spatial selection** (not currently active for HiPS maps).
* J: **Overlays** manipulation to change the options or color for the HEALPix and points overlay.
* K: **Image lock** and alignment (tools for when multiple images are displayed).
* L: **Expand panel** to have the coverage chart take the full browser window.

**5. Zoom in.**
Above C in Figure 1, click the "zoom in" icon (magnifying glass with a + inside) 5-6 times to zoom in,
until individual object markers are displayed instead of the HEALPix grid (Figure 2).

**6. Select a single object.**
Click on any individual marker, and notice that it's row will be highlighted orange in the table panel and its symbol will be orange in the active chart (Figure 2).

.. figure:: images/portal-104-2-2.png
    :name: portal-104-2-2
    :alt: The new view of the zoomed-in coverage chart.

    Figure 2: The coverage chart panel, zoomed in to show individual markers, with one object selected.

**7. Option: save a PNG of the coverage chart.**
Click on the tools icon (F in Figure 1) and select the disk icon next to "Save...".
Leave the default selection of PNG file and click "Save".
An image of the coverage chart will automatically download.
Note the option to export the overlays as a regions file.

**8. Reset the coverage chart.**
Click on the tools icon (F in Figure 1) and select the circular arrow icon next to "Save..." to restore to default options.
