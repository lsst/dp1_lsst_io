.. _portal-201-1:

#################################
201.1. Object table (Coming Soon)
#################################

For the Portal Aspect of the Rubin Science Platform at data.lsst.cloud.

**Data Release:** DP1

**Last verified to run:** *2025-11-05* (Date of the latest revision)

**Learning objective:** Understand the contents of, and how to access, the ``Object`` table.

**LSST data products:** ``Object`` table

**Credit:** Originally developed by the Rubin Community Science team.
Please consider acknowledging them if this tutorial is used for the preparation of journal articles, software releases, or other tutorials.

**Get Support:** Everyone is encouraged to ask questions or raise issues in the `Support Category <https://community.lsst.org/c/support/6>`_ of the Rubin Community Forum.
Rubin staff will respond to all questions posted there.

**INTRODUCTION:** The Object table contains forced measurements in the u g r i z y deep_coadd images at the sky coordinates of every source detected in any individual Visit image, or in a deep_coadd image in any filter, with signal-to-noise ratio ≥ 5.

The Object table contains only deblended objects (the "children" of deblending only, no "parent" objects), and duplicates have been rejected (e.g., objects in the overlapping edges of deep_coadd images).

TAP table name: dp1.Object

----

**1. Log in to the Portal Aspect of the RSP.**

**2. Explore the schema.**

**3. Explore the key columns in the Object table.**

* ObjectID

* Coordinates

* Photometry

Magnitudes 

PSF fluxes

cModel fluxes 

Other extended-object photometry measurements

[f]_sersicFlux: Sersic flux (NED documentation)

[f]_gaap*: GaaP fluxes (Kuijken et al. 2008)

[f]_kronFlux: Kron flux (NED documentation)

[f]_ap*: aperture fluxes (radii; pixels)

Milky Way dust extinction

* HSM Moments

Hirata-Seljak-Mandelbaum (HSM) moments (Hirata & Seljak 2003, Mandelbaum et al. 2005):

shape_xx, _yy, and _xy
[f]_ixx, _iyy, and _ixy
Extendedness (star/galaxy separation)

If the product of the cModel flux and a configurable flux ratio (0.985) is less than the PSF flux, the object is "not extended" (extendedness = 0, or False). If it is greater than the PSF flux, the object is considered "extended" (extendedness = 1, or True)

refExtendedness (extendedness in band refBand)
[f]_extendedness (extendedness in filter [f])
2.2.5. Flags
Pixel flags

A variety of flags indicating whether pixels that are saturated, or affected by cosmic rays, contributed to the object's measurements.

[f]_pixelFlags_*
Measurement flags

The flux and shape measurements mentioned above have associated flag columns suffixed with _flag.

Deblending flags

If the object was deblended from a parent with more than one child, this flag is True:

detect_fromBlend
The objectId of the parent.

parentObjectId
Blendedness flag

A measure of how much the flux is affected by neighbors (1- f_child/f_parent)
This uses the absolute value of the instrumental flux to try to obtain a de-noised value. See section 4.9.11 of Bosch et al. 2018, PASJ, 70.

[f]_blendedness

Descriptions and units
For a subset of the key columns show the table of their descriptions and units.

3. Data access
The Object table is available via the TAP service and the butler.

Recommended access method: TAP.

3.1. Advisory: avoid full-table queries
Avoid full-table queries. Always include spatial constraints.

The Object table is a large, inclusive, union set of measurements made in the deeply coadded images at the locations of all objects detected in any image.

The DP1 data release Object table is relatively small and full-table TAP queries can run in minutes. However, skipping spatial constraints is not a good habit to form, because future data release Object tables will contain billions of rows.

3.2. TAP (Table Access Protocol)
The Object table is stored in Qserv and accessible via the TAP services using ADQL queries.

Include spatial constraints: Qserv stores catalog data sharded by coordinate (RA, Dec), so ADQL query statements that include constraints by coordinate do not requre a whole-catalog search and are typically faster (and can be much faster) than ADQL query statements which only include constraints for other columns. Use either an ADQL cone or polygon search for faster queries (do not use WHERE ... BETWEEN statements to set boundaries on RA and Dec).

3.2.1. Demo query
Define a query to return the nine "key columns" from Section 2.3.

Impose spatial constraints: search within 0.2 degrees of the center of the Extended Chandra Deep Field South (ECDFS) field, RA, Dec =  
53.13, − 28.10 .

query = "SELECT objectId, coord_ra, coord_dec, r_extendedness, r_blendedness, " \
        "r_psfMag, r_psfMagErr, r_cModelMag, r_cModelMagErr " \
        "FROM dp1.Object " \
        "WHERE CONTAINS(POINT('ICRS', coord_ra, coord_dec), " \
        "CIRCLE('ICRS', 53.13, -28.10, 0.2)) = 1 " \
        "ORDER BY coord_ra ASC "
job = service.submit_job(query)
job.run()
job.wait(phases=['COMPLETED', 'ERROR'])
print('Job phase is', job.phase)
if job.phase == 'ERROR':
    job.raise_if_error()

Do the plotting within Portal 

3.2.2. Joinable tables 

The Object table can be joined to the ForcedSource table on the column objectId.

The ForcedSource table contains forced PSF photometry in the processed visit images and difference images at the sky coordinates of every object.

The following query joins the Object and ForcedSource tables.
Columns returned include the object and forcedSource unique identifiers, and the r-band PSF flux from the Object table.
The query is for objects that are within 0.1 degrees of the ECDFS field center, are not extended (are point-like), and have an apparent magnitude 20<r<25 mag.

query = "SELECT o.objectId, o.r_psfFlux " \
        "FROM dp1.Object AS o " \
        "JOIN dp1.ForcedSource AS fs ON o.objectId = fs.objectId " \
        "WHERE CONTAINS(POINT('ICRS', o.coord_ra, o.coord_dec), " \
        "CIRCLE('ICRS', 53.13, -28.10, 0.1)) = 1 " \
        "AND o.refExtendedness = 0 " \
        "AND o.r_psfMag > 20 AND o.r_psfMag < 25 " \
        "ORDER BY o.objectId ASC"
job = service.submit_job(query)
job.run()
job.wait(phases=['COMPLETED', 'ERROR'])
print('Job phase is', job.phase)
if job.phase == 'ERROR':
    job.raise_if_error()
