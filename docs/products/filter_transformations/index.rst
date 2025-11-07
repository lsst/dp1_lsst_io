.. _filter-transformations:

######################
Filter transformations
######################

Filter transformations to/from the LSSTComCam photometric system and other astronomical photometric systems.

.. (This line commented-out for now) |rtn-099_doi| [:download:`BibTeX </bib/filter-transformations.bib>`]


Access
======

The filter transformations are accessible via `RTN-099 <https://rtn-099.lsst.io/>`_.

Description
===========

The filter transformations were derived using both synthetic and empirical data and
are intended to support calibration and comparison across survey systems. The filter
transformation relations include both polynomial-fit equations and lookup-table-based
methods.  They are generally valid for stars with typical spectral energy distributions
(SEDs), and caution should be used when applying them to objects with strong emission
lines or atypical colors.

Transformation relations are currently available to/from LSSTComCam Data Preview 1 (DP1)
photometric system and the photometric systems of the Dark Energy Survey (DES), PanSTARRS,
SDSS, Gaia DR3, Euclid Q1, and Johnson-Cousins UBVRcIc.  There are also some transformation
equations based on synthetic photometry available to/from LSSTCam filters and DES and TESS.


.. The following lines commented out for now:
.. Tutorials
.. ---------
..
.. See the :ref:`300-level notebook <notebook-300>` tutorial demonstrating how to apply the filter transfomration relations.
