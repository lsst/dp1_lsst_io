.. _access:

###########
Data access
###########

The services and tools for accessing the data products.

**Data Policy:** Only Rubin data rights holders may have an account in the Rubin Science Platform (RSP) and access to Data Preview 1.
All scientists and students in the US and Chile, plus named members of international in-kind teams, have Rubin data rights.

`Learn more about the Rubin data policy <https://rubinobservatory.org/for-scientists/data-products/data-policy>`_.


Rubin Science Platform (RSP)
============================

All of the data products are available exclusively through the Rubin Science Platform (RSP).

Get started
-----------

Follow these `instructions to sign up for an RSP account <https://rsp.lsst.io/guides/getting-started/get-an-account.html>`_, then work through the :doc:`/tutorials/index`.

.. _access-getsupport:

Get support
-----------

To ask question and get help with any aspect of the Rubin data products, services, and tools, please post a new topic in the Rubin Community Forum's `Support category <https://community.lsst.org/c/support/6>`_.
Weekly `Rubin Science Assemblies <https://rubinobservatory.org/for-scientists/events-deadlines/events-rsa>`_ offer presentations, hands-on tutorials, and drop-in office hours as live support.


Table Access Protocol (TAP)
---------------------------

A protocol of the IVOA for standardized access to catalog data for discovery, search, and retrieval.
All catalogs and images can be accessed with the TAP service via the RSP's Portal, Notebook, and API aspects.
The Astronomy Query Data Language (ADQL) is commonly used to query data subsets for retrieval, but the Portal also offers a graphical user interface to the TAP service.

.. toctree::
    :maxdepth: 1
    :glob:

    adql_queries


Simple Image Access
-------------------

A protocol of the IVOA for standardized access to image data for discovery, search, and retrieval.
All images can be accessed with the SIA service via the RSP's Portal, Notebook, and API aspects.


Butler
------

Custom Rubin software package for data organization and handling (images and catalogs).
Images and catalogs can be accessed with the Butler via the RSP's Notebook aspect.

.. toctree::
    :maxdepth: 1
    :glob:

    butler_terminology
    name_changes

