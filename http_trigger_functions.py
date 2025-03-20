import logging
import azure.functions as func

http_triggers_bp = func.Blueprint()

def process_request(req: func.HttpRequest, function_type: str) -> str:
    """Helper function to process the request and return function details."""
    
    # Extract query parameters
    query_params = req.params

    # Extract body parameters if available
    try:
        req_body = req.get_json()
    except ValueError:
        req_body = {}

    return f"""
    This is a {function_type} HTTP triggered function executed successfully.
    Query Params: {query_params}
    Request Body: {req_body}
    """

@http_triggers_bp.route(route="function_http_trigger")
def function_http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Processing function_http_trigger request")
    response_message = process_request(req, "standard")
    return func.HttpResponse(response_message, status_code=200)

@http_triggers_bp.route(route="anonymous_http_trigger", auth_level=func.AuthLevel.ANONYMOUS)
def anonymous_http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Processing anonymous_http_trigger request")
    response_message = process_request(req, "anonymous")
    return func.HttpResponse(response_message, status_code=200)

@http_triggers_bp.route(route="secure_http_trigger", auth_level=func.AuthLevel.ADMIN)
def secure_http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Processing secure_http_trigger request")
    response_message = process_request(req, "secure (admin)")
    return func.HttpResponse(response_message, status_code=200)

@http_triggers_bp.route(route="get_http_trigger", methods=["GET"])
def get_http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Processing GET request")

    name = req.params.get("name", "Guest")  # Extract query param
    response_message = f"GET request received. Hello, {name}!"
    
    return func.HttpResponse(response_message, status_code=200)

@http_triggers_bp.route(route="post_http_trigger", methods=["POST"])
def post_http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Processing POST request")

    try:
        req_body = req.get_json()
        name = req_body.get("name", "Unknown")  # Extract name from request body
    except ValueError:
        name = "Unknown"

    response_message = f"POST request received. Hello, {name}!"
    
    return func.HttpResponse(response_message, status_code=200)

@http_triggers_bp.route(route="put_http_trigger", methods=["PUT"])
def put_http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Processing PUT request")

    try:
        req_body = req.get_json()
        item_id = req_body.get("id", "No ID provided")  # Extract item ID from body
    except ValueError:
        item_id = "No ID provided"

    response_message = f"PUT request received. Updating item with ID: {item_id}"
    
    return func.HttpResponse(response_message, status_code=200)

@http_triggers_bp.route(route="delete_http_trigger", methods=["DELETE"])
def delete_http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Processing DELETE request")

    item_id = req.params.get("id", "No ID provided")  # Extract item ID from query params
    response_message = f"DELETE request received. Deleting item with ID: {item_id}"
    
    return func.HttpResponse(response_message, status_code=200)
