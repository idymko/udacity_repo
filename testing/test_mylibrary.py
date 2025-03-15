# File: test_mylibrary.py
# Pytest filename starts with "test_...."
import pytest
import pandas as pd
import requests
import logging 

##################################
"""
Function to test
"""
def import_data(pth):
    df = pd.read_csv(pth)
    return df
##################################
"""
Fixture - The test function test_import_data() will 
use the return of path() as an argument
"""
@pytest.fixture(scope="module", params=["sample_file1.txt", "sample_file2.txt"])
# https://docs.pytest.org/en/7.1.x/how-to/fixtures.html
def path(request):
    value = request.param
    return value

##################################
"""
Test method
"""
def test_import_data(path):
    try:
        df = import_data(path)

    except FileNotFoundError as err:
        logging.error("File not found")
        raise err

    # Check the df shape
    try:
        assert df.shape[0] > 0
        assert df.shape[1] > 0

    except AssertionError as err:
        logging.error(
            "Testing import_data: The file doesn't appear to have rows and columns")
        raise err
    return None
##################################