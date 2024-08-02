from src.controllers.login_create import LoginCreate
from src.models.repos.user_repos import UserRepos
from src.views.login_create_view import LoginCreateView
from src.models.settings.db_connection_handler import db_connection_handler

def login_create_composer():
  conn = db_connection_handler.get_connection()
  model = UserRepos(conn)
  controller = LoginCreate(model)
  view = LoginCreateView(controller)
  
  return view