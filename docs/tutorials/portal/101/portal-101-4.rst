.. _portal-101-4:

#############################################
101.4. Use the query job monitor (get job ID)
#############################################

For the Portal Aspect of the Rubin Science Platform at data.lsst.cloud.

**Data Release:** DP1

**Last verified to run:** 2025-06-12

**Learning objective:** Use the Job Monitor to obtain the status and ID of, and delete, submitted query jobs.

**LSST data products:** ``Object`` table

**Credit:** Originally developed by the Rubin Community Science team. Please consider acknowledging them if this tutorial is used for the preparation of journal articles,
software releases, or other tutorials.

**Get Support:** Everyone is encouraged to ask questions or raise issues in the `Support Category <https://community.lsst.org/c/support/6>`_ of the Rubin Community Forum.
Rubin staff will respond to all questions posted there.

----

**1. Log into the Portal from the RSP.**
In a web browser go to the Rubin Science Platform (RSP) using the URL `data.lsst.cloud <https://data.lsst.cloud/>`_.

**2. Create a sample job.**
For the purpose of this tutorial, click Edit ADQL in the upper right hand corner and paste the following query into the box and hit Search.

.. code-block:: sql

  SELECT coord_dec,coord_ra,g_psfFlux
    FROM dp1.Object
    WHERE CONTAINS(POINT('ICRS', coord_ra, coord_dec),CIRCLE('ICRS', 53.13, -28.1, 0.0027))=1


**3.  Examine the job monitor.**
Click on the "Job Monitor" tab on the top.
The job monitor will have all jobs submitted by you (created within the retention period).
The jobs listed are in the chronological order (most recent first).
You can return to any of those jobs by clicking the line corresponding to the particular job.

.. figure:: images/portal-101-4-1.png
    :name: portal-101-4-1
    :alt: Job monitor screenshot.

    Figure 1:  Job monitor screenshot.

**5. Learn about individual jobs.**  In the column with a header "control" click on the green "wave" for a job of choice - this will bring you to that job,
and if completed - will reveal the results.
Click on the circle with a letter "i" - this will show your search converted to an ADQL query as well as the job ID.

Clicking on the red "garbage can" will delete the job.

An example of informaton for a recent job is in the figure below.

.. figure:: images/portal-101-4-2.png
    :width:  400
    :name: portal-101-4-2
    :alt: The screenshot illustrating information about a recent job, available from the job monitor.

    Figure 2:  The screenshot illustrating information about a recent job, available from the job monitor.

