.. _isr:

##################################
Instrument signature removal (ISR)
##################################

ISR removes instrumental effects introduced in the raw images by the telescope and detectors to produce an accurate representation of the incoming light.

For descriptions of the ISR steps and the generation, verification, certification, approval, and distribution of the calibration products necessary for ISR, refer to the paper `Instrument Signature Removal and Calibration Products for the Rubin Legacy Survey of Space and Time <https://ui.adsabs.harvard.edu/abs/2025JATIS..11a1209P/abstract>`_, the "Rubin Baseline Calibration Plan" (`SITCOMTN-086 <https://sitcomtn-086.lsst.io/>`_), and the "Verifying LSST Calibration Data Products" (`DMTN-101 <https://dmtn-101.lsst.io/>`_) and "Calibration Generation, Verification, Acceptance, and Certification" (`DMTN-222 <https://dmtn-222.lsst.io/>`_) technical notes.

ISR is the first step of the image processing which leads to calibrated, science-ready images.

**Users should not attempt to recreate or rerun ISR; it is automatically applied within the LSST Science Pipelines**

The steps of ISR include:

* dithering of digitized counts
* serial overscan subtraction
* masking of saturated and suspect pixels
* gain scaling
* correction of crosstalk in parallel overscan
* parallel overscan subtraction
* correction of crosstalk between amplifiers
* linearity correction
* serial charge transfer inefficiency (CTI) correction
* image assembly and trimming
* bias subtraction
* dark subtraction
* brighter-fatter correction
* defect masking and interpolation
* variance plane construction
* flat fielding


.. figure:: images/isr_model.png
    :width: 600
    :name: isr_model
    :alt: A schematic diagram of a model with various detector signatures relevant for LSSTCam images.

    Figure 1: The model of the detector and readout board (REB) components, labeled with the effects that they impart on signal (from |dp1_paper|).


.. figure:: images/isr_steps.png
    :width: 600
    :name: isr_steps
    :alt: A schematic diagram with Instrument Signature Removal steps relevant for LSSTCam images.

    Figure 2: Instrument Signature Removal steps derived form the detector model in Figure 1 (from `Plazas Malagón et al. 2025 <https://ui.adsabs.harvard.edu/abs/2025JATIS..11a1209P/abstract>`_).


Overview
========

Each sensor and its readout amplifiers can vary slightly in performance, causing images of even a uniformly illuminated focal plane to exhibit discontinuities and shifts due to detector effects.
Figure 1 illustrates the model of detector components and their impact on the signal, tracing the process from photons incident on the detector surface to the final quantized values recorded in the image files.
Based on this model, a series of Instrument Signature Removal steps are implemented to eliminate camera-induced effects (Figure 2).

The ISR pipeline essentially “works backward” through the signal chain, correcting the integer analog-to-digital units (ADU) raw camera output back to a floating-point number of photoelectrons created in the silicon.
The physical detector, shown on the left in Figure 1, is the source of effects that arise from the silicon itself, such as the dark current and the brighter-fatter effect (`Broughton et al. 2024 <https://ui.adsabs.harvard.edu/abs/2024PASP..136d5003B/abstract>`_, `Gruen et al. 2015 <https://ui.adsabs.harvard.edu/abs/2015JInst..10C5032G/abstract>`_).

After the image has integrated, the charge is shifted to the serial register and read out, which can introduce charge transfer inefficiencies and a clock-injected offset level.
The signals for all amplifiers are transferred via cables to the Readout Board (REB), during which crosstalk between the amplifiers may occur.
The Analog Signal Processing Integrated Circuit (ASPIC) on the REB converts the analog signal from the detector into a digital signal, adding both quantization and a bias level to the image.
Although the signal chain is designed to be stable and linear, the presence of numerous sources of non-linearity reveals its complexity.

Following this model, the sequence of ISR corrections is carefully structured to reverse the detector and electronics effects in the order opposite to their introduction.
For example, quantization artifacts are addressed first through dithering and differential non-linearity correction, followed by serial overscan subtraction, saturation masking, and gain normalization.
Crosstalk is then corrected to prevent its contamination of later steps like parallel overscan subtraction and linearity correction.
CTI is corrected next, just before assembling the amplifier segments into full CCD images.
The final steps include bias and dark subtraction, brighter-fatter effect correction, defect masking, variance plane construction, and flat-fielding.
Each of these steps is tied to specific elements in the detector readout chain, and their ordering ensures that each correction builds upon a cleaner, more physically meaningful image (`Plazas Malagón et al., 2025 <https://ui.adsabs.harvard.edu/abs/2025JATIS..11a1209P/abstract>`_).
