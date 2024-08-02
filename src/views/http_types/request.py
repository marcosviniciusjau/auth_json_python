class Request:
  def __init__(
      self, 
      body: dict,
      headers: dict = None,
      param: dict = None,
      token_infos: dict = None
    ) -> None:
    self.body = body
    self.headers = headers
    self.param = param
    self.token_infos = token_infos
