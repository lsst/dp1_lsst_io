.. _moving-drp:

####################################
Solar System data release processing
####################################

In addition to the prompt processing that will be performed on a daily basis, re-processing of the data will be performed annually to produce the Data Release data products.

The :doc:`/processing/moving/ss_prompt` products for Solar System objects will include single visit images, difference images, catalogs of sources detected in difference images (``DiaSources``) and detected objects that are associated with Solar System objects (``SSObjects``), which will include all data collected by the survey to date and will be entered into the Prompt Products database and made available in near real time.
One exception to the use of all survey data to date for the near real time data releases, however, is the Alert Production pipeline that limits the  ``DiaSource`` history for all variability parameters within the alert packets to a 12-month period.

The roughly annual Data Release data products for Solar System objects will include high-fidelity re-processing of all catalogs derived from re-reductions of all survey data using improved calibrations and a single, well-characterized, software release.
In addition, the Data Release data products will include an LSST catalog of Solar System objects that will be suitable for population studies of objects detected by LSST with orbits estimated using only LSST data; this catalog will not rely on association of known objects using MPC orbit predictions.

In contrast to the Prompt Products database, which is updated continuously during observing, the Data Release database is static and will not change after release.
In general, the Data Release data products are best for purposes such as large-scale Solar System population studies and model debiasing, while the Daily (Prompt) data products are most useful for efforts such as follow-up and characterization of Solar System objects as they are detected by the survey.
