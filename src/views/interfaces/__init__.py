from abc import ABC, abstractmethod
from src.views.http_types.http_request import Request
from src.views.http_types.http_response import Response

class ViewInterface(ABC):
  @abstractmethod
  def handle(self, request: Request) -> Response:
    pass