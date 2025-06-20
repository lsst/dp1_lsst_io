.. _portal-105-1:

###########################################
105.1. Navigate the image results interface
###########################################

For the Portal Aspect of the Rubin Science Platform at data.lsst.cloud.

**Data Release:** DP1

**Last verified to run:** 6/20/2025

**Learning objective:** Navigate the multi-panel interface for image data results.

**LSST data products:** DP1 images (co-adds)

**Credit:** Originally developed by the Rubin Community Science team.
Please consider acknowledging them if this tutorial is used for the preparation of journal articles, software releases, or other tutorials.

**Get Support:** Everyone is encouraged to ask questions or raise issues in the `Support Category <https://community.lsst.org/c/support/6>`_ of the Rubin Community Forum.
Rubin staff will respond to all questions posted there.

----

**1. Log in to the Portal Aspect of the RSP.**
Log in to the Rubin Science Platform, and select the Portal aspect.
There, go to the Portal's "General TAP" tab, and switch to the UI interface.
If the "General TAP" tab is not available click on the "hamburger" icon on the upper left, and click on the "General TAP" entry.
This will result in an additional tab on top.

**2. Select the appropriate table and enter the image coordinates.**
Select "dp1" for the "Table Collection (Schema)" on the left, and "dp1.ObsCore" on the right.
For Observation Type and Source, select "PVIs (2)".
For "Location" select "Observation boundary contains point" and enter ``53.0, -28.0`` in the associated box.
Unselect "Timing" and "Object ID Search" boxes.

**3. Review the Results tab layout.**
The default layout of the Results tab is shown in Figure 1.

.. figure:: images/portal-105-1-1.png
    :name: portal-105-1-1
    :alt: The Results tab after a query has been executed

    Figure 1: The results of the query above, which defaults to a screens split three ways:
* an image associated with the first entry in the tabular data below at upper left
* default plot at upper right (corresponding to the first two columns , and the tabular data below.
