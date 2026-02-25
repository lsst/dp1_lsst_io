.. _flag-recommendations:

###########################################
Recommended flag usage and mask planes
###########################################

Recommended flag usage by table
================================

This section provides table-specific guidance on which flags to apply for typical science-quality selections.

.. _flags-object:

Object table
------------

Purpose: Deep coadd measurements of static sky objects.

Critical flags to require equal to 0:

Minimal quality cuts (recommended for most science):

.. code-block:: sql

   -- For r-band example; adjust band as needed
   WHERE r_psfFlux_flag = 0                    -- PSF flux succeeded
     AND r_pixelFlags_saturatedCenter = 0      -- No saturation at center
     AND r_pixelFlags_crCenter = 0              -- No cosmic ray at center
     AND r_pixelFlags_interpolatedCenter = 0   -- No interpolation at center
     AND r_pixelFlags_sensor_edgeCenter = 0    -- Not on detector edge
     AND r_pixelFlags_inexact_psfCenter = 0    -- PSF model not discontinuous at center
     AND r_invalidPsfFlag = 0                   -- Valid PSF model

Additional filters for specific science:

Galaxy samples (model photometry):

.. code-block:: sql

   AND r_cModel_flag = 0          -- CModel fit succeeded
   AND r_extendedness = 1              -- Extended source (galaxy)
   AND r_extendedness_flag = 0     -- Classification valid

Star samples (PSF photometry):

.. code-block:: sql

   AND r_extendedness = 0              -- Point source (star)
   AND r_extendedness_flag = 0     -- Classification valid
   AND r_pixelFlags_edge = 0       -- Not on any edge (optional stricter cut)

Stars used and reserved in PSF modeling can also be identified using ``{band}_calib_psf_used`` and ``{band}_calib_psf_reserved`` in the Source table (see :ref:`calibration-flags`).

High-precision photometry or shapes:

.. code-block:: sql

   AND r_kronFlux_flag = 0         -- If using Kron flux
   AND r_hsmShapeRegauss_flag = 0  -- If using HSM shapes
   AND r_pixelFlags_interpolated = 0  -- Minimal interpolation (optional)

Multi-band requirements: When requiring detections in multiple bands, ensure flux measurements and key pixel flags are valid in each band used.
Check ``pixelFlags_nodata`` to confirm coverage.

Band-specific flags: Object table has ~100 flags per band.
The naming pattern is ``{band}_{measurement}_flag`` (e.g., ``g_psfFlux_flag``, ``i_cModel_flag``).
Apply the same flag logic to each band independently.

.. _flags-source:

Source table
------------

Purpose: Single-epoch visit detections.

Critical flags to require equal to 0:

Standard source quality selection:

.. code-block:: sql

   WHERE centroid_flag = 0              -- Centroid succeeded (position reliable)
     AND psfFlux_flag = 0               -- PSF flux succeeded
     AND pixelFlags_edge = 0            -- Not on CCD edge
     AND pixelFlags_saturatedCenter = 0 -- No saturation at center
     AND pixelFlags_bad = 0             -- No bad pixels
     AND deblend_nChild = 0                 -- Not a parent (avoid double-counting)
     AND deblend_skipped = 0            -- Deblending completed

Additional recommended cuts:

.. code-block:: sql

   AND pixelFlags_crCenter = 0          -- No cosmic ray at center
   AND pixelFlags_interpolatedCenter = 0 -- No interpolation at center
   AND pixelFlags_suspectCenter = 0      -- No suspect pixels at center

Deblending note: Always use ``deblend_nChild = 0`` to select isolated sources or deblended children.
Parents (``deblend_nChild > 0``) represent blended groups and should not be treated as individual objects.
Sources with ``deblend_skipped = 1`` are complex blends that failed deblending and should also be excluded.

Calibration stars: If specifically selecting or excluding calibration stars, use ``calib_*`` flags (including ``calib_psf_used`` and ``calib_psf_reserved``), but note DP1 caveats (:ref:`calibration-flags`).

.. _flags-forced-source:

ForcedSource table
------------------

Purpose: Forced photometry at Object positions on single-epoch images.

Critical flags to require equal to 0 (per measurement):

.. code-block:: sql

   WHERE psfFlux_flag = 0               -- Direct image PSF flux succeeded
     AND pixelFlags_saturatedCenter = 0 -- No saturation at forced position
     AND pixelFlags_edge = 0            -- Position not on edge
     AND invalidPsfFlag = 0             -- PSF model valid

If using difference image flux:

.. code-block:: sql

   AND psfDiffFlux_flag = 0             -- Difference flux succeeded
   AND diff_PixelFlags_nodataCenter = 0 -- Difference image has coverage

Light curve usage: When constructing light curves, apply these flags to each measurement (row) individually.
This filters out poor-quality epochs while retaining good measurements for the same object across other visits.

.. _flags-dia-source:

DiaSource table
---------------

Purpose: Transient/variable detections on difference images.

Critical flags for transient science:

High-confidence real astrophysical transients:

.. code-block:: sql

   WHERE isDipole = 0                   -- Not a subtraction dipole artifact
     AND reliability > 0.5                  -- Likely real (adjust threshold as needed)
     AND psfFlux_flag = 0               -- Difference flux succeeded
     AND pixelFlags_edge = 0            -- Not on edge
     AND pixelFlags_saturatedCenter = 0 -- No saturation
     AND pixelFlags_bad = 0             -- No bad pixels

Reliability threshold guidance:

- ``reliability > 0.5``: Balanced cut; removes most artifacts while retaining real variables
- ``reliability > 0.8``: High-purity sample; may lose some real faint variables
- ``reliability > 0.3``: Higher completeness; includes more potential artifacts

DP1 reliability caveat: The real/bogus classifier in DP1 is preliminary.
It may assign lower scores to some real variables (especially variable stars) that didn't match training expectations.
Always consider your science tolerance for contamination versus completeness.

Additional quality filters:

.. code-block:: sql

   AND centroid_flag = 0                -- Position reliable
   AND pixelFlags_cr = 0                -- Not a cosmic ray residual

.. _flags-dia-forced:

ForcedSourceOnDiaObject table
------------------------------

Purpose: Forced photometry at DiaObject positions on difference images.

Critical flags (per measurement):

.. code-block:: sql

   WHERE psfDiffFlux_flag = 0               -- Difference flux succeeded
     AND diff_PixelFlags_nodataCenter = 0   -- Difference image has coverage
     AND pixelFlags_saturatedCenter = 0     -- No saturation
     AND invalidPsfFlag = 0                  -- PSF valid

Usage: Apply these filters when building DiaObject light curves from forced photometry.
Similar to ForcedSource, filter per-measurement to remove bad epochs while keeping good ones.

Connection to image mask planes
================================

Catalog ``pixelFlags_*`` columns are directly derived from :ref:`image mask planes <images-mask-planes>`.
Each mask plane bit in the image (BAD, SAT, CR, INTRP, EDGE, etc.) propagates to a corresponding pixel flag in the catalog.

Key mask plane to flag mappings:

.. list-table::
   :header-rows: 1
   :widths: 20 25 55

   * - Mask Plane
     - Catalog Flag
     - Notes
   * - SAT
     - ``pixelFlags_saturated``
     - Saturated pixels
   * - CR
     - ``pixelFlags_cr``
     - Cosmic rays (interpolated in final images)
   * - INTRP
     - ``pixelFlags_interpolated``
     - Interpolated pixels (from CRs, defects, saturation)
   * - EDGE
     - ``pixelFlags_edge``
     - Image edge (single exposures)
   * - SENSOR_EDGE
     - ``pixelFlags_sensor_edge``
     - Detector boundaries (coadds)
   * - BAD
     - ``pixelFlags_bad``
     - Known bad pixels (detector defects)
   * - SUSPECT
     - ``pixelFlags_suspect``
     - Suspect pixels (near saturation)
   * - NO_DATA
     - ``pixelFlags_nodata``
     - No data available
   * - CLIPPED
     - ``pixelFlags_clipped``
     - Outlier rejection during coaddition
   * - REJECTED
     - (propagates to CLIPPED)
     - Input visit excluded during coaddition
   * - INEXACT_PSF
     - ``pixelFlags_inexact_psf``
     - PSF model discontinuous (OR of CLIPPED, REJECTED, SENSOR_EDGE)

Footprint vs center: Flags without ``Center`` suffix are set if any pixel in the source footprint has that mask bit.
``Center`` flags are set only if a pixel in the central 3x3 box has that bit.
For quality filtering, center flags are typically more important since they affect core photometry.

See :ref:`images-visit-mask-planes` and :ref:`images-deep-coadd-mask-planes` for detailed mask plane descriptions.
