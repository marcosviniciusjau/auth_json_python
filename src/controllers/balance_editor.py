from src.controllers.interfaces.balance_editor import BalanceEditorInterface
from src.models.interfaces.user_repo import UserReposInterface
class BalanceEditor(BalanceEditorInterface):
  def __init__(self, user_repo: UserReposInterface) -> None:
    self.__user_repo = user_repo

  def edit(self, user_id: int, new_balance: float) -> None:
    self.__user_repo.edit_balance(user_id, new_balance)
    return {
      "type": "User",
      "count": 1,
      "new_balance": new_balance
    }