from src.controllers.interfaces.login_create import LoginCreatorInterface
from src.views.http_types.request import Request
from src.views.http_types.response import Response

class LoginCreatorView:
  def __init__(self, controller: LoginCreatorInterface) -> None:
    self.__controller = controller

  def handle(self, request: Request) -> Response:
    username = request.body.get("username")
    password = request.body.get("password")
    self.__validate_inputs(username, password)

    response = self.__controller.create(username, password)
    return Response(body={"data": response}, status_code=201)

  def __validate_inputs(self,username: any, password: any) -> None:
    if (
      not username
      or not password
      or not isinstance(username, str)
      or not isinstance(password, str)
    ) :
      raise Exception("Invalid username or password")