def test_response_code():
    # Create a mock HTTP request
    req = Mock(func.HttpRequest)
    req.params = {}
    req.get_json = Mock(return_value={})

    # Call the function
    response = main(req)

    # Validate the response code
    assert response.status_code == 200
