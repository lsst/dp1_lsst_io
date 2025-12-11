.. _images-visit-mask-planes:

Visit and Difference Image Mask Planes
======================================

The following are the pixel mask bit planes defined in visit and difference images in Data Preview 1 (DP1). Each plane represents a specific per-pixel condition flagged during image processing. Multiple flags may be set on the same pixel simultaneously.

``BAD``
    Pixel marked as bad – e.g. known defective pixel or column, or part of a bad amplifier region.
    These pixels are identified via detector defect maps or instrument signature removal and flagged
    as BAD. They are typically interpolated over in processing.

``CLIPPED``
    Used on :ref:`deep coadds <images-deep-coadd>` only; see the :ref:`deep and template coadds mask planes <images-deep-coadd-mask-planes>` page.
    However, this may be back-propagated on visit and difference images in future data releases.

``CR``
    Pixel hit by a cosmic ray.
    Identified by the cosmic-ray detection algorithm during single-frame processing; such pixels are flagged ``CR`` and interpolated over.
    It may also be an indication that neighboring unmasked pixels were affected by a ``CR``, because the algorithm doesn't always catch the whole region affected by a cosmic ray.

``CROSSTALK``
    Pixel affected by electronic crosstalk from a bright source in another amplifier.
    Flagged during instrument signature removal (ISR) when crosstalk correction is applied.
    After subtracting the crosstalk ghost, the affected pixel is labeled with ``CROSSTALK``.

``DETECTED``
    Pixel that is part of a detected source in this exposure.
    All pixels above the detection threshold belonging to a source footprint are flagged as ``DETECTED``.

``DETECTED_NEGATIVE``
    Pixel that is part of a negative source detection.
    This is used in image difference contexts (for detecting disappearances or negative flux transients).
    In DP1 static visit images, this plane is generally not used (no negative detections are run),
    but it is defined for compatibility with difference imaging.

``EDGE``
    Indicates regions near the boundaries of an image that could not be fully processed due to the application of a convolution kernel (typically the PSF-like detection kernel).
    These pixels are masked because the kernel footprint extends beyond the image boundary, making reliable measurements impossible.

``INEXACT_PSF``
    Used on :ref:`deep coadds <images-deep-coadd>` only; see the :ref:`deep and template coadds mask planes <images-deep-coadd-mask-planes>` page.

``INJECTED``
    Pixel containing an injected synthetic source in the science exposure.
    This plane is used when artificial sources are added to images for testing or calibration.
    Any pixel whose value was modified by inserting a simulated source gets the ``INJECTED`` bit.
    DP1’s official processing did not inject extra sources into visit images, so this will be unset for most DP1 data.

``INJECTED_TEMPLATE``
    Pixel containing an injected synthetic source in the template image.
    Used in difference imaging: if a source was artificially added to the template coadd, those template-contributed pixels in the science image’s difference would get this flag.

``INTRP``
    Interpolated pixel – this pixel’s value was replaced via interpolation (usually because it was flagged ``BAD``, ``SAT``, or ``CR``).
    After interpolation, the pipeline sets the ``INTRP`` bit to indicate the value is not original data.
    For example, saturated cores and cosmic ray hits that have been patched will have both their original flag (``SAT`` or ``CR``) and ``INTRP`` set.

``ITL_DIP``
    Pixel in a region affected by the “ITL dip” artifact.
    This is a vendor-specific detector effect seen in ITL CCDs (like those in LSSTComCam) where very bright stars cause a vertical dark trail (a drop in measured flux extending up/down along the column).
    The pipeline identifies these trails in ISR and masks them.
    Pixels along such a trail are flagged with ``ITL_DIP``.

``NOT_DEBLENDED``
    Pixel in a source footprint that was not deblended.
    If a detected object was too large, too close to an image edge, or had too high a fraction of masked pixels, the deblender may skip it.
    In that case the entire footprint is flagged ``NOT_DEBLENDED``.
    For example, very bright stars or crowded cores that the deblender could not separate will have this mask.

``NO_DATA``
    Pixel with no valid data in this exposure.
    In single-visit images this can occur if a pixel falls outside the illuminated area or within a sensor artifact so severe that no data value is present.
    In general, ``NO_DATA`` indicates that the pixel should be ignored in analysis (not observed).

``REJECTED``
    Used on :ref:`deep coadds <images-deep-coadd>` only; see the :ref:`deep and template coadds mask planes <images-deep-coadd-mask-planes>` page.

``SAT``
    Saturated pixel.
    The pixel’s value exceeded the Photon Transfer Curve (PTC) turnoff point — the threshold at which the detector begins to deviate from linearity and blooming starts.
    Pixels above this threshold are flagged as ``SAT``.
    In DP1 visit image processing, the ``SAT`` mask is dilated slightly to ensure bleed trails from saturated stars are fully masked, covering adjacent pixels that may be affected by charge blooming.
    For comparison, the ``SUSPECT`` bit is also set above the PTC turnoff but not dilated — it flags pixels likely affected by saturation without meeting the criteria for full saturation.

``SAT_TEMPLATE``
    Pixel that corresponds to a saturated pixel in the template image.
    This is used in difference imaging: if the static sky template had a saturation at this location, the difference image flags it as ``SAT_TEMPLATE`` (to distinguish from saturation in the new science exposure).
    This helps avoid false detections or mis-estimation in difference images.
    Not used in standalone visit images; relevant in DP1 difference image products.

``SENSOR_EDGE``
    Used on :ref:`deep coadds <images-deep-coadd>` only; see the :ref:`deep and template coadds mask planes <images-deep-coadd-mask-planes>` page.

``STREAK``
    Pixel in a linear streak region — typically from satellites, aircraft, or occasionally diffraction spikes.
    The ``STREAK`` mask is applied during difference imaging.
    Pixels are flagged ``STREAK`` when linear features are detected inside ``DETECTED`` regions of the difference image, usually via Hough transform.
    Once a streak is identified, the masked region is extended across the full detector column or row to cover the artifact completely.

``SUSPECT``
    Pixel that is suspicious — likely affected by blooming, non-linearity, or readout effects — but not fully saturated.
    The ``SUSPECT`` bit is set for pixels above the PTC turnoff (i.e., where the detector begins to deviate from linear response), just like ``SAT``.
    However, unlike ``SAT``, the ``SUSPECT`` mask is not dilated.
    It flags only those pixels directly above the threshold, without extending to surrounding regions.
    This means ``SUSPECT`` pixels are typically on the shoulders or flanks of saturated regions, where flux is high but blooming is not yet strong enough to trigger the ``SAT`` dilation.

``UNMASKEDNAN``
    Pixel value is a NaN (Not-a-Number) that was not originally masked.
    This flags any pixels that turned into NaNs during processing.
    If a pixel ends up with an undefined value (NaN) and no other mask bit set, the pipelines will set the ``UNMASKEDNAN`` plane for that pixel.
    This alerts the user that the pixel has invalid data.
    Such cases are rare and typically indicate a processing error or division-by-zero in calibration.

``VIGNETTED``
    Pixel in a vignetted region of the sensor.
    This means the pixel is significantly darkened by the optical vignetting (for example, at the very edge of the field of view where the camera’s optics or filter holder obscures light).
    Such pixels receive the ``VIGNETTED`` flag.
    Effectively, these areas have much lower exposure and are often excluded from analysis.
    By default, extremely vignetted sources are not deblended.

