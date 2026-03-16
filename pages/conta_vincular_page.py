from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ContaVincularPage(BasePage):
  # Locators 
  ID_FRAME = ("ifDlgUnidade")
  UNIDADE_BTN = (By.ID, "detalhe-1-nomeUnidade")
  CODIGO_LOTACAO_INPUT = (By.XPATH, "//input[@title='Codigo de Lotacao']")
  PESQUISAR_BTN = (By.ID, "pesquisar")

  def __init__(self, driver):
      super().__init__(driver)

  def search_unidade(self, codigo_lotacao):
    self.click(self.UNIDADE_BTN)
    self.driver.switch_to.frame(self.ID_FRAME)
    self.enter_text(self.CODIGO_LOTACAO_INPUT, codigo_lotacao)
    self.click(self.PESQUISAR_BTN)
    time.sleep(1)

  def gravar_vinculacao(self):
    try:
      print("Olha que eu gravo, hein?")
      return True
    except:
      return False
    finally:
      time.sleep(1)


