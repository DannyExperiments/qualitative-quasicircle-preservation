# Reproduce the checks

Run the standard-library Python replay from the repository root.

    python3 -I scripts/verify_repository.py
    python3 verification/src/replay.py

The first command checks file hashes and the offline explorer archive. The second checks the marked polygon and a finite model of the plateau construction with exact rational arithmetic.

Build the PDF using [the TeX instructions](paper/BUILD.md). The [offline explorer](visualization/construction-explorer.zip) runs from a local file in a browser. To regenerate the GIF, use Python with Pillow and run the script documented in [the illustrated guide](visualization/README.md).
