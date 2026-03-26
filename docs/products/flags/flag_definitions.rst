.. _flag-definitions:

###############################
Flag definitions and categories
###############################

Flag inventory across DP1 tables
=================================

DP1 contains 660 flag columns distributed across five catalog tables, as listed in the table below.

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Table
     - Flag columns
     - Flag types
   * - :ref:`Object <catalogs-object>`
     - 512
     - Pixel quality, measurement failure, extendedness, and calibration flags across 6 photometric bands (u, g, r, i, z, y).
   * - :ref:`Source <catalogs-source>`
     - 82
     - Centroiding, photometry, and calibration flags.
   * - :ref:`ForcedSource <catalogs-forced-source>`
     - 15
     - Pixel quality and forced photometry flags.
   * - :ref:`DiaSource <catalogs-dia-source>`
     - 36
     - Pixel quality, real/bogus classification, and dipole flags.
   * - :ref:`ForcedSourceOnDiaObject <catalogs-dia-forced-source>`
     - 15
     - Pixel quality and forced difference-image photometry flags.

Flag categories
===============

To help users interpret flag meanings, the following sections organize flags into categories based on what the flag indicates.

Pixel quality flags
-------------------

Pattern: ``{band}_pixelFlags_*``

Purpose: Report on issues with individual pixels in the source footprint, derived from :ref:`image mask planes <images-mask-planes>`.

The most commonly used pixel quality flags are listed in the table below.

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Flag name
     - Tables
     - Meaning when set to 1
   * - ``pixelFlags_saturated``
     - Object, Source, DiaSource
     - Saturated pixels in footprint; photometry unreliable.
   * - ``pixelFlags_saturatedCenter``
     - Object, Source, DiaSource
     - Saturated pixel in central 3x3 footprint; critical quality issue.
   * - ``pixelFlags_cr``
     - Object, Source, DiaSource
     - Cosmic ray detected and interpolated in footprint.
   * - ``pixelFlags_crCenter``
     - Object, Source, DiaSource
     - Cosmic ray at center.
   * - ``pixelFlags_interpolated``
     - Object, Source, DiaSource
     - Interpolated pixels in footprint (from CRs, defects, saturation).
   * - ``pixelFlags_interpolatedCenter``
     - Object, Source, DiaSource
     - Interpolated pixel at center; affects core photometry and shapes.
   * - ``pixelFlags_edge``
     - Source, DiaSource
     - Source on CCD edge (deprecated for Object coadds; see ``sensor_edge``).
   * - ``pixelFlags_sensor_edge``
     - Object
     - Detector boundary crossed footprint.
   * - ``pixelFlags_sensor_edgeCenter``
     - Object
     - Detector edge near center; important for coadds.
   * - ``pixelFlags_bad``
     - Object, Source, DiaSource
     - Known bad pixels (detector defects) in footprint.
   * - ``pixelFlags_suspect``
     - Source, DiaSource
     - Suspect pixels (near saturation, non-linear response).
   * - ``pixelFlags_suspectCenter``
     - Source, DiaSource
     - Suspect pixel at center.
   * - ``pixelFlags_clipped``
     - Object
     - Artifact rejection during coaddition excluded input pixels.
   * - ``pixelFlags_clippedCenter``
     - Object
     - Clipping occurred at center.
   * - ``pixelFlags_nodata``
     - Object, Source, DiaSource
     - No pixel data available (off coverage area).

Key points:

- Center variants: Flags with ``Center`` suffix indicate the issue affects the object's central footprint (typically a 3x3 pixel box), which is more critical for photometry and shapes than flags affecting only the outer footprint.
- Coadd-specific flags: On Object table coadds, ``pixelFlags_edge`` is deprecated. Use ``pixelFlags_sensor_edge`` and ``pixelFlags_sensor_edgeCenter`` instead, which indicate where detector boundaries from input visits crossed the object.

Measurement failure flags
--------------------------

Pattern: ``*_flag`` (algorithm-specific)

Purpose: Indicate that a particular measurement algorithm failed or produced unreliable results.

The general measurement failure flags are listed in the table below.

.. list-table::
   :header-rows: 1
   :widths: 30 15 55

   * - Flag name
     - Tables
     - Meaning when set to 1
   * - ``{band}_psfFlux_flag``
     - Object, Source, ForcedSource
     - PSF flux measurement failed; do not use PSF flux.
   * - ``{band}_cModel_flag``
     - Object, Source
     - Galaxy model (CModel) fit failed; do not use model fluxes.
   * - ``{band}_kronFlux_flag``
     - Object
     - Kron aperture flux failed (bad radius, near edge).
   * - ``{band}_apNNFlux_flag``
     - Object, Source
     - Aperture flux in NN-pixel aperture failed.
   * - ``{band}_gaapFlux_flag``
     - Object
     - GAaP (Gaussian Aperture and PSF) photometry failed.
   * - ``centroid_flag``
     - Source, DiaSource
     - Centroid algorithm failed; do not trust position.
   * - ``{band}_extendedness_flag``
     - Object, Source
     - Star/galaxy classifier failed; extendedness value unreliable.
   * - ``{band}_sizeExtendedness_flag``
     - Object
     - Shape-based star/galaxy classifier failed.
   * - ``shape_flag``
     - Source, DiaSource
     - Shape measurement (second moments) failed.
   * - ``{band}_hsmShapeRegauss_flag``
     - Object
     - HSM Regaussianization shape measurement failed.

Key points:

- Measurement values when flagged: ``{band}_psfFlux_flag`` is set when the algorithm returns a non-finite flux or a flux error. When the flux is finite, a set flag could be related to other types of errors, such as ``pixelFlags_saturatedCenter = 1``.
- Subflag pattern: Many algorithms provide detailed subflags explaining why the measurement failed (e.g., ``psfFlux_flag_edge``, ``psfFlux_flag_noGoodPixels``). If the general flag is set to ``1``, the specific failure reason may be in a subflag, but the general flag alone is sufficient to filter the measurement.
- Usage rule: If a measured quantity (flux, shape, etc.) is used, the corresponding general flag should be required to be ``0``. For example, when using ``r_psfFlux``, require ``r_psfFlux_flag = 0``.

Difference imaging flags
------------------------

The DiaSource-specific flags are listed in the table below.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Flag name
     - Meaning and recommendation
   * - ``isDipole``
     - Detection classified as dipole artifact (imperfect image subtraction). Exclude dipoles (``isDipole = 0``) for clean transient samples; these are typically subtraction residuals of bright stars.
   * - ``psfDiffFlux_flag``
     - PSF flux on difference image failed. Require ``0`` to use difference flux.
   * - ``forced_PsfFlux_flag``
     - Forced flux on direct (science) image failed. If using science image flux (``scienceFlux``), require ``0``.

The ForcedSourceOnDiaObject difference imaging flags are listed in the table below.

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Flag name
     - Meaning when set to 1
   * - ``psfDiffFlux_flag``
     - Forced PSF flux on difference image failed.
   * - ``diff_PixelFlags_nodataCenter``
     - Position outside difference image coverage (no template); difference flux invalid.
   * - ``psfFlux_flag``
     - Forced PSF flux on science image failed.

Specialized flags
-----------------

Other notable flags are listed in the table below.

.. list-table::
   :header-rows: 1
   :widths: 30 20 50

   * - Flag name
     - Tables
     - Meaning when set to 1
   * - ``invalidPsfFlag``
     - Object, ForcedSource, ForcedSourceOnDiaObject
     - PSF model invalid (no inputs); measurements unreliable. Exclude these sources.
   * - ``blendedness_flag``
     - Object, Source
     - Blendedness measurement algorithm failed.
   * - ``inputCount_flag``
     - Object
     - Failed to compute number of coadd input exposures.
   * - ``trail_flag_edge``
     - DiaSource
     - Trailed source (streak) extended off image edge.

.. _calibration-flags:

Calibration usage flags
-----------------------

Pattern: ``{band}_calib_*``

For most science, these flags can be ignored as they pertain to internal use in the calibration process.

These flags indicate whether a source was used in astrometric calibration, photometric calibration, or PSF modeling during single-visit processing.

The common calibration flags are listed in the table below.

.. list-table::
   :header-rows: 1
   :widths: 30 15 55

   * - Flag name
     - Tables
     - Meaning when set to 1
   * - ``calib_astrometry_used``
     - Source
     - Source used in astrometric (WCS) solution.
   * - ``calib_photometry_used``
     - Source
     - Source used in photometric zeropoint determination.
   * - ``calib_photometry_reserved``
     - Source
     - Source reserved from photometric calibration (held out for validation).
   * - ``calib_psf_used``
     - Source
     - Source used for PSF modeling.
   * - ``calib_psf_reserved``
     - Source
     - Source reserved from PSF determination.
   * - ``calib_psf_candidate``
     - Source
     - Source was a candidate for PSF star selection.

Important DP1 caveat: In DP1, these flags reflect preliminary single-visit calibration selections and are not updated for final global calibrations (FGCM photometry, refined astrometry).
There are known mismatches between single-visit and final calibrations.

These flags are primarily diagnostic.
Calibrator stars can be excluded if needed (e.g., ``calib_photometry_used = 0`` to remove stars used for zeropoint fitting), but the preliminary nature means some true calibrators will not be flagged and vice versa.
