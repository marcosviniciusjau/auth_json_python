from src.controllers.balance_editor import BalanceEditor
from src.models.repos.user_repos import UserRepos
from src.views.balance_editor_view import BalanceEditorView
from src.models.settings.db_connection_handler import db_connection_handler

def balance_editor_composer():
  conn = db_connection_handler.get_connection()
  model = UserRepos(conn)
  controller = BalanceEditor(model)
  view = BalanceEditorView(controller)

  return view