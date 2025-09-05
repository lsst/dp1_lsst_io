.. _bandpasses:

##########
Bandpasses
##########

LSSTComCam filter bandpasses.


|bandpasses_doi| [:download:`BibTeX </bib/butler-bandpasses.bib>`]


Access
======

The bandpasses are accessible via the Butler.


Butler
------

Examples of dataset types:

* ``('standard_passband', {band, instrument}, ArrowAstropy)``


Description
===========

There are six ``standard_passband`` datasets in the DP1 Butler repository -- one for each of the *ugrizy* bands.
These datasets tabulate the full-system transmission of the six LSSTComCam filters as a function of wavelength, which was used as a reference for the LSSTComCam DP1 photometry.
The ``standard_passband`` dataset is keyed by band and is in Astropy Table format.


.. figure:: figures/dp1_comcam_std_bandpasses.png
    :name: dp1-std-bandpasses
    :alt: Curves illustrating throughput as a function of wavelength for each of the six LSSTComCam filters.

    Figure 1: The LSSTComCam standard bandpasses, illustrating full system throughput as a function of wavelength.


Tutorials
---------

*Coming soon.*



