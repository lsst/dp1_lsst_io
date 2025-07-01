.. _portal-104-7:

##############################################
104.7. Plot a light curve of a variable object
##############################################

For the Portal Aspect of the Rubin Science Platform at data.lsst.cloud.

**Data Release:** DP1

**Last verified to run:** 7/1/2025

**Learning objective:** Plot a light curve of an object with known coordinates.
The most reliable way is to first determine the ``diaObjectId`` of the object, and use that to perform forced photometry at the location of the object.

**LSST data products:** DP1 ``DiaObject`` and ``ForcedSourceOnDiaObject`` catalogs

**Credit:** Originally developed by the Rubin Community Science team.
Please consider acknowledging them if this tutorial is used for the preparation of journal articles, software releases, or other tutorials.

**Get Support:** Everyone is encouraged to ask questions or raise issues in the `Support Category <https://community.lsst.org/c/support/6>`_ of the Rubin Community Forum.
Rubin staff will respond to all questions posted there.

----

**1. Log in to the Portal and execute a query.**
Go to the Portal's DP1 Catalogs tab, switch to the ADQL interface (click on "Edit ADQL" tab), and enter the query below.
This step will return the ``diaObjectId`` for the object with coordinates in the query.

.. code-block:: SQL

        SELECT
        diaObjectId, ra, dec, nDiaSources
        FROM dp1.DiaObject
        WHERE CONTAINS(POINT('ICRS', ra, dec),
        CIRCLE('ICRS', 53.112562, -27.684829, 0.00028)) = 1

**2. Execute the ADQL query to retrieve the object ID.**
Click the Search button at lower left.
The query will be executed and the results will appear in the Results tab.
As a default, the "Coverage" panel (upper left) will display the "Deep Coadd" field image containing the coordinates entered in the search.
The "Active Chart" panel will display the default plot, dec as a function of RA.

.. figure:: ./portal-104-10-1.png
    :name: portal-104-10-1
    :alt: Default search results from a query.

    Figure 1: The default results view obtained by executing of the query described above.
The appropriate ``diaObjectId`` - 611256447031836758 - is the one with the lagrest number of significant detections.

**4.  Execute the ADQL query to retrieve the object's light curve.**

.. code-block:: SQL

        SELECT
        src.diaObjectId, src.coord_dec, src.coord_ra,
        src.psfFlux, src.psfFluxErr, src.band, visinfo.visit, visinfo.expMidptMJD
        FROM dp1.ForcedSourceOnDiaObject as src
        JOIN dp1.Visit as visinfo
        ON visinfo.visit = src.visit
        WHERE diaObjectId = 611256447031836758

**5. Select the quantities to be plotted.**
By default, the plot on the upper right hand side panel is of the dec as a function of RA.
To change this, click on the "gear" above the plot, and enter the parameters as in the screenshot below.

.. figure:: ./portal-104-10-2.png
    :name: portal-104-10-2
    :width: 500
    :alt: Parameters for the light curve plot

    Figure 2: The box with selection of parameters for the plot of the light curve of the selected target as a fnction of observation epoch (in MJD-60000).

**6. Plot the light curve of the object.**
Click "Apply" - this will result in the light curve measured in several filters.
On the table at the bottom, click on the box below the column header "band" and check only "i" for this filter.

.. figure:: ./portal-104-10-3.png
    :name: portal-104-10-3
    :alt: The i-band light curve plot

    Figure 3: The light curve of the selected target in the ``i`` band as a function of observation epoch (in MJD-60000).



