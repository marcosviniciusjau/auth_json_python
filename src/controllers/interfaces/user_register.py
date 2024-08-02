from abc import ABC, abstractmethod

class UserRegisterInterface(ABC):
  @abstractmethod
  def registry_user(self, username: str, password: str) -> dict:
    pass