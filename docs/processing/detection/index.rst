.. _detection:

################################
Source detection and measurement
################################

Sources in the visit and deep coadd images are detected, deblended, and measured
following (approximately) the process in `Bosch et al. (2018) <https://ui.adsabs.harvard.edu/abs/2018PASJ...70S...5B/abstract>`_,
as described in
"The LSST Science Pipelines Software: Optical Survey Pipeline Reduction and Analysis Environment"
(`pstn-019.lsst.io <https://pstn-019.lsst.io/>`_).

All measurements are stored in the catalog :doc:`/products/index`.


Sources and objects
===================

Key terminology:

* ``source``: a detection in a single processed visit image
* ``object``: an astrophysical object at a static sky coordinate

Measurements made on objects in a processed visit image are called "sources".

Measurements made on objects in the deep coadd images are called "objects".


.. _detection-detection:

Detection
=========

Detection refers specifically to the process of finding regions with above-threshold flux
in images, with one or more peaks within them.
These regions are called ``Footprints``.

The threshold used for detection is a signal-to-noise ratio > 5.


Pixel flags
-----------

If the footprint contains one or more flagged pixels,
e.g., for cosmic rays, detector edge, bad pixels, or flux saturation,
the source is also flagged.


.. _detection-deblend:

Deblending
==========

After detection, ``Footprints`` with multiple peaks are deblended into
"children" (with the original blended footprint called the "parent").

The Scarlet Lite algorithm is used for deblending, as described in
"The current state of scarlet and looking toward the future" (`dmtn-194.lsst.io <https://dmtn-194.lsst.io/>`_).

Only the deblended children are included in the catalogs.


.. _detection-measurement:

Measurement
===========

A large variety of centroid, size, shape, and flux measurements are made
on the deblended children.
It is important to note that child fluxes may be sub-threshold
(signal-to-noise ratio < 5), if their parent was above-threshold.

In visit images, measurements of sources assume a PSF or Gaussian shape.
The results are stored in the ``Source`` catalog.

In deep coadd images, measurements of objects include both PSF and extended shapes.
A wide variety of flux measurements are pre-calculated, such as the
composite model (cModel), Gaussian-aperture-and-PSF (GaaP), and Sersic models.
The results are stored in the ``Object`` catalog.


.. _detection-forcephot:

Forced photometry
=================

In general, "forced" photometry means a measurement is made at a fixed coordinate in an image,
regardless of whether an above-threshold region was detected in that particular image.

All of the measurements in the ``Object`` catalog, which made on the deep coadd images,
are forced photometry measurements.
The set of fixed coordinates is the union set of all detected objects and sources
(even sources only detected in one visit, or one band).

Forced PSF photometry measurements are also made on all visit images
and all difference images at the locations of all objects.
The results are stored in the ``ForcedSource`` catalog.
