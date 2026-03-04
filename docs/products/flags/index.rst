.. _flags:

######################
Catalog flag columns
######################

Data Preview 1 (DP1) catalog tables contain extensive boolean flag columns that indicate quality issues, processing failures, or special conditions identified during Science Pipelines processing.
**These flags are provided for users to apply as quality filters based on their science requirements.**
DP1 data is delivered largely "as measured" with minimal a priori filtering, since the appropriate flag criteria depend on the specific science case.

This section provides guidance on understanding and using flag columns across all DP1 catalog tables.

.. toctree::
   :maxdepth: 1
   :titlesonly:

   flag_definitions
   flag_recommendations
   mask_planes

What is a flag column?
======================

A flag column is a boolean (True/False) column in a catalog table that indicates whether a specific condition, issue, or failure occurred during measurement or processing.

The key characteristics of flag columns are the following.

- Data type: Boolean (``bool`` or ``boolean`` in the schema).
- Naming convention: Most flag columns have ``flag`` in the column name (e.g., ``psfFlux_flag``, ``pixelFlags_saturated``). Some flags, such as those related to calibration (``calib_*``) and deblending (``deblend_*``), do not include "flag" in their name. The naming pattern is typically ``{band}_{measurement}_flag`` for the Object table and ``{measurement}_flag`` for Source-level tables.
- Interpretation: ``1`` (True) indicates the condition occurred or the measurement failed; ``0`` (False) indicates success or absence of the issue.
- Usage: Users typically filter out rows where critical flags are set to ``1`` to obtain clean, science-quality samples.
