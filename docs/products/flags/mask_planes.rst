.. _flag-mask-planes:

####################################
Connection to image mask planes
####################################

Catalog ``pixelFlags_*`` columns are directly derived from :ref:`image mask planes <images-mask-planes>`.
Each mask plane bit in the image (``BAD``, ``SAT``, ``CR``, ``INTRP``, ``EDGE``, etc.) propagates to a corresponding pixel flag in the catalog.

The key mask plane to flag mappings are listed in the table below.

.. list-table::
   :header-rows: 1
   :widths: 20 25 55

   * - Mask Plane
     - Catalog Flag
     - Notes
   * - SAT
     - ``pixelFlags_saturated``
     - Saturated pixels.
   * - CR
     - ``pixelFlags_cr``
     - Cosmic rays (interpolated in final images).
   * - INTRP
     - ``pixelFlags_interpolated``
     - Interpolated pixels (from CRs, defects, saturation).
   * - EDGE
     - ``pixelFlags_edge``
     - Image edge (single exposures).
   * - SENSOR_EDGE
     - ``pixelFlags_sensor_edge``
     - Detector boundaries (coadds).
   * - BAD
     - ``pixelFlags_bad``
     - Known bad pixels (detector defects).
   * - SUSPECT
     - ``pixelFlags_suspect``
     - Suspect pixels (near saturation).
   * - NO_DATA
     - ``pixelFlags_nodata``
     - No data available.
   * - CLIPPED
     - ``pixelFlags_clipped``
     - Outlier rejection during coaddition.
   * - REJECTED
     - (propagates to CLIPPED)
     - Input visit excluded during coaddition.

Footprint vs center: Flags without ``Center`` suffix are set if any pixel in the source footprint has that mask bit.
``Center`` flags are set only if a pixel in the central 3x3 box has that bit.
For quality filtering, center flags are typically more important since they affect core photometry.

See :ref:`images-visit-mask-planes` and :ref:`images-deep-coadd-mask-planes` for detailed mask plane descriptions.
