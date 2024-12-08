import azure.functions as func
import pytest
from unittest.mock import Mock
from . import main 

def test_with_json_body():
    # Create a mock HTTP request with a JSON body containing a name parameter
    req = Mock(func.HttpRequest)
    req.params = {}
    req.get_json = Mock(return_value={'name': 'dhaval'})

    # Call the function
    response = main(req)

    # Validate the response
    assert response.status_code == 200
    assert response.get_body().decode() == "Hello, dhaval!"
