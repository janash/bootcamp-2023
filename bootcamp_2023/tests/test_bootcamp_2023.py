"""
Unit and regression test for the bootcamp_2023 package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest
import numpy as np

import bootcamp_2023

def test_build_bond_list_exception():

    coordinates = np.array([[0,0,0], [0,1,0]])

    with pytest.raises(ValueError):
        bootcamp_2023.build_bond_list(coordinates, max_bond=1, min_bond=1.1)

def test_bootcamp_2023_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "bootcamp_2023" in sys.modules
