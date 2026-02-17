.. _catalogs-flags:

######################
Catalog flag columns
######################

Data Preview 1 (DP1) catalog tables contain extensive boolean flag columns that indicate quality issues, processing failures, or special conditions identified during Science Pipelines processing.
**These flags are provided for users to apply as quality filters based on their science requirements.**
DP1 data is delivered largely "as measured" with minimal a priori filtering, since the appropriate flag criteria depend on the specific science case.

This page provides comprehensive guidance on understanding and using flag columns across all DP1 catalog tables.

.. contents::
   :local:
   :depth: 2

What is a flag column?
======================

**Definition:** A flag column is a boolean (True/False) column in a catalog table that indicates whether a specific condition, issue, or failure occurred during measurement or processing.

**Key characteristics:**

- **Data type:** Boolean (``bool`` or ``boolean`` in the schema)
- **Naming convention:** Most flag columns have ``flag`` in the column name (e.g., ``psfFlux_flag``, ``pixelFlags_saturated``)
- **Interpretation:** ``True`` (or 1) indicates the condition occurred or the measurement failed; ``False`` (or 0) indicates success or absence of the issue
- **Usage:** Users typically filter out rows where critical flags are ``True`` to obtain clean, science-quality samples

**Exception:** Calibration flags (``calib_*``) use different semantics—see :ref:`calibration-flags` below.

Flag inventory across DP1 tables
=================================

DP1 contains **660+ flag columns** distributed across five catalog tables:

.. list-table:: Flag column distribution
   :header-rows: 1
   :widths: 25 15 60

   * - **Table**
     - **Flag columns**
     - **Description**
   * - :ref:`Object <catalogs-object>`
     - 512
     - Coadded source measurements across 5 photometric bands (u, g, r, i, z); extensive per-band flags
   * - :ref:`Source <catalogs-source>`
     - 82
     - Single-epoch visit detections; includes centroiding, photometry, deblending flags
   * - :ref:`ForcedSource <catalogs-forced-source>`
     - 15
     - Forced photometry at Object positions; primarily pixel quality flags
   * - :ref:`DiaSource <catalogs-dia-source>`
     - 36
     - Difference imaging detections; includes real/bogus classification, dipole flags
   * - :ref:`ForcedSourceOnDiaObject <catalogs-dia-forced-source>`
     - 15
     - Forced photometry at DiaObject positions; similar to ForcedSource

Tables without flag columns: :ref:`DiaObject <catalogs-dia-object>`, :ref:`Visit <catalogs-visit-table>`, :ref:`CcdVisit <catalogs-visit-detector-table>`, :ref:`CoaddPatches <catalogs-coadd-patches>`, SSObject, SSSource, MPCORB contain metadata and aggregate statistics but no per-row quality flags.

Flag categories
===============

Flags can be organized into functional categories based on what they indicate:

Pixel quality flags
-------------------

**Pattern:** ``{band}_pixelFlags_*``

**Purpose:** Report on issues with individual pixels in the source footprint, derived from :ref:`image mask planes <images-mask-planes>`.

**Common pixel flags:**

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - **Flag name**
     - **Tables**
     - **Meaning**
   * - ``pixelFlags_saturated``
     - Object, Source, DiaSource
     - Saturated pixels in footprint; photometry unreliable
   * - ``pixelFlags_saturatedCenter``
     - Object, Source, DiaSource
     - Saturated pixel in central 3×3 region; **critical quality issue**
   * - ``pixelFlags_cr``
     - Object, Source, DiaSource
     - Cosmic ray detected and interpolated in footprint
   * - ``pixelFlags_crCenter``
     - Object, Source, DiaSource
     - Cosmic ray at center
   * - ``pixelFlags_interpolated``
     - Object, Source, DiaSource
     - Interpolated pixels in footprint (from CRs, defects, saturation)
   * - ``pixelFlags_interpolatedCenter``
     - Object, Source, DiaSource
     - Interpolated pixel at center; affects core photometry/shapes
   * - ``pixelFlags_edge``
     - Source, DiaSource
     - Source on CCD edge (deprecated for Object coadds—see ``sensor_edge``)
   * - ``pixelFlags_sensor_edge``
     - Object
     - Detector boundary crossed footprint
   * - ``pixelFlags_sensor_edgeCenter``
     - Object
     - Detector edge near center; **important for coadds**
   * - ``pixelFlags_bad``
     - Object, Source, DiaSource
     - Known bad pixels (detector defects) in footprint
   * - ``pixelFlags_suspect``
     - Source, DiaSource
     - Suspect pixels (near saturation, non-linear response)
   * - ``pixelFlags_suspectCenter``
     - Source, DiaSource
     - Suspect pixel at center
   * - ``pixelFlags_clipped``
     - Object
     - Artifact rejection during coaddition excluded input pixels
   * - ``pixelFlags_clippedCenter``
     - Object
     - Clipping occurred at center
   * - ``pixelFlags_nodata``
     - Object, Source, DiaSource
     - No pixel data available (off coverage area)

**Key distinction—"Center" variants:** Flags with ``Center`` suffix indicate the issue affects the object's central region (typically a 3×3 pixel box), which is more critical for photometry and shapes than flags affecting only the outer footprint.

**Coadd-specific flags:** On Object table coadds, ``pixelFlags_edge`` and ``pixelFlags_offimage`` are deprecated. Use ``pixelFlags_sensor_edge`` and ``pixelFlags_sensor_edgeCenter`` instead, which indicate where detector boundaries from input visits crossed the object.

Measurement failure flags
--------------------------

**Pattern:** ``*_flag`` (algorithm-specific)

**Purpose:** Indicate that a particular measurement algorithm failed or produced unreliable results.

**General failure flags:**

.. list-table::
   :header-rows: 1
   :widths: 30 15 55

   * - **Flag name**
     - **Tables**
     - **Meaning when True**
   * - ``{band}_psfFlux_flag``
     - Object, Source, ForcedSource
     - PSF flux measurement failed; do not use PSF flux
   * - ``{band}_cModel_flag``
     - Object, Source
     - Galaxy model (CModel) fit failed; do not use model fluxes
   * - ``{band}_kronFlux_flag``
     - Object
     - Kron aperture flux failed (bad radius, near edge)
   * - ``{band}_apNNFlux_flag``
     - Object, Source
     - Aperture flux in NN-pixel aperture failed
   * - ``{band}_gaapFlux_flag``
     - Object
     - GAaP (Gaussian Aperture and PSF) photometry failed
   * - ``centroid_flag``
     - Source, DiaSource
     - Centroid algorithm failed; **do not trust position**
   * - ``{band}_extendedness_flag``
     - Object, Source
     - Star/galaxy classifier failed; extendedness value unreliable
   * - ``{band}_sizeExtendedness_flag``
     - Object
     - Shape-based star/galaxy classifier failed
   * - ``shape_flag``
     - Source, DiaSource
     - Shape measurement (second moments) failed
   * - ``{band}_hsmShapeRegauss_flag``
     - Object
     - HSM Regaussianization shape measurement failed

**Subflag pattern:** Many algorithms provide detailed subflags explaining *why* the measurement failed (e.g., ``psfFlux_flag_edge``, ``psfFlux_flag_noGoodPixels``).
If the general flag is ``True``, the specific failure reason may be in a subflag, but **the general flag alone is sufficient to filter the measurement**.

**Usage rule:** If you use a measured quantity (flux, shape, etc.), **require its corresponding general flag to be False**.
Example: When using ``r_psfFlux``, require ``r_psfFlux_flag = False``.

Deblending flags
----------------

**Purpose:** Indicate status and quality of the deblending process (separating overlapping sources).

**Source table deblending flags:**

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - **Flag name**
     - **Meaning and recommendation**
   * - ``deblend_nChild``
     - Number of deblended children. If > 0, this is a parent (blended group) and should **not** be used as an independent object (to avoid double-counting). **Require** ``deblend_nChild = 0`` for science samples.
   * - ``deblend_skipped``
     - Deblender skipped this source (too complex, too many peaks, or footprint too large). This parent record contains flux from multiple objects. **Exclude** sources with ``deblend_skipped = True`` to avoid contaminated photometry.
   * - ``deblend_tooManyPeaks``
     - Deblending skipped due to excessive peaks in footprint (often accompanies ``deblend_skipped``).
   * - ``deblend_parentTooBig``
     - Deblending skipped because parent footprint was too large.
   * - ``deblend_deblendedAsPsf``
     - Source treated as point source during deblending (informational; not a failure).
   * - ``deblend_hasStrayFlux``
     - Blend had unassigned "stray flux" not allocated to children; photometry may be incomplete.
   * - ``deblend_masked``
     - Majority of parent footprint was masked; often leads to ``deblend_skipped``.

**Typical science cut:** ``deblend_nChild = 0 AND deblend_skipped = False``

This ensures you use only isolated sources or properly deblended children, excluding blended parents and complex cases.

.. _calibration-flags:

Calibration usage flags
-----------------------

**Pattern:** ``{band}_calib_*``

**Purpose:** Indicate whether a source was used in astrometric calibration, photometric calibration, or PSF modeling during single-visit processing.

**Common calibration flags:**

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - **Flag name**
     - **Meaning when True**
   * - ``calib_astrometry_used``
     - Source used in astrometric (WCS) solution
   * - ``calib_photometry_used``
     - Source used in photometric zeropoint determination
   * - ``calib_photometry_reserved``
     - Source reserved from photometric calibration (held out for validation)
   * - ``calib_psf_used``
     - Source used for PSF modeling
   * - ``calib_psf_reserved``
     - Source reserved from PSF determination
   * - ``calib_psf_candidate``
     - Source was a candidate for PSF star selection

**Important DP1 caveat:** In DP1, these flags reflect *preliminary* single-visit calibration selections and are **not updated** for final global calibrations (FGCM photometry, refined astrometry).
There are known mismatches between single-visit and final calibrations.

**Usage recommendation:** Use with caution.
These flags are primarily diagnostic.
You may exclude calibrator stars if needed (e.g., ``calib_photometry_used = False`` to remove stars used for zeropoint fitting), but the preliminary nature means some true calibrators won't be flagged and vice versa.
For most science, these flags can be ignored.

Difference imaging flags
------------------------

**DiaSource-specific flags:**

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - **Flag name**
     - **Meaning and recommendation**
   * - ``isDipole``
     - Detection classified as dipole artifact (imperfect image subtraction). **Exclude** dipoles (``isDipole = False``) for clean transient samples—these are typically subtraction residuals of bright stars.
   * - ``reliability``
     - Real/bogus score (0-1); higher = more likely real astrophysical source. **Apply threshold** (e.g., ``reliability > 0.5`` or ``> 0.8``) to remove artifacts (cosmic rays, ghosts, dipoles). Preliminary model in DP1; use with awareness it may filter some real variables.
   * - ``psfDiffFlux_flag``
     - PSF flux on difference image failed. Require ``False`` to use difference flux.
   * - ``forced_PsfFlux_flag``
     - Forced flux on direct (science) image failed. If using science image flux (``scienceFlux``), require this ``False``.

**ForcedSourceOnDiaObject difference imaging flags:**

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - **Flag name**
     - **Meaning**
   * - ``psfDiffFlux_flag``
     - Forced PSF flux on difference image failed
   * - ``diff_PixelFlags_nodataCenter``
     - Position outside difference image coverage (no template); difference flux invalid

Specialized flags
-----------------

**Other notable flags:**

.. list-table::
   :header-rows: 1
   :widths: 30 20 50

   * - **Flag name**
     - **Tables**
     - **Meaning**
   * - ``invalidPsfFlag``
     - Object, ForcedSource, ForcedSourceOnDiaObject
     - PSF model invalid (no inputs); measurements unreliable. **Exclude** these sources.
   * - ``blendedness_flag``
     - Object, Source
     - Blendedness measurement algorithm failed
   * - ``inputCount_flag``
     - Object
     - Failed to compute number of coadd input exposures
   * - ``trail_flag_edge``
     - DiaSource
     - Trailed source (streak) extended off image edge

Recommended flag usage by table
================================

This section provides table-specific guidance on which flags to apply for typical science-quality selections.

.. _flags-object:

Object table
------------

**Purpose:** Deep coadd measurements of static sky objects.

**Critical flags to require False:**

Minimal quality cuts (recommended for most science):

.. code-block:: sql

   -- For r-band example; adjust band as needed
   WHERE r_psfFlux_flag = 0                    -- PSF flux succeeded
     AND r_pixelFlags_saturatedCenter = 0      -- No saturation at center
     AND r_pixelFlags_crCenter = 0              -- No cosmic ray at center
     AND r_pixelFlags_interpolatedCenter = 0   -- No interpolation at center
     AND r_pixelFlags_sensor_edgeCenter = 0    -- Not on detector edge
     AND r_invalidPsfFlag = 0                   -- Valid PSF model

**Additional filters for specific science:**

*Galaxy samples (model photometry):*

.. code-block:: sql

   AND r_cModel_flag = 0          -- CModel fit succeeded
   AND r_extendedness > 0.5            -- Extended source
   AND r_extendedness_flag = 0     -- Classification valid

*Star samples (PSF photometry):*

.. code-block:: sql

   AND r_extendedness < 0.5            -- Point source
   AND r_extendedness_flag = 0     -- Classification valid
   AND r_pixelFlags_edge = 0       -- Not on any edge (optional stricter cut)

*High-precision photometry or shapes:*

.. code-block:: sql

   AND r_kronFlux_flag = 0         -- If using Kron flux
   AND r_hsmShapeRegauss_flag = 0  -- If using HSM shapes
   AND r_pixelFlags_interpolated = 0  -- Minimal interpolation (optional)

**Multi-band requirements:** When requiring detections in multiple bands, ensure flux measurements and key pixel flags are valid in *each* band used.
Check ``pixelFlags_nodata`` to confirm coverage.

**Band-specific flags:** Object table has ~100 flags per band.
The naming pattern is ``{band}_{measurement}_flag`` (e.g., ``g_psfFlux_flag``, ``i_cModel_flag``).
Apply the same flag logic to each band independently.

.. _flags-source:

Source table
------------

**Purpose:** Single-epoch visit detections.

**Critical flags to require False:**

Standard source quality selection:

.. code-block:: sql

   WHERE centroid_flag = 0              -- Centroid succeeded (position reliable)
     AND psfFlux_flag = 0               -- PSF flux succeeded
     AND pixelFlags_edge = 0            -- Not on CCD edge
     AND pixelFlags_saturatedCenter = 0 -- No saturation at center
     AND pixelFlags_bad = 0             -- No bad pixels
     AND deblend_nChild = 0                 -- Not a parent (avoid double-counting)
     AND deblend_skipped = 0            -- Deblending completed

**Additional recommended cuts:**

.. code-block:: sql

   AND pixelFlags_crCenter = 0          -- No cosmic ray at center
   AND pixelFlags_interpolatedCenter = 0 -- No interpolation at center
   AND pixelFlags_suspectCenter = 0      -- No suspect pixels at center

**Deblending note:** Always use ``deblend_nChild = 0`` to select isolated sources or deblended children.
Parents (``deblend_nChild > 0``) represent blended groups and should not be treated as individual objects.
Sources with ``deblend_skipped = True`` are complex blends that failed deblending and should also be excluded.

**Calibration stars:** If specifically selecting or excluding calibration stars, use ``calib_*`` flags, but note DP1 caveats (:ref:`calibration-flags`).

.. _flags-forced-source:

ForcedSource table
------------------

**Purpose:** Forced photometry at Object positions on single-epoch images.

**Critical flags to require False (per measurement):**

.. code-block:: sql

   WHERE psfFlux_flag = 0               -- Direct image PSF flux succeeded
     AND pixelFlags_saturatedCenter = 0 -- No saturation at forced position
     AND pixelFlags_edge = 0            -- Position not on edge
     AND invalidPsfFlag = 0             -- PSF model valid

**If using difference image flux:**

.. code-block:: sql

   AND psfDiffFlux_flag = 0             -- Difference flux succeeded
   AND diff_PixelFlags_nodataCenter = 0 -- Difference image has coverage

**Light curve usage:** When constructing light curves, apply these flags to each measurement (row) individually.
This filters out poor-quality epochs while retaining good measurements for the same object across other visits.

.. _flags-dia-source:

DiaSource table
---------------

**Purpose:** Transient/variable detections on difference images.

**Critical flags for transient science:**

High-confidence real astrophysical transients:

.. code-block:: sql

   WHERE isDipole = 0                   -- Not a subtraction dipole artifact
     AND reliability > 0.5                  -- Likely real (adjust threshold as needed)
     AND psfFlux_flag = 0               -- Difference flux succeeded
     AND pixelFlags_edge = 0            -- Not on edge
     AND pixelFlags_saturatedCenter = 0 -- No saturation
     AND pixelFlags_bad = 0             -- No bad pixels

**Reliability threshold guidance:**

- ``reliability > 0.5``: Balanced cut; removes most artifacts while retaining real variables
- ``reliability > 0.8``: High-purity sample; may lose some real faint variables
- ``reliability > 0.3``: Higher completeness; includes more potential artifacts

**DP1 reliability caveat:** The real/bogus classifier in DP1 is preliminary.
It may assign lower scores to some real variables (especially variable stars) that didn't match training expectations.
Always consider your science tolerance for contamination versus completeness.

**Additional quality filters:**

.. code-block:: sql

   AND centroid_flag = 0                -- Position reliable
   AND pixelFlags_cr = 0                -- Not a cosmic ray residual

.. _flags-dia-forced:

ForcedSourceOnDiaObject table
------------------------------

**Purpose:** Forced photometry at DiaObject positions on difference images.

**Critical flags (per measurement):**

.. code-block:: sql

   WHERE psfDiffFlux_flag = 0               -- Difference flux succeeded
     AND diff_PixelFlags_nodataCenter = 0   -- Difference image has coverage
     AND pixelFlags_saturatedCenter = 0     -- No saturation
     AND invalidPsfFlag = 0                  -- PSF valid

**Usage:** Apply these filters when building DiaObject light curves from forced photometry.
Similar to ForcedSource, filter per-measurement to remove bad epochs while keeping good ones.

Connection to image mask planes
================================

Catalog ``pixelFlags_*`` columns are directly derived from :ref:`image mask planes <images-mask-planes>`.
Each mask plane bit in the image (BAD, SAT, CR, INTRP, EDGE, etc.) propagates to a corresponding pixel flag in the catalog.

**Key mask plane to flag mappings:**

.. list-table::
   :header-rows: 1
   :widths: 20 25 55

   * - **Mask Plane**
     - **Catalog Flag**
     - **Notes**
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

**Footprint vs center:** Flags without ``Center`` suffix are set if *any* pixel in the source footprint has that mask bit.
``Center`` flags are set only if a pixel in the central 3×3 box has that bit.
For quality filtering, **center flags are typically more important** since they affect core photometry.

See :ref:`images-visit-mask-planes` and :ref:`images-deep-coadd-mask-planes` for detailed mask plane descriptions.

