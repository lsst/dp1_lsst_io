.. _citedp1:

##########################
How to cite Data Preview 1
##########################

For general information, see `how to cite Rubin Observatory <https://rubinobservatory.org/for-scientists/documentation/cite>`_.


DOI and publications
====================

When citing this data release please reference the data release paper: |dp1_paper|.

When asked to cite the DP1 dataset as a whole please use:

|dataset_doi|

If you only use a specific subset, such as only querying the Objects catalog or only using the deep coadd images, you may cite the DOI explicitly assigned to that subset.
Each individual page in :ref:`products` includes the relevant DOI.

Bibtex
------

Find ``bibtex`` entries for all DOI in `the LSST texmf package <https://github.com/lsst/lsst-texmf/blob/main/texmf/bibtex/bib/lsst.bib>`_.


Telescope and instrument
------------------------

For AAS publications please refer to the `facility <https://journals.aas.org/facility-keywords/>`_ as "Rubin:Simonyi" and for DP1 use "Rubin:Simonyi (LSSTComCam)".
The `Minor Planet Center <https://minorplanetcenter.net/iau/lists/ObsCodesF.html>`_ has allocated the telescope code X05.

The instrument itself can be formally cited as

|comcam_doi|

and that page includes additional references describing the camera.


How to refer to single objects from DP1 data
============================================

If you are referring to individual sources or objects from the Data Preview 1 catalogs, please use the naming convention described here, which has been registered with the International Astronomical Union (IAU) and was developed following `IAU specifications <https://cdsweb.u-strasbg.fr/Dic/iau-spec.html>`_.
All designations should begin with "LSST-DP1" (denoting the Legacy Survey of Space and Time, Data Preview 1), followed by a string that specifies which table the object was obtained from.
These strings should be "O" (for the ``Object`` table), "S" (``Source``), "DO" (``DiaObject``), "DS" (``DiaSource``), or "SSO" (``SSObject``).
Following this table identifier, the (18-digit for all tables except ``SSObject``, for which the ID is 17 digits long) unique numeric identifier from the specified table (i.e., the ``objectId``, ``sourceId``, ``diaObjectId``, ``diaSourceId``, or ``ssObjectId``) should be included.
The "fields" of the identifier should be separated by dashes, so that the designation appears like "LSST-DP1-TAB-123456789012345678."
To summarize, here are examples for objects from each table:

* ``Object``: LSST-DP1-O-609788942606161356 (for ``objectId`` 609788942606161356)
* ``Source``: LSST-DP1-S-600408134082103129 (for ``sourceId`` 600408134082103129)
* ``DiaObject``: LSST-DP1-DO-609788942606140532 (for ``diaObjectId`` 609788942606140532)
* ``DiaSource``: LSST-DP1-DS-600359758253260853 (for ``diaSourceId`` 600359758253260853)
* ``SSObject``: LSST-DP1-SSO-21163611375481943 (for ``ssObjectId`` 21163611375481943)

All catalog entries reported in DP1 tables will have at least one of these five types of IDs.
Refer to the following list for the identifier in each of the remaining tables that are provided with DP1:

* ``ForcedSource``: ``objectId``
* ``ForcedSourceOnDiaObject``: ``diaObjectId``
* ``SSSource``: ``diaSourceId`` or ``ssObjectId``
* ``MPCORB``: ``ssObjectId``

Reporting data to external systems
==================================

When reporting discoveries or followup information from DP1 to external archives and messaging mechanisms
(e.g., the IAU Transient Name Service (``https://www.wis-tns.org/``),
please remember to use "LSSTComCam" as the instrument name and "Rubin:Simonyi"
(or just "Rubin" if that's not available) as the observatory/facility/telescope name,
and please look for an option to report filters as "LSST" and not "Sloan", despite the similarity in photometric systems.

If you encounter a service where these metadata options are not yet available,
we ask that you bring this to our attention;
a post on the "Support" category on https://community.lsst.org/ would be very much appreciated.
