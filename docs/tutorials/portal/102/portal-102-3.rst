.. _portal-102-3:

###################################
102.3. Query for images with ObsTAP
###################################

For the Portal Aspect of the Rubin Science Platform at data.lsst.cloud.

**Data Release:** DP1

**Last verified to run:** 2025-06-28

**Learning objective:** Use the ObsTAP service to retrieve DP1 images.

**LSST data products:** ``visit_image``

**Credit:** Originally developed by the Rubin Community Science team.
Please consider acknowledging them if this tutorial is used for the preparation of journal articles, software releases, or other tutorials.

**Get Support:** Everyone is encouraged to ask questions or raise issues in the `Support Category <https://community.lsst.org/c/support/6>`_ of the Rubin Community Forum. Rubin staff will respond to all questions posted there.

----

**1. Log in to the RSP and enter the Portal Aspect.**
In a web browser go to `data.lsst.cloud <https://data.lsst.cloud/>`_, select the Portal Aspect, and log in.

**2. Select the DP1 Images tab.**
On the Portal landing page, click on the tab labeled "DP1 Images".

**3. Mouse-over for pop-up notes.**
In the "DP1 Images" tab (Figure 1) use the mouse to hover-over the components of the UI or click on the question marks and see pop-up explanations of the functionality.

.. figure:: images/portal-102-3-1.png
    :name: portal-102-3-1
    :alt: The graphical user interface for the Portal, offering drop-down menus to select catalogs and tables, entry fields for temporal and spatial constraints, and an interative view of the selected table schema.

    Figure 1: The Portal User Interface (UI) for querying images.


**4. Review the UI components.**
In the Portal UI (Figure 1) review the 4 main components labeled A through D, which are used together to query (search) and retrieve images.

* A: Select the type of image to be returned (e.g., processed visit image, deep coadd, difference image).
* B: Define the spatial constraints for the image query.
* C: Define the temporal constraints for the image query.
* D: The ``ivoa.ObsCore`` table holds all image metadata. It is recommended to use all pre-selected columns.

**5. Set the observation type and source.**
Check the box next to "Observation Type and Source".
Select calibration level 2 (for PVIs: processed visit images),
set the instrument name to LSSTComCam, the collection to LSST.DP1,
and the data product subtype to be "lsst.visit_image".

**6. Set the location.**
Check the box next to "Location".
For "Query Type" select "Observation boundary contains point" and
for coordinates, use the approximate center of the ECDFS field, RA, Dec = 53.0, -28.0 degrees.

**7. Set the timing.**
Check the box next to "Timing".
For "Time of Observation" select "Overlapping specified range".
Select "MJD values" and enter 60625 for the "Start Time" and 60630 for the "End Time".

**8. Execute the search.**
Click on the "Search" button at lower left.

**9. Review the results.**
The results interface enables interactive visualization of the 49 visit images which meet the search criteria.

.. figure:: images/portal-102-3-2.png
    :name: portal-102-3-2
    :alt: The image results interface.

    Figure 2: The image results interface.


Next steps: see the tutorials in the series on manipulating the image results interface.
