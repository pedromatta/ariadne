from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException

class SolucionarIntegracaoPage(BasePage):

  route = "solucionarintegracao"

  # Localizadores de Pesquisa
  REGISTROS_DE_INTEGRACAO_RAD = (By.ID, "uniReg-1")
  REGISTROS_ASSOCIADOS_RAD = (By.ID, "ind_sem_identificacao-1")
  CODIGO_CENTRO_CUSTO_INPUT = (By.ID, "codigo_centro_custo")
  PESQUISAR_BTN = (By.ID, "pesquisar")

  def __init__(self, driver):
    super().__init__(driver)

  def search_codigo_lotacao(self, codigo_lotacao):
    """Procura registro pelo codigo de lotacao"""
    self.click(self.REGISTROS_DE_INTEGRACAO_RAD)
    self.enter_text(self.CODIGO_CENTRO_CUSTO_INPUT, codigo_lotacao)
    self.js_click(self.PESQUISAR_BTN)

  def select_first_result(self):
    """
    Clica no primeiro registro clicável na tabela de resultado da pesquisa.
    Retorna True se conseguir clicar em algum registro e False se não conseguir
    clicar em nenhuma linha ou nenhum resultado aparecer.
    """
    try:
      # Tenta encontrar as linhas
      rows = self.find_elements(self.ROWS)
      if not rows:
        return False
          
      # Itera pelas linhas para clicar no primeiro 'td'
      for row in rows:
        try:
          first_cell = row.find_element(*self.ROW_FIRST_CELL)
          first_cell.click()
          return True # Sucesso
        except Exception:
          continue # Tenta a proxima linha se a primeira não for clicavel
                
      return False # Nao conseguiu clicar em nenhuma linha
    except TimeoutException:
      return False # Nenhum resultado apareceu
