.. _portal-102-3:

###################################
102.3. Query for images with ObsTAP
###################################

For the Portal Aspect of the Rubin Science Platform at data.lsst.cloud.

**Data Release:** DP1

**Last verified to run:** 2025-06-25

**Learning objective:** Use the ObsTAP service to retrieve DP1 images.

**LSST data products:** ``visit_image``

**Credit:** Originally developed by the Rubin Community Science team.
Please consider acknowledging them if this tutorial is used for the preparation of journal articles, software releases, or other tutorials.

**Get Support:** Everyone is encouraged to ask questions or raise issues in the `Support Category <https://community.lsst.org/c/support/6>`_ of the Rubin Community Forum.
Rubin staff will respond to all questions posted there.

----

**1. Select the image repository for your query.** Go to the Rubin Science Platform at `data.lsst.cloud <https://data.lsst.cloud/>`_,
select the Portal Aspect, and select the "General TAP" tab.
(If that tab does not appear after selecting the Portal Aspect, click on the "menu" (three horizontal lines) icon in the upper left,
and click on "General TAP" to add it as an additional tab.)

**2. Select “ivoa” from the "Table Collection (Schema)" menu.**
In the box for selecting tables, "dp1.ObsCore" will appear.
Note: leave all columns selected in the "Output Column Selection and Constraints table".

**3.  Select the Observation Type and Source.**
Check the box for the "Observation Type and Source".
In the drop-down menu, for "Calibration Level" select "PVIs (2)".
For the "Data Product Type" select "image", and leave the  "Instrument Name" and "Collection" in the default state.

.. figure:: images/portal-102-3-1.png
    :name: portal-102-3-1
    :alt: Screenshot of calibration level window.

Figure 1:  The screenshot of calibration window.

**4. Select the location contained in the images to be retrieved.**
Select the "Location" box and in the "Query Type" select "Observation boundary contains point."
In the "Coordinates or Object Name" enter the desired coordinates.
This example uses 53.13, -28.10 for RA and Dec.

.. figure:: images/portal-102-3-2.png
    :name: portal-102-3-2
    :alt: Screenshot of Coordinates or Object Name window.

Figure 2:  The screenshot of Coordinates or Object Name window.


**5.  Retrieve the images.**
Click on the "Search" button.
This will result in extracting 50 images meeting the selected criteria.
By default, the displayed image on the upper left is the first one in the table of images on the bottom of the screen.
The plot on the upper right will display the pointing directions of the telescope for individual images.

.. figure:: images/portal-102-3-3.png
    :name: portal-102-3-3
    :alt: Screenshot of the window resulting from the execution of the search above.

Figure 3:  The screenshot of the window resulting from the execution of the search.

**6.  Examine the images.**
Click on any line in the table - this will result in displaying the image corresponding to the table entry.
Click on any point on the scatter plot on the right - this also will display the corresponding image.

For more information, see image results interface tutorial.

