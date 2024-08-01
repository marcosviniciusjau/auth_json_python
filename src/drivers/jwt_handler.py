import jwt
from datetime import datetime, timedelta
from src.config.jwt_configs import jwt_infos
class JWTHandler:
  def create_token(self, body: dict = {})-> str:
    token = jwt.encode(
      payload = {
        'exp': datetime.utcnow() + timedelta(days=1),
        **body
      },
      key = jwt_infos['KEY'],
      algorithm = jwt_infos['ALGORITHM']
    )
    return token

  def decode_token(self,token:str)-> dict:
    token_info = jwt.decode(
      token,
      key=jwt_infos['KEY'],
      algorithms=jwt_infos['ALGORITHM']
      )
    return token_info
