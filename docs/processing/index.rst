.. _processing:

###############
Data processing
###############

A high-level overview of the Data Release Processing (DRP) steps which generated the data products.

All processing was done with the `LSST Science Pipelines <https://pipelines.lsst.io/>`_

For details see |dp1_paper|.


.. _processing-isr:

Instrument signature removal (ISR)
==================================

Corrects the raw images for the effects of the telescope and detector.

.. toctree::
    :maxdepth: 1
    :glob:

    isr/index


.. _processing-calibration:

Calibration
===========

Generates the science-ready processed visit images.

.. toctree::
    :maxdepth: 1
    :glob:

    calibration/index


.. _processing-coaddition:

Coaddition
==========

Generates the deep coadd and template images.

.. toctree::
    :maxdepth: 1
    :glob:

    coaddition/index


.. _processing-detection:

Source detection and measurement
================================

Generates the catalogs of measurements for detected sources.

.. toctree::
    :maxdepth: 1
    :glob:

    detection/index


.. _processing-dia:

Difference image analysis
=========================

Runs image substraction to generate difference images and associated detection catalogs.

.. toctree::
    :maxdepth: 1
    :glob:

    dia/index


.. _processing-moving:

Moving objects processing
=========================

Links detected sources into moving objects and generates Solar System catalogs.

.. toctree::
    :maxdepth: 1
    :glob:

    moving/index

