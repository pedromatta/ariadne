from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException

class ContaPage(BasePage):

  # Localizadores de Pesquisa
  SEM_IDENTIFICACAO_RAD = (By.ID, "semidentificacao-1")
  PESQUISAR_BTN = (By.ID, "pesquisar")

  def __init__(self, driver, route, input_id):
    super().__init__(driver)
    self.route = route
    self.KEY_INPUT = (By.ID, input_id)

  def search_identifier(self, identifier):
    """Procura registro com o identificador especificado"""
    self.click(self.SEM_IDENTIFICACAO_RAD)
    self.enter_text(self.KEY_INPUT, identifier)
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
