import json
import pytest
from unittest.mock import Mock
import azure.functions as func
from http_trigger_functions import function_http_trigger, anonymous_http_trigger, secure_http_trigger, get_http_trigger, post_http_trigger, put_http_trigger, delete_http_trigger

# Helper function to create a mock HTTP request
def create_mock_request(method, params=None, body=None):
    mock_req = Mock()
    mock_req.method = method
    mock_req.params = params or {}
    mock_req.get_json = Mock(return_value=body or {})
    return mock_req

@pytest.mark.parametrize("func_handler,method,params,body,expected_response", [
    (function_http_trigger, "GET", {"name": "Test"}, None, "Query Params: {'name': 'Test'}"),
    (anonymous_http_trigger, "GET", {}, None, "anonymous HTTP triggered function"),
    (secure_http_trigger, "GET", {}, None, "secure (admin) HTTP triggered function"),
    (get_http_trigger, "GET", {"name": "Alice"}, None, "Hello, Alice!"),
    (post_http_trigger, "POST", {}, {"name": "Bob"}, "Hello, Bob!"),
    (put_http_trigger, "PUT", {}, {"id": "1234"}, "Updating item with ID: 1234"),
    (delete_http_trigger, "DELETE", {"id": "5678"}, None, "Deleting item with ID: 5678"),
])
def test_http_triggers(func_handler, method, params, body, expected_response):
    mock_req = create_mock_request(method, params, body)
    response = func_handler(mock_req)  # Call the actual function handler

    assert response.status_code == 200
    assert expected_response in response.get_body().decode()
