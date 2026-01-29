.. _images-deep-coadd-mask-planes:

Deep and Template Coadd Mask Planes
===================================

This page documents the mask planes used in deep coadd template coadd images in Data Preview 1 (DP1).
Each plane corresponds to a bit in the coadd mask and reflects the propagation or summary of pixel conditions from contributing single-visit exposures.

``BAD``
    Pixel is flagged as bad in one or more input exposures.
    The ``BAD`` flag is set if all contributing inputs had the pixel marked bad or if the coadd inherited a bad status for that location.
    Typically, ``BAD`` pixels on the coadd correspond to known defects where no usable inputs remained.
    These often appear alongside ``NO_DATA`` in deeply masked regions.

``CLIPPED``
    Pixel was excluded during coaddition due to artifact clipping -- i.e. at least one input image for this pixel was identified as an artifact and excluded.
    The coaddition algorithm in DP1 aggressively rejects transient features such as cosmic rays, meteors, or satellite trails.

``CR``
    One or more input visits flagged this pixel as a cosmic ray.
    That input’s contribution is rejected, but other clean exposures may still contribute.
    ``CR`` indicates cosmic ray activity in the input stack at this location.

``CROSSTALK``
    At least one input exposure marked this pixel as affected by crosstalk.
    As with ``CR``, other clean visits may contribute.
    ``CROSSTALK`` serves as a provenance indicator for masked artifacts.

``DETECTED``
    Pixel was detected as part of a source footprint on the coadd itself.
    This is set after coaddition when sources are measured on the final stacked image.
    All pixels in detected footprints are flagged ``DETECTED``.

``DETECTED_NEGATIVE``
    Used in :ref:`difference images <images-difference-image>` only, see the :ref:`visit and difference image <images-visit-mask-planes>` page.

``EDGE``
    Pixel lies near the nominal edge of an input image.
    In practice, coadds use ``SENSOR_EDGE`` for meaningful edge marking.
    The ``EDGE`` bit is retained for compatibility but less relevant than in visit images.

``INEXACT_PSF``
    The PSF at this pixel is ill-defined or varies significantly across inputs.
    This usually occurs at patch boundaries or regions with partial input coverage.
    When set, ``INEXACT_PSF`` is always accompanied by at least one of ``SENSOR_EDGE``, ``CLIPPED``, or ``REJECTED`` flags.

``INTRP``
    Pixel value was interpolated during stacking, or all inputs had this pixel marked interpolated.
    If only interpolated pixels contributed at this location, the coadd propagates ``INTRP``.
    This is rare in coadds but possible in narrow masked regions.

``ITL_DIP``
    One or more input images flagged this pixel as affected by the ITL “dip” artifact.
    This dark trail appears on some ITL CCDs due to bright stars.
    ``ITL_DIP`` in coadds marks locations where dips were flagged in the visit images and may help interpret masked vertical artifacts.

``NOT_DEBLENDED``
    A source footprint on the coadd could not be deblended.
    Large or complex detections, such as stellar halos or crowded galaxies, may skip deblending.
    The entire footprint receives the ``NOT_DEBLENDED`` mask.

``NO_DATA``
    No usable data contributed to this coadd pixel.
    ``NO_DATA`` is common at tract patch edges or in areas not covered by any visit.
    It may also occur where inputs were masked and no valid interpolation was possible.

``REJECTED``
    Pixel where a contributing image was masked and not used.
    On coadds, this flags pixels where one or more input exposures had the pixel masked (e.g. ``BAD`` or ``SAT``) and thus that pixel’s coadd value comes from fewer images.
    Many ``REJECTED`` pixels are those falling on a sensor defect or bad column that persisted through single-frame processing.
    If all inputs rejected this pixel, it may be flagged as ``REJECTED`` and possibly ``NO_DATA``.

``SAT``
    One or more input images had this pixel flagged ``SAT`` (saturated).
    If a configurable fraction of contributing visits flagged it as saturated, the coadd sets ``SAT``.
    This does not mean the coadd pixel itself is saturated, but that saturation affected at least part of the stack at this location.

``SENSOR_EDGE``
    Pixel lies within a margin near the edge of at least one contributing input image.
    This margin is set during warping and coaddition and flags partial or unreliable coverage.
    Objects with pixels in ``SENSOR_EDGE`` regions may have poor PSF modeling or incomplete photometry.

``STREAK``
    Used in :ref:`difference images <images-difference-image>` only, see the :ref:`visit and difference image <images-visit-mask-planes>` page.

``SUSPECT``
    Pixel was flagged as ``SUSPECT`` (likely above the PTC turnoff but not fully saturated) in one or more inputs.
    If a configurable fraction of input visits marked the pixel as ``SUSPECT``, it propagates to the coadd.
    Unlike ``SAT``, ``SUSPECT`` is not dilated, and thus this bit marks only the directly affected pixels.
    It indicates that photometry may be mildly biased due to non-linearity or blooming shoulders.

``UNMASKEDNAN``
    Coadd pixel contains a NaN due to all contributing inputs being invalid or some processing error.
    This is rare and usually indicates a failure to interpolate or combine values properly.
    The ``UNMASKEDNAN`` bit serves as a safety net for unexpected invalid results.

``VIGNETTED``
    Pixel lies in a vignetted region in all contributing visits.
    These areas received significantly less flux due to optical shading near the corners or edge of the field.
    ``VIGNETTED`` pixels may appear at the outer edges of the coadd and usually have lower weight.

