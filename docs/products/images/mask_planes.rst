.. _images-mask-planes:

###########
Mask planes
###########

In the LSST Science Pipelines, each processed image includes not only the measured flux values but also a companion bit mask image that records the condition of every pixel.
These mask planes encode information about detector defects, cosmic rays, saturation, missing data, and other effects that influence data quality.
Each named mask plane corresponds to a specific bit flag that can be set independently or in combination with others on a given pixel.

The following table provides a summary.

.. list-table::
   :header-rows: 1
   :widths: 14 8 10 8 10 14 36

   * - **Mask Plane**
     - **Visit Bit**
     - **Visit 2ⁿ**
     - **Coadd Bit**
     - **Coadd 2ⁿ**
     - **Image Type**
     - **Description (DP1-specific)**

   * - **BAD**
     - 0
     - 1
     - 0
     - 1
     - visit + coadd
     - Permanently bad pixels, including entire bad amplifiers. Excluded from science use.

   * - **SAT**
     - 1
     - 2
     - 1
     - 2
     - visit + coadd
     - The flux in this pixel was too high to be accurately recorded (its value exceeded the Photon Transfer Curve (PTC) turnoff point). In coadds, it indicates that saturation affected at least part of the stack at this location.

   * - **INTRP**
     - 2
     - 4
     - 2
     - 4
     - visit + coadd
     - Pixel’s value was replaced via interpolation (usually because it was flagged ``BAD``, ``SAT``, or ``CR``). For coadds, the value was interpolated during stacking, or all inputs had this pixel interpolated.

   * - **CR**
     - 3
     - 8
     - 3
     - 8
     - visit + coadd
     - Pixels hit by a cosmic ray; these pixels are interpolated. For coadds, one or more input visits flagged this pixel as a cosmic ray.

   * - **EDGE**
     - 4
     - 16
     - 4
     - 16
     - visit + coadd
     - Region unprocessed due to the convolution kernel footprint extending beyond the image edge.

   * - **DETECTED**
     - 5
     - 32
     - 5
     - 32
     - visit + coadd
     - Pixel footprint belongs to a detected source above threshold. For coadds, the pixel was detected as part of a source footprint on the coadd itself.

   * - **DETECTED_NEGATIVE**
     - 6
     - 64
     - 6
     - 64
     - difference
     - Negative source detection in difference images.

   * - **SUSPECT**
     - 7
     - 128
     - 7
     - 128
     - visit + coadd
     - Pixel above the PTC turnoff but not fully saturated. Not dilated like ``SAT``. Propagates to coadd if a configurable fraction of input visits flagged it as ``SUSPECT``.

   * - **NO_DATA**
     - 8
     - 256
     - 8
     - 256
     - visit + coadd
     - No valid data (chip gap, missing coverage, or failed amplifier).

   * - **VIGNETTED**
     - 9
     - 512
     - 9
     - 512
     - visit + coadd
     - Pixel vignetted by optics; low-weight or low-quality. For coadds, vignetted in all contributing visits.

   * - **STREAK**
     - 10
     - 1024
     - 10
     - 1024
     - difference
     - Linear artifact (satellite trail, diffraction spike).

   * - **CLIPPED**
     - 11
     - 2048
     - 11
     - 2048
     - coadd only
     - At least one input image contributing to this pixel was identified as an artifact and excluded.

   * - **CROSSTALK**
     - 12
     - 4096
     - 12
     - 4096
     - visit + coadd
     - Pixel affected by electronic crosstalk from a bright source in another amplifier. For coadds, one or more inputs flagged this pixel as affected by crosstalk.

   * - **INEXACT_PSF**
     - 13
     - 8192
     - 13
     - 8192
     - coadd only
     - The PSF at this pixel is ill-defined or varies significantly across inputs. When set, this flag is accompanied by at least one of ``SENSOR_EDGE``, ``CLIPPED``, or ``REJECTED``.

   * - **ITL_DIP**
     - 16
     - 65536
     - 14
     - 16384
     - visit + coadd
     - "ITL dip" artifact: dark vertical trails from bright sources on ITL CCDs. For coadds, one or more input images flagged this pixel as affected.

   * - **NOT_DEBLENDED**
     - 17
     - 131072
     - 15
     - 32768
     - visit + coadd
     - Pixel in a source footprint that was not deblended.

   * - **REJECTED**
     - 18
     - 262144
     - 16
     - 65536
     - coadd only
     - Pixel where a contributing image was masked and not used.

   * - **SENSOR_EDGE**
     - 20
     - 1048576
     - 17
     - 131072
     - coadd only
     - Pixel lies within a margin near the edge of at least one contributing input image.

   * - **UNMASKEDNAN**
     - 21
     - 2097152
     - 18
     - 262144
     - visit + coadd
     - Pixel contains NaN without other masks; indicates invalid data.

   * - **INJECTED**
     - 14
     - 16384
     - —
     - —
     - visit only
     - Pixels with synthetic sources injected for testing or validation.

   * - **INJECTED_TEMPLATE**
     - 15
     - 32768
     - —
     - —
     - difference
     - Pixels with synthetic sources injected into template images (for difference image analysis).

   * - **SAT_TEMPLATE**
     - 19
     - 524288
     - —
     - —
     - difference
     - Pixel saturated in the template used for difference imaging.

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
