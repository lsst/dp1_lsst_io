.. _moving:

#############################
Solar System processing (SSP)
#############################

The Solar System processing (SSP) pipeline links together detections of new and known solar system objects,
and interfaces with the Minor Planet Center (MPC) for physical parameter derivation and orbit fitting.


General overview of SSP
=======================

.. toctree::
    :maxdepth: 1
    :titlesonly:
    :glob:

    ss_prompt
    ss_linking
    ss_drp



Solar System processing in DP1
==============================

Solar System processing in DP1 consists of two key components: the association of observations (sources) with known solar system objects, and the discovery of previously unknown objects by linking sets of tracklets, where a tracklet is defined as two or more observations taken in close succesion in a single night.

To generate expected positions for known objects, ephemerides are computed for all objects found in the Minor Planet Center orbit catalog using the ``Sorcha`` survey simulation toolkit (`Merritt et al., in press <https://github.com/dirac-institute/sorcha>`_).
To enable fast lookup of objects potentially present in an observed visit, we use the ``mpsky`` package (M. Juric 2025).
In each difference image resulting from :doc:`/processing/dia/index` processing, the closest ``DIASource`` within 1 arcsecond of a known solar system object’s predicted position is associated to that object.

Solar system object discovery uses the ``heliolinx`` package of asteroid identification and linking tools (`A. Heinze et al. 2023 <https://ui.adsabs.harvard.edu/abs/2023DPS....5540503H/abstract>`_).
The suite consists of the following tasks:

- Tracklet creation with ``make_tracklets``
- Multi-night tracklet linking with ``heliolinc``
- Linkage post processing (orbit fitting, outlier rejection, and de-duplication) with ``link_purify``

The inputs to the ``heliolinx`` suite included all sources detected in difference images produces by an early processing of the LSSTComCam commissioning data, including some that were later rejected as part of DP1 processing and hence are not part of this DP1 release.

Tracklet creation with ``make_tracklets`` used an upper limit angular velocity of 1.5 deg/day, faster than any main belt asteroid and in the range of many NEO discoveries.
To avoid excessive false tracklets from fields that were observed many times per night, the minimum tracklet length was set to three and the minimum on-sky motion for a valid tracklet was set to five arcseconds.

The heart of the discovery pipeline is the ``heliolinc`` task, which connects (“links”) tracklets belonging to the same object over a series of nights.
It employs the HelioLinC3D algorithm (`S. Eggl et al. 2020 <https://ui.adsabs.harvard.edu/abs/2020DPS....5221101E/abstract>`_; `A. Heinze et al. 2022 <https://ui.adsabs.harvard.edu/abs/2022DPS....5450404H/abstract>`_), a refinement of the original HelioLinC algorithm of `M. J. Holman et al. (2018) <https://ui.adsabs.harvard.edu/abs/2018AJ....156..135H/abstract>`_.
The ``heliolinc`` run tested each tracklet with 324 different hypotheses spanning heliocentric distances from 1.5 to 9.8 AU and radial velocities spanning the full range of possible bound orbits (eccentricity 0.0 to nearly 1.0).
This range of distances encompasses all main belt asteroids and Jupiter Trojans, as well as many comets and Mars-crossers and some NEOs.
Smaller heliocentric distances were not attempted here because nearby objects move rapidly across the sky and hence were not likely to remain long enough in an LSSTComCam field to be discovered.
A clustering radius was chosen corresponding to 1.33 × 10−3 AU at 1 AU from Earth.
Linkages produced by ``heliolinc`` are then post-processed with ``link_purify`` into a final non-overlapping set of candidate discoveries, ranked from highest to lowest probability of being a real asteroid based on astrometric orbit-fit residuals and other considerations.



