#!/usr/bin/env python
import logging
import sys

import ase
import ase.io

from compute.layer_raman_engine import process_structure_core
from compute.utils.structures import tuple_from_ase


def test_structure(filename, skin_factor=1.1):
    logger = logging.getLogger("layer-raman-tool-app")

    # Print to stderr, also DEBUG messages
    # logger.setLevel(logging.DEBUG)
    logger.setLevel(logging.WARNING)
    logger.addHandler(logging.StreamHandler())

    asecell = ase.io.read(filename)
    structure = tuple_from_ase(asecell)
    return_data = process_structure_core(
        structure, logger, flask_request=None, skin_factor=skin_factor
    )
    print("RETURN DATA:")
    print(return_data)


if __name__ == "__main__":
    try:
        filename = sys.argv[1]
    except IndexError:
        print("Pass a filename")
        sys.exit(1)

    try:
        skin_factor = float(sys.argv[2])
    except IndexError:
        skin_factor = 1.1
    except ValueError:
        print("The second parameter, if present, must be a float")
        sys.exit(1)

    test_structure(filename, skin_factor=skin_factor)
