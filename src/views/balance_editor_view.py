from src.controllers.interfaces.balance_editor import BalanceEditorInterface
from src.views.http_types.request import Request
from src.views.http_types.response import Response


class BalanceEditorView:

  def __init__(self, controller: BalanceEditorInterface) -> None:
    self.__controller = controller

  def handle(self, request: Request) -> Response:
    new_balance = request.body.get("new_balance")
    user_id = request.param.param.get("user_id")
    self.__validate_inputs(new_balance, user_id)

    response = self.__controller.edit(user_id, new_balance)
    return Response(body={"data": response}, status_code=200)

  def __validate_inputs(self,new_balance: any, user_id: any) -> None:
    if (
      not new_balance
      or not user_id
      or not isinstance(new_balance, float)
    ) :
      raise Exception("Invalid username or password")