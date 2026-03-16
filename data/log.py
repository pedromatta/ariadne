class Log:
  identificador = ""
  codigo_lotacao = ""
  registro_a_vincular = False
  unidade_encontrada = False
  conta_vinculada = False
  
  def to_dict(self):
    return {
      "Identificador": self.identificador,
      "Codigo de Lotacao": self.codigo_lotacao,
      "Registro a Vincular": self.registro_a_vincular,
      "Unidade Encontrada": self.unidade_encontrada,
      "Conta Vinculada": self.conta_vinculada,
    }
