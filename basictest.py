import azure.functions as func
import pytest
from unittest.mock import Mock
from . import main 

def test_main():
    # Create a mock HTTP request
    req = Mock(func.HttpRequest)
    req.params = {}
    req.get_json = Mock(return_value={})

    # Call the function
    response = main(req)

    # Validate the response
    assert response.status_code == 200
    assert response.get_body().decode() == "Hello, World! for assignment3, student id 8933139"