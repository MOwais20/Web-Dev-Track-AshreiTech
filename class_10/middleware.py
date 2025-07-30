from starlette.requests import Request
from starlette.responses import Response
import time

# Middleware function to log details about each request
async def log_requests(request: Request, call_next):
    # Record the start time of the request
    start_time = time.time()
    # Process the request and get the response
    response: Response = await call_next(request)
    # Calculate how long the request took to process
    process_time = time.time() - start_time
    # Print the HTTP method, path, and processing time
    print(f"{request.method} {request.url.path} completed in {process_time:.4f}s")
    # Return the response to the client
    return response
