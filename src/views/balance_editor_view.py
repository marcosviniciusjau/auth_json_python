from src.controllers.interfaces.balance_editor import BalanceEditorInterface
from src.errors.types.bad_request import BadRequestError
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse


class BalanceEditorView:

  def __init__(self, controller: BalanceEditorInterface) -> None:
    self.__controller = controller

  def handle(self, request: HttpRequest) -> HttpResponse:
    new_balance = request.body.get("new_balance")
    user_id = request.params.get("user_id")
    header_user_id = request.headers.get("uid")
    self.__validate_inputs(new_balance, user_id)

    response = self.__controller.edit(user_id, new_balance)
    return HttpResponse(body={"data": response}, status_code=200)

  def __validate_inputs(self,new_balance: any, user_id: any, header_user_id: any) -> None:
    if (
      not new_balance
      or not user_id
      or not isinstance(new_balance, float)
      or int(header_user_id) != int(user_id)
    ) : raise BadRequestError("Invalid input")