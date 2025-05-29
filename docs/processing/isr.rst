.. _isr:

############################
Instrument signature removal
############################

The first step in processing LSSTComCam images is to correct for the effects introduced by the telescope and detector. Each sensor and its readout amplifiers can vary slightly in performance, causing images of even a uniformly illuminated focal plane to exhibit discontinu- ities and shifts due to detector effects. The Instrument Signature Removal (ISR) pipeline aims to recover the original astrophysical signal as best as possible and pro- duce science-ready single-epoch images for source detec- tion and measurement.

Figure 8 illustrates the model of detector components and their impact on the signal, tracing the process from photons incident on the detector surface to the final quantized values recorded in the image files. The ISR pipeline essentially “works backward” through the sig- nal chain, correcting the integer analog-to-digital units (ADU) raw camera output back to a floating-point num- ber of photoelectrons created in the silicon. The physi- cal detector, shown on the left in Figure 8, is the source of effects that arise from the silicon itself, such as the dark current and the brighter-fatter effect (A. A. Plazas et al. 2018). After the image has integrated, the charge is shifted to the serial register and read out, which can introduce charge transfer inefficiencies and a clock- injected offset level. The signals for all amplifiers are transferred via cables to the Readout Board (REB), dur- ing which crosstalk between the amplifiers may occur. The Analog Signal Processing Integrated Circuit (AS- PIC) on the REB converts the analog signal from the detector into a digital signal, adding both quantization and a bias level to the image. Although the signal chain is designed to be stable and linear, the presence of nu- merous sources of non-linearity indicates otherwise.

The ISR processing pipeline for DP1 performs: dither- ing, serial overscan subtraction, saturation masking, gain normalization, crosstalk correction, parallel over- scan subtraction, linearity correction, serial charge transfer inefficiency (CTI) correction, image assembly, bias subtraction, dark subtraction, brighter-fatter cor- rection, defect masking and interpolation, variance plan construction, and flat fielding.

.. _isr-tbd:

To be determined
================

*Subsections by signature?*


.. _isr-tbd2:

To be determined2
=================

*Subsections by signature?*
