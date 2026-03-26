.. _flag-recommendations:

######################
Flag usage guidance
######################

Flag usage guidance by table
================================

This section provides table-specific guidance on which flags to apply for typical science-quality selections.
The flags listed under "recommended quality filters" should be applied in most science analyses.
Additional filters are provided as guidance for specific science cases and should be adapted based on the science requirements.

.. _flags-object:

Object table
------------

Guidance for the application of flags on the deep coadd measurements of static sky objects.

Cuts for r-band PSF photometry are shown; adjust the band prefix as needed.

.. code-block:: sql

   -- For r-band example; adjust band as needed
   WHERE r_psfFlux_flag = 0                   -- PSF flux succeeded
     AND r_pixelFlags_saturatedCenter = 0     -- No saturation at center
     AND r_pixelFlags_crCenter = 0            -- No cosmic ray at center
     AND r_pixelFlags_interpolatedCenter = 0  -- No interpolation at center
     AND r_pixelFlags_sensor_edgeCenter = 0   -- Not on detector edge
     AND r_invalidPsfFlag = 0                 -- Valid PSF model

Additional filters for specific science cases are described below.

Galaxy samples (model photometry).

.. code-block:: sql

   AND r_cModel_flag = 0        -- CModel fit succeeded
   AND r_extendedness = 1       -- Extended source (galaxy)
   AND r_extendedness_flag = 0  -- Classification valid

.. note::

   The ``extendedness`` classifier in DP1 has not been fully characterized for purity or completeness.
   There is currently no published guidance on the selection function these cuts produce.
   Users should treat galaxy/star separation as approximate and validate against their specific science requirements.

Star samples (PSF photometry).

.. code-block:: sql

   AND r_extendedness = 0       -- Point source (star)
   AND r_extendedness_flag = 0  -- Classification valid

.. note::

   The same caveats about the ``extendedness`` classifier apply as for galaxy samples above.

Stars used and reserved in PSF modeling can also be identified using ``{band}_calib_psf_used`` and ``{band}_calib_psf_reserved`` in the Source table (see :ref:`calibration-flags`).

High-precision Kron photometry.

.. code-block:: sql

   AND r_kronFlux_flag = 0  -- Kron flux succeeded

High-precision shape measurements.

.. code-block:: sql

   AND r_hsmShapeRegauss_flag = 0  -- HSM shapes succeeded

Strict pixel quality (optional).

.. code-block:: sql

   AND r_pixelFlags_interpolated = 0  -- No interpolated pixels in footprint

Multi-band requirements: When requiring detections in multiple bands, ensure flux measurements and key pixel flags are valid in each band used.
Check ``pixelFlags_nodata`` to confirm coverage.

Band-specific flags: The Object table has approximately 100 flags per band.
The naming pattern is ``{band}_{measurement}_flag`` (e.g., ``g_psfFlux_flag``, ``i_cModel_flag``).
Apply the same flag logic to each band independently.

.. _flags-source:

Source table
------------

Guidance for the application of flags on single-epoch visit detections.

.. code-block:: sql

   WHERE centroid_flag = 0               -- Centroid succeeded
     AND psfFlux_flag = 0                -- PSF flux succeeded
     AND pixelFlags_edge = 0             -- Not on CCD edge
     AND pixelFlags_saturatedCenter = 0  -- No saturation at center
     AND pixelFlags_bad = 0              -- No bad pixels

Additional quality filters.

.. code-block:: sql

   AND pixelFlags_crCenter = 0            -- No cosmic ray at center
   AND pixelFlags_interpolatedCenter = 0  -- No interpolation at center
   AND pixelFlags_suspectCenter = 0       -- No suspect pixels at center

Calibration stars: If specifically selecting or excluding calibration stars, use ``calib_*`` flags (including ``calib_psf_used`` and ``calib_psf_reserved``), but note DP1 caveats (:ref:`calibration-flags`).

.. _flags-forced-source:

ForcedSource table
------------------

Guidance for the application of flags on forced photometry at Object positions on single-epoch images.

.. code-block:: sql

   WHERE psfFlux_flag = 0                -- PSF flux succeeded
     AND pixelFlags_saturatedCenter = 0  -- No saturation at forced position
     AND pixelFlags_edge = 0             -- Position not on edge
     AND invalidPsfFlag = 0              -- PSF model valid

If using difference image flux.

.. code-block:: sql

   AND psfDiffFlux_flag = 0              -- Difference flux succeeded
   AND diff_PixelFlags_nodataCenter = 0  -- Difference image has coverage

Light curve usage: When constructing light curves, apply these flags to each measurement (row) individually.
This filters out poor-quality epochs while retaining good measurements for the same object across other visits.

.. _flags-dia-source:

DiaSource table
---------------

Guidance for the application of flags on transient/variable detections on difference images.


High-confidence real astrophysical transients.

.. code-block:: sql

   WHERE isDipole = 0                    -- Not a subtraction dipole artifact
     AND psfFlux_flag = 0                -- Difference flux succeeded
     AND pixelFlags_edge = 0             -- Not on edge
     AND pixelFlags_saturatedCenter = 0  -- No saturation
     AND pixelFlags_bad = 0              -- No bad pixels

Additional quality filters.

.. code-block:: sql

   AND centroid_flag = 0  -- Position reliable
   AND pixelFlags_cr = 0  -- Not a cosmic ray residual

.. _flags-dia-forced:

ForcedSourceOnDiaObject table
------------------------------

Guidance for the application of flags on forced photometry at DiaObject positions on _difference_ images.


.. code-block:: sql

   WHERE psfDiffFlux_flag = 0              -- Difference flux succeeded
     AND diff_PixelFlags_nodataCenter = 0  -- Difference image has coverage
     AND pixelFlags_saturatedCenter = 0    -- No saturation
     AND invalidPsfFlag = 0                -- PSF valid

Apply these filters when building DiaObject light curves from forced photometry on difference images.
Similar to ForcedSource, filter per-measurement to remove bad epochs while keeping good ones.

Guidance for the application of flags on forced photometry at DiaObject positions on _science_ images.


.. code-block:: sql

   WHERE psfFlux_flag = 0                  -- Science image flux succeeded
     AND pixelFlags_bad = 0                -- No bad pixels
     AND pixelFlags_saturatedCenter = 0    -- No saturation
     AND invalidPsfFlag = 0                -- PSF valid

Apply these filters when building DiaObject light curves from forced photometry on science images.
Similar to ForcedSource, filter per-measurement to remove bad epochs while keeping good ones.
