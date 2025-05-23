.. _portal-101-1:

##############################################
101.1. How to navigate the UI (user interface)
##############################################

For the Portal Aspect of the Rubin Science Platform at data.lsst.cloud.

**Data Release:** DP1

**Last verified to run:** *yyyy-mm-dd*

**Learning objective:** This tutorial demonstrates how to navigate the Portal's user interface (UI), and provides a tour of the main components.

**LSST data products:** *List the catalogs and images used.*

**Credit:** Originally developed by Greg Madejski and Melissa Graham. Please consider acknowledging them if this tutorial is used for the preparation of journal articles, software releases, or other tutorials.

**Get Support:** Everyone is encouraged to ask questions or raise issues in the `Support Category <https://community.lsst.org/c/support/6>`_ of the Rubin Community Forum. Rubin staff will respond to all questions posted there.


.. _portal-101-1-S1:

1. Open the Portal Aspect on the RSP.
=====================================

**1.1. Log in to the Portal Aspect of the Rubin Science Platform.**
In a browser, go to the URL `data.lsst.cloud <https://data.lsst.cloud>`_ and select the Portal Aspect.
Follow the process to log in.

**1.2. Select the X tab in the Portal.**
*Explanation of the setup, reference to Figure 1.*

.. figure:: images/template_figure.png
    :name: template_figure_portal_101_1
    :alt: Alt-text goes here.

    Figure 1: Figure caption goes here.


**1.3. Execute the ADQL query.**
*Explanation of the query, reference to the code block below.*

.. code-block:: SQL

    SELECT g_H, r_H, i_H, z_H
    FROM dp03_catalogs_10yr.SSObject
    WHERE ssObjectId > 8660000000000000000



.. _portal-101-1-S2:

2. The second section
=====================

**2.1.** *And so on.*



.. _portal-101-1-ex:

X. Exercises for the learner
============================

**X.1. A clear, achievable task.**

**X.2. Another clear, achievable task.**
