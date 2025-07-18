#! /usr/bin/env python

"""Split an bibtex file containing multiple entries into one file per
relevant DOI.

Assumes only the entries for a single data release are in the dois.bib file.
Writes multiple file to a docs/bib/ directory using standard naming convention.
"""

from pybtex.database import BibliographyData, Entry
import os.path


def write_bib(entry: Entry, root: str) -> None:
    outfile = f"docs/bib/{root}.bib"
    if os.path.exists(outfile):
        raise RuntimeError(f"Unexpected reuse of bib root {root}")
    with open(outfile, "w") as fd:
        print(entry.to_string("bibtex"), file=fd)


with open("dois.bib") as fd:
    bib = BibliographyData.from_string(fd.read(), "bibtex")


outdir = "docs/bib"
for entry in bib.entries.values():
    title = entry.fields["title"].replace("{", "").replace("}", "")
    if not title.startswith("Legacy Survey of Space and Time Data"):
        # Not a dataset DOI.
        continue

    if ":" not in title:
        # Primary DOI.
        write_bib(entry, "dataset")
        continue

    _, dataset_type = title.split(":")
    dataset_type = dataset_type.removesuffix("[Data set]")
    dataset_type = dataset_type.strip()
    dataset_type = dataset_type.replace("\\", "")
    if dataset_type.endswith("dataset type"):
        # Butler.
        butler_type = (
            dataset_type.removesuffix("dataset type").strip().replace(" ", "-")
        )
        write_bib(entry, "butler-" + butler_type)
    elif dataset_type.endswith("searchable catalog"):
        # TAP.
        tap_type = dataset_type.removesuffix("searchable catalog").strip()
        write_bib(entry, "tap-" + tap_type)
    else:
        print(f"Didn't recognize {entry}")
