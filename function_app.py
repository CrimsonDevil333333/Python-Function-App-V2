import logging
import azure.functions as func
from http_trigger_functions import http_triggers_bp

app = func.FunctionApp() 

app.register_functions(http_triggers_bp) # Register HTTP triggers blueprint

