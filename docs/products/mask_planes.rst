.. _products_mask_planes:

###########
Mask planes
###########

In the LSST Science Pipelines, each processed image includes not only the measured flux values but also a companion bit mask image that records the condition of every pixel.
These mask planes encode information about detector defects, cosmic rays, saturation, missing data, and other effects that influence data quality.
Each named mask plane corresponds to a specific bit flag that can be set independently or in combination with others on a given pixel.

The following table provides a summary.

.. list-table::
   :header-rows: 1
   :widths: 15 15 70

   * - **Mask Plane**
     - **Image Type**
     - **Description (DP1-specific)**
   * - **BAD**
     - visit + coadd
     - Permanently bad pixels, including “vampire” pixels (bright defect stealing charge from neighbors). Excluded from science use.
   * - **SAT**
     - visit + coadd
     - Pixel’s value exceeded the Photon Transfer Curve (PTC) turnoff point. In coadds, indicates that saturation affected at least part of the stack at this location.
   * - **INTRP**
     - visit + coadd
     - Pixel’s value was replaced via interpolation (usually because it was flagged ``BAD``, ``SAT``, or ``CR``). For coadds, the value was interpolated during stacking, or all inputs had this pixel interpolated.
   * - **CR**
     - visit + coadd
     - Pixel hit by a cosmic ray. Usually interpolated. For coadds, one or more input visits flagged this pixel as a cosmic ray.
   * - **EDGE**
     - visit + coadd
     - Region unprocessed due to convolution kernel footprint extending beyond the image edge. In practice, coadds use ``SENSOR_EDGE`` for meaningful edge marking.
   * - **DETECTED**
     - visit + coadd
     - Pixel footprint belongs to a detected source above threshold. For coadds, the pixel was detected as part of a source footprint on the coadd itself.
   * - **DETECTED_NEGATIVE**
     - difference imaging
     - Negative source detection in difference images.
   * - **SUSPECT**
     - visit + coadd
     - Pixel above the PTC turnoff but not fully saturated. Not dilated like ``SAT``. Propagates to coadd if a configurable fraction of input visits flagged it as ``SUSPECT``.
   * - **NO_DATA**
     - visit + coadd
     - No valid data (chip gap, missing coverage, or failed amplifier).
   * - **VIGNETTED**
     - visit + coadd
     - Pixels vignetted by optics; low-weight or low-quality data. For coadds, the pixel lies in a vignetted region in all contributing visits.
   * - **STREAK**
     - difference imaging
     - Linear artifact (e.g., satellite trail or diffraction spike).
   * - **CLIPPED**
     - coadd only
     - At least one input image for this pixel was identified as an artifact and excluded.
   * - **CROSSTALK**
     - visit + coadd
     - Pixel affected by electronic crosstalk from a bright source in another amplifier. For coadds, one or more inputs flagged this pixel as affected by crosstalk.
   * - **INEXACT_PSF**
     - coadd only
     - The PSF at this pixel is ill-defined or varies significantly across inputs. When set, this flag is accompanied by at least one of ``SENSOR_EDGE``, ``CLIPPED``, or ``REJECTED``.
   * - **ITL_DIP**
     - visit + coadd
     - “ITL dip” artifact: dark vertical trails from bright sources on ITL CCDs. For coadds, one or more input images flagged this pixel as affected.
   * - **NOT_DEBLENDED**
     - visit + coadd
     - Pixel in a source footprint that was not deblended.
   * - **REJECTED**
     - coadd only
     - Pixel where a contributing image was masked and not used.
   * - **SENSOR_EDGE**
     - coadd only
     - Pixel lies within a margin near the edge of at least one contributing input image.
   * - **UNMASKEDNAN**
     - visit + coadd
     - Pixel contains NaN without other mask; indicates invalid data.
   * - **INJECTED**
     - visit only
     - Pixels with synthetic sources injected for testing or validation.
   * - **INJECTED_TEMPLATE**
     - difference imaging
     - Pixels with synthetic sources injected into template images (for difference image analysis).
   * - **SAT_TEMPLATE**
     - difference imaging
     - Pixel saturated in the template image used for difference imaging.


Visit and difference images
===========================

.. toctree::
   :maxdepth: 1
   :titlesonly:

   visit_image_mask_planes

Deep and template coadds images
===============================

.. toctree::
   :maxdepth: 1
   :titlesonly:

   deep_coadd_mask_planes
