class Workflow:
  id = "",
  codigo = "",
  nome = "",
  col_key = "",
  route = "",
  input_id = "",

  def __init__(self, id, codigo, nome, col_key, route, input_id):
    self.id=id
    self.codigo=codigo
    self.nome=nome
    self.col_key=col_key
    self.route=route
    self.input_id=input_id
