.. _portal-105-5:

################################
105.5. Use the image cutout tool
################################

For the Portal Aspect of the Rubin Science Platform at data.lsst.cloud.

**Data Release:** DP1

**Last verified to run:**  September 6, 2025

**Learning objective:** View image cutouts instead of full-frame images in Firefly.

**LSST data products:**

**Credit:** Originally developed by the Rubin Community Science team.
Please consider acknowledging them if this tutorial is used for the preparation of journal articles, software releases, or other tutorials.

**Get Support:** Everyone is encouraged to ask questions or raise issues in the `Support Category <https://community.lsst.org/c/support/6>`_ of the Rubin Community Forum.
Rubin staff will respond to all questions posted there.

----

**1. Log in to the Portal Aspect of the RSP.**
Go to `data.lsst.cloud <https://data.lsst.cloud>`_ , select the Portal Aspect, and click on the "DP1 Images" tab at the top.

**2. Enter the Observation Type and Source, and the coordinates of the image to be examined.**
The example below uses the Euclid Deep Field South (ECDS) containing the location of RA = 59.1, Dec = -48.73.
In the "Location" tab on the left, request "Observation boundary contains point" and enter those coordinatres ihe box just below.
Select Processed Visit Images (PVIs) by clicking on the "PVIs (2)" box in the "Observation Type and Source" tab on the left.

**3. Restrict the observation epochs.**
In the "Timing" tab, for the "Time of Observation" select "Overlaping specific range"..." and enter 60638 and 60641 as start time and End Time.
Click the "Search" button.



**4. Select a single-band observaton.**
In the table on the bottom, in the column with the header "lsst band" select "i" from the dropdown menu.

**4. Select the cutout tool.**
Above the image on the upper left, click on "scissors" which will select the cutout tool.
The pop-up window will allow for some choices:  the default is "Search Target Center".

**4. Change the coordinates of the cutout.**
Change the cutout center by clicking on the circle next to "Entered Position".
Click on the "Change Cutout Center" box and enter your desired coordinates (which need to be within the selected PVI).
The example here uses RA = 52.9936, Dec = -28.4118.
Click on "Update Cutout", which will show a single cutout corresponding to the first entry in the table below.

**Image**

**5. Display multiple cutouts.**


