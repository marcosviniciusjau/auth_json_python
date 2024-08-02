from src.views.http_types.http_response import HttpResponse
from .types.bad_request import BadRequestError
from .types.not_found import NotFoundError
from .types.unauthorized import UnauthorizedError

def handle_errors(error: Exception) -> HttpResponse:
  if isinstance(error, (BadRequestError, NotFoundError, UnauthorizedError)):
     return HttpResponse(
          status_code=error.status_code,
           body={
              "errors": [{
                 "title": error.name,
                 "detail": error.message
              }]
            }
      )
   
  return HttpResponse(
      status_code=500,
      body={
         "errors": [{
            "title": "Internal Server Error",
            "detail": str(error)
         }]
       }
   )