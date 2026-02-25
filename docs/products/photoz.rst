.. _products_photoz:

#################
Photo-z estimates
#################

As documented in the SIT-Com tech note "Initial studies of photometric redshifts with LSSTComCam from DP1"
(`SITCOMTN-154 <https://sitcomtn-154.lsst.io/>`_),
members of the Rubin Commissioning Science Unit for photometric redshifts have generated photo-z estimates for every galaxy in DP1.

Access to these photo-z estimates from the Rubin Science Platform is available via the :ref:`products_lsdb` and the :ref:`products_photoz_pzserver`.


.. _products_photoz_pzserver:

Photo-z Server
==============

The `LSST Photo-z Server <https://pzserver.linea.org.br/>`_ is an online service complementary to the Rubin Science Platform (RSP).
It hosts and produces photometric redshift–related lightweight data products and provides tools for data management, sharing, and provenance tracking.
Access is granted using RSP credentials.
See the Photo-z Server `User Guide <https://docs.linea.org.br/en/sci-platforms/pz_server.html>`_ for instructions on how to use it.

The DP1 :doc:`/products/catalogs/object` catalog is available as input data for the **Training Set Maker** pipeline.
A comprehensive collection of **Reference Redshift Catalogs** (mostly spectroscopic) from the literature is also available for users to build customized training sets.

A dedicated `documentation page <https://data.linea.org.br/en/sci_products/pzserver.html>`_ includes links to datasets curated by the Photo-z Server administrators, such as the DP1 preliminary photo-z data products described in `SITCOMTN-154 <https://sitcomtn-154.lsst.io/>`_ (see Appendix B.2 for details on accessing these datasets via the Photo-z Server).


