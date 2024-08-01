from src.drivers.password_handler import PasswordHandler
from src.models.repos.user_repos import UserRepos
from src.models.interfaces.user_repo import UserReposInterface

class UserRegister:

  def __init__(self, user_repos:UserReposInterface) -> None:
    self.__user_repos = user_repos
    self.__password_handle = PasswordHandler()

  def registry_user(self, username: str, password: str) -> dict:
   hashed_password = self.__create_hash_password(password)
   self.__registry_new_user(username, hashed_password)
   return self.__format_response(username)
  
  def __create_hash_password(self, password: str) -> str:
    hashed_password = self.__password_handle.encrypt_password(password)
    return hashed_password
  
  def __registry_new_user(self, username: str, hashed_password: str)-> None:
    self.__user_repos.registry_user(username, hashed_password)

  def __format_response(self, username: str) -> dict:
    return {
      "type": "User",
      "count": 1,
      "username": username
    }
    
  