import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ContaVincularPage(BasePage):
  # Locators 
  UNIDADE_BTN = (By.ID, "detalhe-1-nomeUnidade")
  NOME_UNIDADE_INPUT = (By.ID, "nome_unidade")
  PESQUISAR_BTN = (By.ID, "pesquisar")

  def __init__(self, driver):
      super().__init__(driver)

  def executar_vinculo(self, nome):
    """
    Pesquisa a unidade e seleciona o primeiro resultado.
    """
    time.sleep(3) 
    self.search_unidade(nome)

    return self.select_first_result()

  def search_unidade(self, nome):
    self.click(self.UNIDADE_BTN)
    self.enter_text(self.NOME_UNIDADE_INPUT, nome)
    self.click(self.PESQUISAR_BTN)

