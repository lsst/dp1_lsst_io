.. _images:

######
Images
######

*High-level descriptions of the processing stage (by name; processing is described elsewhere) that results in these images, and the metadata they come with. Their flux units, etc.*

*For easy navigability try to structure each subsection the same (e.g., overview then pixel data then metadata, or whatever works). OK to make sub-sub-sections.*


.. _images-visit:

Visit images
============

*A visit is one observation of a sky location in one filter.*

*Visit images are fully processed, sky subtracted, and calibrated.*

*The image for one individual detector is called a ``calexp``.*

Pixel data
----------

*Calibrated but not absolutely. Quote units, and how to convert to AB mags.*

Metadata
--------

*Metadata includes PSF, photcalib, WCS, etc.*


.. _images-coadd:

Coadd images
============

*Coadded images are created by combining overlapping visits.*

*Coadded images are made one per filter.*

*The tesselated coadded images are divided into tracts and patches. Quote sizes. Tract is about like the full focal plane and patch is about like a detector.*

*One patch of a coadded image is called a ``deepCoadd``.*

*Metadata includes PSF, photcalib, WCS, etc.*


Cell-based coadds
-----------------

*Remove if they're not done for DP1.*


.. _images-difference:

Difference images
=================

*Content similar to above.*

.. _images-template:

Template images
===============

*Content similar to above.*


.. _images-raw:

Raw images
==========

*Content similar to above.*