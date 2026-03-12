class Log:
  identificador = ""
  codigo_lotacao = ""
  registro_a_vincular = False
  unidade_vinculada = False
  conta_vinculada = False
  
  def to_dict(self):
    return {
      "Identificador": self.identificador,
      "Codigo de Lotacao": self.codigo_lotacao,
      "Registro a Vincular": self.registro_a_vincular,
      "Unidade Vinculada": self.unidade_vinculada,
      "Conta Vinculada": self.conta_vinculada
    }
