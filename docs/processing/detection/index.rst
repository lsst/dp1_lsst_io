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

The term "sources" refers to measurements made on detections in a processed visit image.

The term "objects" refers to measurements made on detections in the deep coadd images.


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

The Scarlet Lite algorithm performs the deblending, as described in
"The current state of scarlet and looking toward the future" (`dmtn-194.lsst.io <https://dmtn-194.lsst.io/>`_).

The catalogs only include the deblended children.


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
composite model (cModel), Gaussian-aperture-and-PSF (`GaaP <https://ui.adsabs.harvard.edu/abs/2008A%26A...482.1053K/abstract>`_), and Sersic models.
The results are stored in the ``Object`` catalog.


.. _detection-forcephot:

Forced photometry
=================

In general, "forced" photometry refers to a measurement made at a fixed coordinate in an image,
regardless of whether an above-threshold region was detected in that particular image.

Most of the photometry measurements in the ``Object`` catalog, made on deep coadd images,
are forced photometry measurements, made at the centroid from the "reference" band.
The reference band is chosen based on detection significance using the priority order of i, r, z, y, g, then u band.

When a photometry algorithm also involves fitting an ellipse, three different approaches are used:

* In most elliptical galaxy photometry (e.g. Kron), the aperture is a multiple of the second-moment shape measured in the reference band.
* In `cModel <https://www.sdss3.org/dr8/algorithms/magnitudes.php#cmodel>`_ galaxy fitting, the models are fit independently to each band, and the fit from the reference image is used for additional forced photometry in all bands.
* In multiprofit galaxy fitting, the models are fit simultaneously to all bands.

Forced PSF photometry measurements are also made on all visit images
and all difference images at the locations of all objects.
The results are stored in the ``ForcedSource`` catalog.
