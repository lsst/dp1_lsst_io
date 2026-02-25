.. _flag-definitions:

###################################
Flag definitions and categories
###################################

What is a flag column?
======================

A flag column is a boolean (True/False) column in a catalog table that indicates whether a specific condition, issue, or failure occurred during measurement or processing.

Key characteristics:

- Data type: Boolean (``bool`` or ``boolean`` in the schema)
- Naming convention: Most flag columns have ``flag`` in the column name (e.g., ``psfFlux_flag``, ``pixelFlags_saturated``). Some flags, such as those related to calibration (``calib_*``) and deblending (``deblend_*``), do not include "flag" in their name. The naming pattern is typically ``{band}_{measurement}_flag`` for the Object table and ``{measurement}_flag`` for Source-level tables.
- Interpretation: ``1`` (True) indicates the condition occurred or the measurement failed; ``0`` (False) indicates success or absence of the issue
- Usage: Users typically filter out rows where critical flags are set to ``1`` to obtain clean, science-quality samples

Flag inventory across DP1 tables
=================================

DP1 contains 660+ flag columns distributed across five catalog tables:

.. list-table:: Flag column distribution
   :header-rows: 1
   :widths: 25 15 60

   * - Table
     - Flag columns
     - Description
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

Tables without flag columns: :ref:`DiaObject <catalogs-dia-object>`, :ref:`Visit <catalogs-visit-table>`, :ref:`CcdVisit <catalogs-visit-detector-table>`, :ref:`CoaddPatches <catalogs-coadd-patches>`, :ref:`SSObject <catalogs-ss-object>`, :ref:`SSSource <catalogs-ss-source>`, MPCORB contain metadata and aggregate statistics but no per-row quality flags.

Flag categories
===============

Flags can be organized into functional categories based on what they indicate:

Pixel quality flags
-------------------

Pattern: ``{band}_pixelFlags_*``

Purpose: Report on issues with individual pixels in the source footprint, derived from :ref:`image mask planes <images-mask-planes>`.

Common pixel flags:

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Flag name
     - Tables
     - Meaning
   * - ``pixelFlags_saturated``
     - Object, Source, DiaSource
     - Saturated pixels in footprint; photometry unreliable
   * - ``pixelFlags_saturatedCenter``
     - Object, Source, DiaSource
     - Saturated pixel in central 3x3 region; critical quality issue
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
     - Source on CCD edge (deprecated for Object coadds; see ``sensor_edge``)
   * - ``pixelFlags_sensor_edge``
     - Object
     - Detector boundary crossed footprint
   * - ``pixelFlags_sensor_edgeCenter``
     - Object
     - Detector edge near center; important for coadds
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
   * - ``pixelFlags_inexact_psfCenter``
     - Object
     - PSF model discontinuous at center (OR of CLIPPED, REJECTED, SENSOR_EDGE)

Key distinction -- "Center" variants: Flags with ``Center`` suffix indicate the issue affects the object's central region (typically a 3x3 pixel box), which is more critical for photometry and shapes than flags affecting only the outer footprint.

Coadd-specific flags: On Object table coadds, ``pixelFlags_edge`` and ``pixelFlags_offimage`` are deprecated. Use ``pixelFlags_sensor_edge`` and ``pixelFlags_sensor_edgeCenter`` instead, which indicate where detector boundaries from input visits crossed the object.

Measurement failure flags
--------------------------

Pattern: ``*_flag`` (algorithm-specific)

Purpose: Indicate that a particular measurement algorithm failed or produced unreliable results.

General failure flags:

.. list-table::
   :header-rows: 1
   :widths: 30 15 55

   * - Flag name
     - Tables
     - Meaning when set to 1
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
     - Centroid algorithm failed; do not trust position
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

Subflag pattern: Many algorithms provide detailed subflags explaining why the measurement failed (e.g., ``psfFlux_flag_edge``, ``psfFlux_flag_noGoodPixels``).
If the general flag is set to ``1``, the specific failure reason may be in a subflag, but the general flag alone is sufficient to filter the measurement.

Usage rule: If you use a measured quantity (flux, shape, etc.), require its corresponding general flag to be ``0``.
Example: When using ``r_psfFlux``, require ``r_psfFlux_flag = 0``.

Deblending flags
----------------

Purpose: Indicate status and quality of the deblending process (separating overlapping sources).

Source table deblending flags:

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Flag name
     - Tables
     - Meaning and recommendation
   * - ``deblend_nChild``
     - Source
     - Number of deblended children. If > 0, this is a parent (blended group) and should not be used as an independent object (to avoid double-counting). Require ``deblend_nChild = 0`` for science samples.
   * - ``deblend_skipped``
     - Source
     - Deblender skipped this source (too complex, too many peaks, or footprint too large). This parent record contains flux from multiple objects. Exclude sources with ``deblend_skipped = 1`` to avoid contaminated photometry.
   * - ``deblend_tooManyPeaks``
     - Source
     - Deblending skipped due to excessive peaks in footprint (often accompanies ``deblend_skipped``).
   * - ``deblend_parentTooBig``
     - Source
     - Deblending skipped because parent footprint was too large.
   * - ``deblend_deblendedAsPsf``
     - Source
     - Source treated as point source during deblending (informational; not a failure).
   * - ``deblend_hasStrayFlux``
     - Source
     - Blend had unassigned "stray flux" not allocated to children; photometry may be incomplete.
   * - ``deblend_masked``
     - Source
     - Majority of parent footprint was masked; often leads to ``deblend_skipped``.

Typical science cut: ``deblend_nChild = 0 AND deblend_skipped = 0``

This ensures you use only isolated sources or properly deblended children, excluding blended parents and complex cases.

.. _calibration-flags:

Calibration usage flags
-----------------------

Pattern: ``{band}_calib_*``

Purpose: Indicate whether a source was used in astrometric calibration, photometric calibration, or PSF modeling during single-visit processing.

Common calibration flags:

.. list-table::
   :header-rows: 1
   :widths: 30 15 55

   * - Flag name
     - Tables
     - Meaning when set to 1
   * - ``calib_astrometry_used``
     - Source
     - Source used in astrometric (WCS) solution
   * - ``calib_photometry_used``
     - Source
     - Source used in photometric zeropoint determination
   * - ``calib_photometry_reserved``
     - Source
     - Source reserved from photometric calibration (held out for validation)
   * - ``calib_psf_used``
     - Source
     - Source used for PSF modeling
   * - ``calib_psf_reserved``
     - Source
     - Source reserved from PSF determination
   * - ``calib_psf_candidate``
     - Source
     - Source was a candidate for PSF star selection

Important DP1 caveat: In DP1, these flags reflect preliminary single-visit calibration selections and are not updated for final global calibrations (FGCM photometry, refined astrometry).
There are known mismatches between single-visit and final calibrations.

Usage recommendation: Use with caution.
These flags are primarily diagnostic.
You may exclude calibrator stars if needed (e.g., ``calib_photometry_used = 0`` to remove stars used for zeropoint fitting), but the preliminary nature means some true calibrators won't be flagged and vice versa.
For most science, these flags can be ignored.

Difference imaging flags
------------------------

DiaSource-specific flags:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Flag name
     - Meaning and recommendation
   * - ``isDipole``
     - Detection classified as dipole artifact (imperfect image subtraction). Exclude dipoles (``isDipole = 0``) for clean transient samples; these are typically subtraction residuals of bright stars.
   * - ``reliability``
     - Real/bogus score (0-1); higher = more likely real astrophysical source. Apply threshold (e.g., ``reliability > 0.5`` or ``> 0.8``) to remove artifacts (cosmic rays, ghosts, dipoles). Preliminary model in DP1; use with awareness it may filter some real variables.
   * - ``psfDiffFlux_flag``
     - PSF flux on difference image failed. Require ``0`` to use difference flux.
   * - ``forced_PsfFlux_flag``
     - Forced flux on direct (science) image failed. If using science image flux (``scienceFlux``), require ``0``.

ForcedSourceOnDiaObject difference imaging flags:

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Flag name
     - Meaning
   * - ``psfDiffFlux_flag``
     - Forced PSF flux on difference image failed
   * - ``diff_PixelFlags_nodataCenter``
     - Position outside difference image coverage (no template); difference flux invalid

Specialized flags
-----------------

Other notable flags:

.. list-table::
   :header-rows: 1
   :widths: 30 20 50

   * - Flag name
     - Tables
     - Meaning
   * - ``invalidPsfFlag``
     - Object, ForcedSource, ForcedSourceOnDiaObject
     - PSF model invalid (no inputs); measurements unreliable. Exclude these sources.
   * - ``blendedness_flag``
     - Object, Source
     - Blendedness measurement algorithm failed
   * - ``inputCount_flag``
     - Object
     - Failed to compute number of coadd input exposures
   * - ``trail_flag_edge``
     - DiaSource
     - Trailed source (streak) extended off image edge
