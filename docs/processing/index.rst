.. _processing:

###############
Data processing
###############

A high-level overview of the Data Release Processing (DRP) steps which generated the data products.

All processing was done with the `LSST Science Pipelines <https://pipelines.lsst.io/>`_.

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

Generates catalogs of detected sources and measurements of their properties.

.. toctree::
    :maxdepth: 1
    :glob:

    detection/index


.. _processing-dia:

Difference image analysis
=========================

Runs image subtraction to generate difference images and associated detection catalogs.

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

Pipeline graphs
===============

To help visualize the DRP steps, the pipeline graphs below illustrate data products (gray boxes) and Pipeline Tasks (teal boxes).
They are divided into "stages" such that each stage finishes with all the analysis needed to vet it and move onto the next one.
For simplicity, all DRP tasks designed to compute metrics and make plots are omitted.

.. note::
    Not every data product shown is part of DP1!
    These pipeline graphs are a representation of most tasks in the LSSTComCam DRP pipeline at the time DP1 was processed.
    They illustrate how different data products and tasks relate to one another, and are not a definitive record of all processing steps performed.

.. figure:: DP1-stage1-figure.pdf
  :width: 400
  :alt: Pipeline graph of DP1 DRP stage1, showing single visit processing steps

  Stage 1 is ISR, preliminary single-detector calibrations, and analysis on those (which includes matching across visits).

.. figure:: DP1-stage2-figure.pdf
  :width: 400
  :alt: Pipeline graph of DP1 DRP stage2, showing recalibration steps

  Stage 2 is multi-visit and full-visit recalibration.

.. figure:: DP1-stage3-figure.pdf
  :width: 400
  :alt: Pipeline graph of DP1 DRP stage3, showing coaddition steps

  Stage 3 is coaddition and coadd processing, which results in the object table.

..
    .. figure:: DP1-stage4-figure.pdf
    :width: 400
    :alt: Pipeline graph of DP1 DRP stage4, showing variability measurement steps

    Stage 4 uses information from stage 3 to create visit-level final source catalogs and do difference imaging and forced photometry.