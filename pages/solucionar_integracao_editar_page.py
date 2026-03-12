from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class SolucionarIntegracaoEditarPage(BasePage):

  # Localizadores
  NOME_SISTEMA_ORIGEM_PARAGRAPH = (By.XPATH, "//label[@title='Nome do Sistema Origem']/following-sibling::p")

  def __init__(self, driver):
    super().__init__(driver)

  def get_name(self):
    paragraph = self.wait.until(EC.presence_of_element_located(self.NOME_SISTEMA_ORIGEM_PARAGRAPH))
    return paragraph.text

