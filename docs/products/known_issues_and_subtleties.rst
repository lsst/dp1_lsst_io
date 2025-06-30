.. _products_known_issues_and_subtleties:

###########################
Known issues and subtleties
###########################

Crowded fields and deblend skipping
===================================

The DP1 observations include several fields that were selected in part because they presented a challenge for our pipelines (especially with respect to crowding), and we have included our best effort processing on these images despite the fact that it is in some cases very incomplete.

The most common failure mode is when so many peaks are detected in a single above-threshold region that the deblender determines that it would run out of memory trying to separate them and simply gives up, resulting in few or no entries in :ref:`catalogs-object` catalog in that region.
Unfortunately the data product that holds the flags that would make this condition easy to diagnose was not retained in the public release.

We are currently integrating a major change to our deblender that we hope will mitigate this problem in future processing, and future data releases will definitely include a coadd mask plane indicating when skipping still occurs, making the problem easier to diagnose.

It is likely that our direct image processing in crowded fields will still lag dedicated crowded-field photometry codes; Rubin's focus for these fields has always been image subtraction (where we do expect to compete with the state of the art), with the :ref:`catalogs-object` catalog a best-effort addition.

Image units
===========

All image data products are annotated as having units of ``nJy``, but this does not mean individual pixel values can be treated as direct measures of spectral flux density (any more than any other image with an AB magnitude zero point - which would be directly proportional to ``nJy`` - can be used this way).

Instead, it simply means that photometry algorithms that account for the PSF model and aperture corrections (see below) directly yield ``nJy`` fluxes.

Aperture corrections
====================

Rubin processing uses aperture corrections to ensure that different photometry estimators produce consistent results on point sources.
These corrections are measured by applying different algorithms to the same set of bright stars on each single-visit image and interpolating the ratio of each algorithm to a standard one (a background-compensated top-hat aperture flux), which is then used for all photometric calibration.
All fluxes other than the standard algorithm's are then multiplied by the interpolated flux ratio.
Aperture corrections on coadds are computed by averaging the single-detector ratios with the same weights that were used to combine images.

This scheme has several problems:

- These aperture corrections are well-defined for point sources only, but we still apply them for most of our galaxy-focused photometry algorithms (the ``sersic_*`` fluxes are the sole exception), since this at least makes them well-calibrated for poorly-resolved galaxies.

- Coadding apertures with the same weights as the images is only correct in the limit that the images have the same PSF.
  For fixed-aperture photometry a different combination should be used (and will be used in future data releases, if we use this scheme at all), and for PSF-dependent photometry no formally correct combination is possible.

- Ratios of fluxes on even bright stars can be very noisy, and in some cases the aperture correction is a significant fraction of our error budget.

Improving our approach to aperture corrections is a research project; we are not happy with the current situation, but have not yet identified a satisfactory alternative.

Flag columns
============

The measurement algorithms that populate our catalogs typically have both a "general" failure flag that is set for any failure and one or more detailed flags that can be used to identify exactly what happened.
We also have a suite of "pixel flags" (``*_pixelFlags_*``) that report on the image mask planes in the neighborhood of a source or object.

Science users are expected to filter their samples using both types of flags explicitly; almost no filtering has already been performed, and filtering on flags can depend greatly on the science case.

Forced photometry variants and blending
=======================================

There are a total of four variants of forced photometry in Rubin data release processing for the combination of two different reference catalogs (:ref:`catalogs-object` and :ref:`catalogs-dia-object`) and two different measurement images (:ref:`images-visit-image` and :ref:`images-difference-image`).
Each of the two forced photometry catalogs includes rows for both measurement images and a single reference catalog (:ref:`catalogs-forced-source` uses :ref:`catalogs-object` positions, while :ref:`catalogs-dia-forced-source` uses :ref:`catalogs-dia-object` positions).

We expect forced photometry on :ref:`images-difference-image` to behave best, especially in crowded regions, since image subtraction should remove neighbors even more effectively than the deblender we run on the coadds (note that we do not deblend when producing the :ref:`catalogs-dia-source` catalog, either).
There is no deblending whatsoever in our forced photometry on :ref:`images-visit-image`.

Calibration source catalogs and flags
=====================================

The public :ref:`catalogs-source` catalog does not contain the same single-visit detections used to estimate the PSF and fit for the astrometric and photometric calibrations.
Those initial sources (the ``single_visit_star`` and ``recalibrated_star`` butler dataset types) are some of the many intermediate data products that are not retained in a final data release, while :ref:`catalogs-source` detections are made on the final :ref:`images-visit-image` after all calibration steps are complete.

Furthermore, the :ref:`catalogs-object` catalog has a few columns (prefixed with ``calib_``) that purport to identify objects used in various calibration steps.
These are generated from a spatial match from the object positions to the initial sources positions, which means they can suffer from mismatch problems in rare cases.

A more serious problem is that these flags currently reflect our preliminary single-detector astrometric and photometric calibration steps, not the later FGCM and GBDES fits (they do reflect the stars that went into our final Piff PSF models, however).
This problem will be fixed in future data releases.

Ellipse parameterizations and units
===================================

All catalogs (but especially :ref:`catalogs-object`) currently report object sizes and shapes in pixel units, not angular units, and different ellipse parameterizations are used for different estimators (e.g. ``{ixx, iyy, ixy}``, ``{e1, e2, r}``, ``{r_x, r_y, rho}``), reflecting either the parameterization used directly in a measurement algorithm or the expectations of a particular astronomical subfield.

We expect to use angular units and consistent parameterization throughout in future data releases, with tooling provided to efficiently convert between the parameterization (which one is TBD) and those preferred by different subfields.

PSF models leak memory
======================

A bug in the library we use to map C++ code to Python (`pybind11 <https://pybind11.readthedocs.io/en/stable/index.html>`__) prevents our wrappers for Piff PSF objects from being correctly garbage-collected by Python when they are first constructed by C++ code (as is the case when they are loaded from storage).
Since these PSF objects are attached to our processed image data products (i.e. everything but :ref:`images-raw`), loading many of any of these in the same process can slowly increase memory consumption until the process (such as a notebook kernel) is shut down.
The same is true of the ``visit_summary`` butler dataset type.

One workaround for this is to only read the ``image``, ``mask``, or ``variance`` component of an image data product (see :ref:`images`), which can also be more efficient when the rest of the data product is not needed.

This bug has been fixed in the latest version of pybind11, which we will adopt before the next data release.
As this upgrade will involve breaking changes, we may not be able to include it in the 29.x release series.
