from src.models.settings.db_connection_handler import db_connection_handler
from src.controllers.user_register import UserRegister
from src.models.repos.user_repos import UserRepos
from src.views.user_register_view import UserRegisterView
def user_register_composer():
  conn = db_connection_handler.get_connection()
  model = UserRepos(conn)
  controller = UserRegister(model)
  view = UserRegisterView(controller)
  
  return view