.. _portal-105-4:

#####################################################
105.4. Extract pixel values from images (Coming Soon)
#####################################################

For the Portal Aspect of the Rubin Science Platform at data.lsst.cloud.

**Data Release:** DP1

**Last verified to run:**

**Learning objective:** Extract pixel values, e.g., line profile, from images displayed in Firefly.

**LSST data products:**

**Credit:** Originally developed by the Rubin Community Science Team.
Please consider acknowledging them if this tutorial is used for the preparation of journal articles, software releases, or other tutorials.

**Get Support:** Everyone is encouraged to ask questions or raise issues in the `Support Category <https://community.lsst.org/c/support/6>`_ of the Rubin Community Forum.
Rubin staff will respond to all questions posted there.

----

**1. Log in to the Portal Aspect of the RSP.**

*Tutorial coming soon!*

.. This is the beginning of a new tutorial focussing on learning to study variability using features of the Rubin Portal

.. Review the README on instructions to contribute.
.. Review the style guide to keep a consistent approach to the documentation.
.. Static objects, such as figures, should be stored in the _static directory. Review the _static/README on instructions to contribute.
.. Do not remove the comments that describe each section. They are included to provide guidance to contributors.
.. Do not remove other content provided in the templates, such as a section. Instead, comment out the content and include comments to explain the situation. For example:
	- If a section within the template is not needed, comment out the section title and label reference. Do not delete the expected section title, reference or related comments provided from the template.
    - If a file cannot include a title (surrounded by ampersands (#)), comment out the title from the template and include a comment explaining why this is implemented (in addition to applying the ``title`` directive).

.. This is the label that can be used for cross referencing this file.
.. Recommended title label format is "Directory Name"-"Title Name" -- Spaces should be replaced by hyphens.
.. _Tutorials-Examples-DP0-2-Portal-howto-image-extract-pixelvalues:
.. Each section should include a label for cross referencing to a given area.
.. Recommended format for all labels is "Title Name"-"Section Name" -- Spaces should be replaced by hyphens.
.. To reference a label that isn't associated with an reST object such as a title or figure, you must include the link and explicit title using the syntax :ref:`link text <label-name>`.
.. A warning will alert you of identical labels during the linkcheck process.

**Introduction:**
This tutorial demonstrates how to extract pixel values from active images retreived from a Portal image query.

**1. Execute an image query.**
Go to `data.lsst.cloud <https://data.lsst.cloud>`_ , select the Portal Aspect, and
click on the "DP0.2 Images" tab at the top. Enter your desired constraints for the image query,
and click "Search" to execute it.       

**2. Select the Line Tool.**
To extract pixel values along a line (1D brightness profile),
click the "Tools" icon, then select the "Line" icon under the "Extract" section.
In the instruction window, choose an aperture for combining values.

**3. Draw and view profile.**
Click the starting point on the image, drag to the endpoint, and release. 
A pop-up window will display the 1D brightness profile, where you can adjust the aperture if needed.

**4. Save or download.**
Click "Pin Chart/Table" to add the chart and table to the result,
or download them directly. Repeat the process to extract another profile.

.. figure:: /_static/portal_tut06_step03a.png
    :width: 500
    :name: portal_howto_image_extract_pixelvalues-1
    :alt: A screenshot displaying a line drawn across a source, accompanied by a pop-up window showing the source's 1D brightness profile along that line. 

    Figure 1: A line drawn across a source, with a pop-up window displaying the 1D brightness profile of the source.

                                        
**5. Select the Points Tool.**
To extract pixel information for selected points,
click the "Points" icon under the "Extract" section. 
In the instruction window, choose an aperture to combine the values. 

**6. Select points.** 
Click multiple points on the image to extract their pixel values at once. 

**7. Save or download.**
Click "Pin Chart/Table" to save the results temporariliy, or use "Download as Table" and/or
"Download Chart" to save them locally. Results can also be saved as a DS9 region file. 

.. figure:: /_static/portal_tut06_step03b.png
    :name: portal_howto_image_extract_pixelvalues-2
    :alt: A screenshot displaying six selected points on the image (left panel), in the active chart (right panel), and in the pinned table (bottom panel), with a pop-up window offering options for file format and naming for saving.

    Figure 2: Six selected points on the image (left panel), in the active chart (right panel), and in the pinned table (bottom panel), with a pop-up window offering options for file format and naming for saving.
