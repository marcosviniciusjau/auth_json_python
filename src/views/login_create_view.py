from src.controllers.interfaces.login_create import LoginCreateInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class LoginCreateView:
  def __init__(self, controller: LoginCreateInterface) -> None:
    self.__controller = controller

  def handle(self, request: HttpRequest) -> HttpResponse:
    username = request.body.get("username")
    password = request.body.get("password")
    self.__validate_inputs(username, password)

    response = self.__controller.create(username, password)
    return HttpResponse(body={"data": response}, status_code=201)

  def __validate_inputs(self,username: any, password: any) -> None:
    if (
      not username
      or not password
      or not isinstance(username, str)
      or not isinstance(password, str)
    ) :
      raise Exception("Invalid username or password")