.. _portal-103-5:

#################################
103.5. Query for images with ADQL
#################################

For the Portal Aspect of the Rubin Science Platform at data.lsst.cloud.

**Data Release:** DP1

**Last verified to run:** 2025-06-28

**Learning objective:** Query for image data with `Astronomy Data Query Language (ADQL) <https://www.ivoa.net/documents/latest/ADQL.html>`_.

**LSST data products:** ``visit_image``

**Credit:** Originally developed by the Rubin Community Science team.
Please consider acknowledging them if this tutorial is used for the preparation of journal articles, software releases, or other tutorials.

**Get Support:** Everyone is encouraged to ask questions or raise issues in the `Support Category <https://community.lsst.org/c/support/6>`_ of the Rubin Community Forum.
Rubin staff will respond to all questions posted there.

**An introduction to ADQL** is provided in another tutorial in this series.

----

**1. Go to the DP1 Images ADQL interface.**
The button to switch from the user interface to the ADQL interface is in the upper right corner: "Edit ADQL".

**2. Create an ADQL query for images.**
It is recommended to always select all of the columns as in the query statement below.
This query requests images with calibration level 2 (processed visit images) that overlap the coordinates RA, Dec = 53.13, -28.1 degrees.

.. code:: sql

  SELECT dataproduct_type, dataproduct_subtype, calib_level, lsst_band,
         em_min, em_max, lsst_tract, lsst_patch, lsst_filter,
         lsst_visit, lsst_detector, t_exptime, t_min, t_max,
         s_ra, s_dec, s_fov, obs_id, obs_collection, o_ucd,
         facility_name, instrument_name, s_region,
         access_url, access_format
  FROM ivoa.ObsCore
  WHERE calib_level = 2 AND dataproduct_type = 'image'
        AND CONTAINS(POINT('ICRS', 53.13, -28.1), s_region)=1


**3. Execute the query.**
Copy-paste the query above into the ADQL query box, and click "Search".

**4. View the results.**
The 787 individual visit images that meet the ADQL query constraints will be available in the table, with the selected row displayed at upper right, as in Figure 1.

.. figure:: images/portal-103-5-1.png
    :name: portal-103-5-1
    :alt: The screenshot of the image, the scatter plot, and the table resulting from executing the ADQL query above.

    Figure 1: The screenshot of the image, the scatter plot, and the table that result from executing the ADQL query.

