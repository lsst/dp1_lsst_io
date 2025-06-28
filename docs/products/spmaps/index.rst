.. _spmaps:

####################
Survey property maps
####################

Survey-level healsparse property maps.

|survey_property_doi|

Access
======

The survey property maps are accessible via the Butler service.

* :ref:`Dataset type <products_butler_terminology>`\ : ('<map_name>', {**band**, **skymap**}, HealSparseMap)
* Format: `FITS <https://healsparse.readthedocs.io/en/1.9.0/filespec.html#healsparsemap-fits-serialization>`_ (with ``.hsp`` file extension)
* Number of files: |survey_property_butler_count|

Description
===========

Maps in ``HealSparse`` format that aggregate information from the visit images contributing to the ``deep_coadds`` and
summarize key observing conditions and survey characteristics across the sky.

Map types
---------

The map names, descriptions (and units if not dimensionless) are:

* ``deepCoadd_exposure_time_consolidated_map_sum``: Total exposure time accumulated per sky position (second)
* ``deepCoadd_epoch_consolidated_map_min, ...max, ...mean``: Earliest, latest, and mean observation epochs (MJD)
* ``deepCoadd_psf_size_consolidated_map_weighted_mean``: Weighted mean of PSF characteristic width as computed from the determinant radius (pixel)
* ``deepCoadd_psf_e1_consolidated_map_weighted_mean``: Weighted mean of PSF ellipticity component e1
* ``deepCoadd_psf_e2_consolidated_map_weighted_mean``: Weighted mean of PSF ellipticity component e2
* ``deepCoadd_psf_maglim_consolidated_map_weighted_mean``: Weighted mean of PSF flux 5σ magnitude limit (magAB)
* ``deepCoadd_sky_background_consolidated_map_weighted_mean``: Weighted mean of background light level from the sky (nJy)
* ``deepCoadd_sky_noise_consolidated_map_weighted_mean``: Weighted mean of standard deviation of the sky level (nJy)
* ``deepCoadd_dcr_dra_consolidated_map_weighted_mean``: Weighted mean of DCR-induced astrometric shift in right ascension direction, expressed as a proportionality factor
* ``deepCoadd_dcr_ddec_consolidated_map_weighted_mean``: Weighted mean of DCR-induced astrometric shift in declination direction, expressed as a proportionality factor
* ``deepCoadd_dcr_e1_consolidated_map_weighted_mean``: Weighted mean of DCR-induced change in PSF ellipticity (e1), expressed as a proportionality factor
* ``deepCoadd_dcr_e2_consolidated_map_weighted_mean``: Weighted mean of DCR-induced change in PSF ellipticity (e2), expressed as a proportionality factor

Tutorials
---------

See the :ref:`200-level notebook <notebook-200>` or :ref:`200-level portal <portal-200>`
tutorials demonstrating how to access the survey property maps.
