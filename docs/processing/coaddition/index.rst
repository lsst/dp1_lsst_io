.. _coaddition:

################
Image coaddition
################

Coadded images are created by combining multiple calibrated images obtained in the
same filter and of the same region of the sky,
either to achieve greater sensitivity (i.e., "depth")
or a sharper image (i.e., by selecting images with good seeing).


.. _coaddition-patch:

Coadds by patch
===============

When producing coadded images, the processing pipeline refers to a skymap, which defines a grid of
2.2 square degree tracts covering the entire celestial sphere.
Each tract is further subdivided into 10 by 10 equally-sized patches, each covering
approximately 79 square arcminutes.

To create a coadded image, the processing pipeline selects all suitable
(i.e., surpassing certain quality thresholds) calibrated visit images
covering a given patch in a given filter,
warps them onto a single consistent pixel grid for that patch,
then coadds them.

Each individual coadd image covers a single patch.

Patches at the edge of the survey area might not be entirely covered
by the input visit images.
Unobserved sections of the deep coadd image have pixels with
no data flagged as "NO_DATA" in the mask plane.


.. _coaddition-visitselect:

Input image selection
=====================

The selection criteria for coadd inputs for DP1 does not represent the
selection criteria for future data release.

For the DP1 deep coadds, an visit image had to have a PSF FWHM < 1.7 arcseconds
to be selected as an input image.

For template coadds, good seeing (low PSF FWHM) is more important than depth.
For the DP1 template coadded images, the third of the visit images with lowest
PSF FWHM were used as inputs.
If there were less than 36 visit images in total, the 12 visit images with the lowest
PSF FWHM were used.


.. _coaddition-algorithm:

Image combination algorithm
===========================

Selected exposures are combined using a mean
stacking algorithm, weighted by inverse variance.

To mitigate transient artifacts before coaddition,
an artifact rejection procedure first identifies and masks
features such as satellite trails, optical ghosts, and cosmic rays.

See "Coaddition Artifact Rejection and CompareWarp" (`dmtn-080.lsst.io <https://dmtn-080.lsst.io/>`_).



.. _coaddition-background:

Coadd background subtraction
============================

After image coaddition, a constant background residual is fit and subtracted.