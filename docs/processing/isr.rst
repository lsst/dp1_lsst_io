.. _isr:

############################
Instrument signature removal
############################

The first step in processing LSSTComCam images is to correct for the effects introduced by the telescope and detector. Each sensor and its readout amplifiers can vary slightly in performance, causing images of even a uniformly illuminated focal plane to exhibit discontinuities and shifts due to detector effects. The Instrument Signature Removal (ISR) pipeline aims to recover the original astrophysical signal as best as possible and produce science-ready single-epoch images for source detection and measurement.

Figure 1 illustrates the model of detector components and their impact on the signal, tracing the process from photons incident on the detector surface to the final quantized values recorded in the image files. The ISR pipeline essentially “works backward” through the signal chain, correcting the integer analog-to-digital units (ADU) raw camera output back to a floating-point number of photoelectrons created in the silicon. The physical detector, shown on the left in Figure 1, is the source of effects that arise from the silicon itself, such as the dark current and the brighter-fatter effect (Gruen et al. 2018).

After the image has integrated, the charge is shifted to the serial register and read out, which can introduce charge transfer inefficiencies and a clock-injected offset level. The signals for all amplifiers are transferred via cables to the Readout Board (REB), during which crosstalk between the amplifiers may occur. The Analog Signal Processing Integrated Circuit (ASPIC) on the REB converts the analog signal from the detector into a digital signal, adding both quantization and a bias level to the image. Although the signal chain is designed to be stable and linear, the presence of numerous sources of non-linearity indicates otherwise.

.. figure:: images/detector_signature.png
    :width: 600
    :name: detector_signature
    :alt: A schematic diagram of various detector signatures relevant for LSSTCam images.

    Figure 1: The model of the detector and readout board (REB) components, labeled with the effects that they impart on signal.

The ISR processing pipeline for DP1 performs: dithering, serial overscan subtraction, saturation masking, gain normalization, crosstalk correction, parallel overscan subtraction, linearity correction, serial charge transfer inefficiency (CTI) correction, image assembly, bias subtraction, dark subtraction, brighter-fatter correction, defect masking and interpolation, variance plan construction, and flat fielding.
