.. _images-visit-mask-planes:

Visit and Difference Image Mask Planes
======================================

The following are the pixel mask bit planes defined in visit and difference images in Data Preview 1 (DP1). Each plane represents a specific per-pixel condition flagged during image processing. Multiple flags may be set on the same pixel simultaneously.

BAD
    Pixel marked as bad – e.g. known defective pixel or column, or part of a bad amplifier region.
    These pixels are identified via detector defect maps or instrument signature removal and flagged
    as BAD. They are typically interpolated over in processing.

CLIPPED
    Pixel that was clipped during coaddition – i.e. at least one input image for this pixel was
    identified as an artifact and excluded.
    *Usage:* This plane is primarily relevant to coadds; in single-visit images it will normally
    be unset (zero) for all pixels. In deep coadds, ``CLIPPED`` is set when transient artifacts like
    satellite trails or cosmic rays were detected via difference imaging and omitted from the stack.

CR
    Pixel hit by a cosmic ray. Identified by the cosmic-ray detection algorithm
    during single-frame processing; such pixels are flagged ``CR`` and typically interpolated over.

CROSSTALK
    Pixel affected by electronic crosstalk from a bright source in another amplifier. Flagged
    during instrument signature removal (ISR) when crosstalk correction is applied. After subtracting
    the crosstalk ghost, the affected pixel is labeled with ``CROSSTALK``.

DETECTED
    Pixel that is part of a detected source in this exposure. All pixels above the detection threshold
    belonging to a source footprint are flagged as ``DETECTED``.

DETECTED_NEGATIVE
    Pixel that is part of a negative source detection. This is used in image difference contexts
    (for detecting disappearances or negative flux transients). In DP1 static visit images, this
    plane is generally not used (no negative detections are run), but it is defined for compatibility
    with difference imaging.

EDGE
    Pixel on the edge of the sensor or image. This typically marks regions at the periphery of the
    CCD near the edge of the detector, where astrometry/photometry may be unreliable due to e.g.,
    edge distortion effects.

INEXACT_PSF
    Pixel where the PSF is ill-defined or inexact. This is used mainly on coadds: it flags pixels
    for which the effective PSF model is not well-defined because different input images contribute
    to different parts of the coadd image. Whenever ``INEXACT_PSF`` is set, it is accompanied by at least
    one of the descriptive flags (``SENSOR_EDGE``, ``REJECTED``, or ``CLIPPED``) that explain the cause.
    In single-visit images, it remains in the mask schema for coadd usage).

INJECTED
    Pixel containing an injected synthetic source in the science exposure. This plane is used when
    artificial sources are added to images for testing or calibration. Any pixel whose value was
    modified by inserting a simulated source gets the ``INJECTED`` bit.
    DP1’s official processing did not inject extra sources into visit images, so this will be unset
    for most DP1 data.

INJECTED_TEMPLATE
    Pixel containing an injected synthetic source in the template image. Used in difference imaging:
    if a source was artificially added to the template coadd, those template-contributed pixels in
    the science image’s difference would get this flag.

INTRP
    Interpolated pixel – this pixel’s value was replaced via interpolation (usually because it was
    flagged ``BAD``, ``SAT``, or ``CR``). After interpolation, the pipeline sets the ``INTRP`` bit to indicate the
    value is not original data. For example, saturated cores and cosmic ray hits that have been
    patched will have both their original flag (``SAT`` or ``CR``) and ``INTRP`` set.

ITL_DIP
    Pixel in a region affected by the “ITL dip” artifact. This is a vendor-specific detector effect
    seen in ITL CCDs (like those in LSSTComCam) where very bright stars cause a vertical dark
    trail (a drop in measured flux extending up/down along the column).
    The pipeline identifies these trails in ISR and masks them. Pixels along such a trail are flagged
    with ITL_DIP.

NOT_DEBLENDED
    Pixel in a source footprint that was not deblended. If a detected object was too large,
    too close to an image edge, or had too high a fraction of masked pixels, the deblender may skip it.
    In that case the entire footprint is flagged ``NOT_DEBLENDED``.
    For example, very bright stars or crowded cores that the deblender could not separate
    will have this mask.

NO_DATA
    Pixel with no valid data in this exposure.
    In single-visit images this can occur if a pixel falls
    outside the illuminated area or within a sensor artifact so severe that no data value is present.
    On coadds, ``NO_DATA`` is common in areas not covered by any input image.
    In general, ``NO_DATA`` indicates that the pixel should be ignored in analysis (not observed).

REJECTED
    Pixel where a contributing image was masked and not used. On coadds, this flags pixels where one
    or more input exposures had the pixel masked (e.g. ``BAD`` or ``SAT``) and thus that pixel’s coadd value
    comes from fewer images. Many ``REJECTED`` pixels are those falling on a sensor defect or bad column
    that persisted through single-frame processing.
    In single-visit images, this is generally not used (since “rejection” happens during
    coaddition), though the plane exists in the mask schema.

SAT
    Saturated pixel.
    The pixel’s value exceeded the Photon Transfer Curve (PTC) turnoff point — the threshold at which the detector
    begins to deviate from linearity and blooming starts. Pixels above this threshold are flagged as ``SAT``.
    In DP1 visit image processing, the ``SAT`` mask is **dilated** slightly to ensure bleed trails from
    saturated stars are fully masked, covering adjacent pixels that may be affected by charge blooming.
    In coadds, ``SAT`` is only set if a **configurable fraction of input visits** contributing to the coadd
    had the ``SAT`` bit set at that pixel. If too few inputs were saturated, the ``SAT`` bit is not propagated
    to the coadd mask.
    For comparison, the ``SUSPECT`` bit is also set above the PTC turnoff but **not dilated** — it flags
    pixels likely affected by saturation without meeting the criteria for full saturation.


SAT_TEMPLATE
    Pixel that corresponds to a saturated pixel in the template image.
    This is used in difference imaging: if the static sky template had a saturation at this location, the difference image flags it
    as ``SAT_TEMPLATE`` (to distinguish from saturation in the new science exposure).
    This helps avoid false detections or mis-estimation in difference images.
    Not used in standalone visit images; relevant in DP1 difference image products.

SENSOR_EDGE
    Pixel near a sensor’s edge or image boundary where coverage/data are incomplete.
    In coaddition, ``SENSOR_EDGE`` is set on pixels that lie close to the edge of at least one input image.
    Any object whose footprint touches such an area will get a flag indicating potential PSF issues.
    Essentially, ``SENSOR_EDGE`` marks regions of a coadd that were not fully covered by all exposures.
    In single visits, the entire image is one sensor, so ``SENSOR_EDGE`` would typically mark the outer
    few pixels if used (though ``EDGE`` serves a similar purpose).

STREAK
    Pixel in a linear streak region — typically from satellites, aircraft, or occasionally
    diffraction spikes. The ``STREAK`` mask is applied during the ``detectAndMeasureDiaSources``
    stage of difference imaging. Pixels are flagged ``STREAK`` when linear features are detected
    inside ``DETECTED`` regions of the difference image, usually via Hough transform.
    Once a streak is identified, the masked region is extended across
    the full detector column or row to cover the artifact completely.
    This mask is persisted in DP1 visit images, and any ``diaSource`` overlapping the streak region
    will have the ``pixelFlag_streak`` and/or ``pixelFlag_streakCenter`` catalog flags set accordingly.
    Although the same streak detection algorithm is available for the coadd pipeline, it was not enabled
    for DP1 coadd processing, and the `STREAK` mask plane is therefore only relevant in visit images
    for this release.

SUSPECT
    Pixel that is suspicious — likely affected by blooming, non-linearity, or readout effects —
    but not fully saturated. The ``SUSPECT`` bit is set for pixels above the PTC turnoff
    (i.e., where the detector begins to deviate from linear response), just like ``SAT``.

    However, unlike ``SAT``, the ``SUSPECT`` mask is **not dilated**. It flags only those pixels
    directly above the threshold, without extending to surrounding regions. This means ``SUSPECT``
    pixels are typically on the shoulders or flanks of saturated regions, where flux is high
    but blooming is not yet strong enough to trigger the ``SAT`` dilation.

    In coadds, the ``SUSPECT`` bit is only set if a configurable fraction of the contributing
    input images had this bit set for the same pixel.


UNMASKEDNAN
    Pixel value is a NaN (Not-a-Number) that was not originally masked. This flags any pixels that
    turned into NaNs during processing. If a pixel ends up with an undefined value (NaN) and no other
    mask bit set, the pipelines will set the ``UNMASKEDNAN`` plane for that pixel. This alerts the user
    that the pixel has invalid data. Such cases are rare and typically indicate a processing error
    or division-by-zero in calibration.

VIGNETTED
    Pixel in a vignetted region of the sensor. This means the pixel is significantly darkened by
    the optical vignetting (for example, at the very edge of the field of view where the camera’s
    optics or filter holder obscures light). Such pixels receive the ``VIGNETTED`` flag.
    Effectively, these areas have much lower exposure and are often excluded from analysis.
    By default, extremely vignetted sources are not deblended.
