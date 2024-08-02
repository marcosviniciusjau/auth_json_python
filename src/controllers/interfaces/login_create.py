from abc import ABC, abstractmethod

class LoginCreateInterface(ABC):
  @abstractmethod
  def create(self, username: str, password: str) -> dict:
    pass