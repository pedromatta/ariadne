class Workflow:
  id = "",
  nome = "",
  col_key = "",
  route = "",
  input_id = "",

  def __init__(self, id, nome, col_key, route, input_id):
    self.id=id
    self.nome=nome
    self.col_key=col_key
    self.route=route
    self.input_id=input_id
