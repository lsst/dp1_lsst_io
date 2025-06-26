.. _background:

######################
Background subtraction
######################

The background subtraction algorithms in the LSST Science Pipelines estimate and remove large-scale background signals from science imaging.
Such signals may include sky brightness from airglow, moonlight, scattered light instrumental effects and diffuse astrophysical emission.
In so doing, true astrophysical sources are isolated to allow for accurate detection and measurement.

Overview
========

After [Instrument Signature Removal](https://pipelines.lsst.io/modules/lsst.ip.isr/index.html#lsst-ip-isr), each post-ISR image is processed by the [`CalibrateImageTask`](https://pipelines.lsst.io/modules/lsst.pipe.tasks/tasks/lsst.pipe.tasks.calibrateImage.CalibrateImageTask.html), which performs image characterization, including background subtraction, and produces the preliminary science image, `preliminary_visit_image`, and the associated preliminary background model, `preliminary_visit_image_background`. To generate a background model, each post-ISR image is divided into superpixels of $128\times128$ pixels. Pixels with a mask flag set that indicates that they contain no useful science data or that they contain flux from a preliminary source detection are masked. The iterative $3\sigma$ clipped mean of the remaining pixels is calculated for each superpixel, constructing a background statistics image. A sixth-order Chebyshev polynomial is fit to these values to allow for an extrapolation back to the native pixel resolution of the post-ISR image.

Using `preliminary_visit_image_background` as input, [`ReprocessVisitImageTask`](https://pipelines.lsst.io/v/d_2024_11_01/modules/lsst.drp.tasks/tasks/lsst.drp.tasks.reprocess_visit_image.ReprocessVisitImageTask.html) applies calibration models produced by upstream tasks to the single-visit image. It then performs the final round of source detection, deblending, and measurement that ultimately populate the `source` table. One of the outputs of `ReprocessVisitImageTask` is the refined, final visit-level background model, `visit_image_background`, along with the final background-subtracted visit image, `visit_image`.
