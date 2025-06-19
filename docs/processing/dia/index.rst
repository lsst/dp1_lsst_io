.. _dia:

###############################
Difference image analysis (DIA)
###############################

DIA uses the decorrelated `Alard and Lupton (1998) <https://ui.adsabs.harvard.edu/abs/1998ApJ...503..325A/abstract>`_
image differencing algorithm,
as described in "Implementation of Image Difference Decorrelation" (`dmtn-021.lsst.io <https://dmtn-021.lsst.io/>`_)
and in the LSST Science Pipelines documentation for
(`Alard-Lupton implementation <https://pipelines.lsst.io/modules/lsst.ip.diffim/AL_implementation.html>`_).

Key terminology:

* ``DiaSource``: a detection, positive or negative, in a single difference image
* ``DiaObject``: the astrophysical transient or variable object at a static sky coordinate


**Light curves:** the forced photometry fluxes should be used for light curves.

All measurements are stored in the catalog :doc:`/products/index`.


.. _dia-image:

Difference images
=================

Template coadd images are warped, scaled, and PSF-matched to a visit image,
and then subtracted from the visit image to create a difference image.

In the context of DIA, the visit image is sometimes referred to as the
"direct" or "science" image.

For *future* data releases, to save space, the difference images won't be stored.
Instead, a tool for on-the-fly difference image recreation will be provided to users.

For DP1, the difference images are served and can be retrieved
and displayed by users instantaneously, but the inputs and tools
for their re-creation are not supplied.


.. _dia-source:

DIA source detection
====================

DIA source detection refers to the process of finding regions with above-threshold
absolute flux in difference images, where the threshold is a signal-to-noise ratio of 5.

Difference images contain sources of residual flux from the subtraction, both
positive and negative.
Real astrophyisical transients, variables, and moving objects appear as sources with
a flux that's equal to the difference between their flux in the template and visit images.

Spurious sources are also present due to unavoidably imperfect template matching.

Deblending isn't run on difference image sources.

The results of DIA source detection are stored in the ``DiaSource`` catalog.


Reliability score
-----------------

Real and spurious DIA sources can both be detected with a signal-to-noise ratio of 5.

DP1 uses a relatively simple machine learning reliability model,
trained on simulated data and injected point sources labelled by Rubin staff,
and applied to DIA sources.
The reliability value is stored in the ``reliability`` column of the ``DiaSource`` catalog.

Bright stars and correlated noise are the main sources of spurious detections.


Dipoles
-------

Sources with footprints containing both positive and negative peaks were fit with a
dipole centroid code.
Dipoles represent sources that have moved only slightly (e.g., less than the PSF)
between template and visit image.


Pixel flags
-----------

If the footprint contains one or more flagged pixels,
e.g., for cosmic rays, detector edge, bad pixels,
known artifacts, non-astrophysical trails,
the source is also flagged.



.. _dia-object:

DIA object association
======================

DIA sources are associated into DIA objects using a radius of 1 arcsecond.

The DIA objects are stored in the ``DiaObject`` catalog.


Variability characterization
----------------------------

Light curve characterization parameters are calculated for all DIA objects,
such as the minimum, mean, maximum, standard deviation and skew in the
difference image fluxes, the light curve's slope, percentiles, and ``StetsonJ``
parameter.



.. _dia-forcephot:

DIA forced photometry
=====================

In general, "forced" photometry means a measurement is made at a fixed coordinate in an image,
regardless of whether an above-threshold region was detected in that particular image.

Forced PSF photometry measurements are made on all visit and difference images
at the locations of all DIA objects.
The results are stored in the ``ForcedSourceOnDiaObject`` catalog.

