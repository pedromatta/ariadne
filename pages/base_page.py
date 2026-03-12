from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from config import settings

class BasePage:

  route = ""

  # Localizadores genericos de Tabela
  ROW_FIRST_CELL = (By.XPATH, "./td[1]")
  ROWS = (By.TAG_NAME, "tr")

  def __init__(self, driver):
    self.driver = driver
    self.wait = WebDriverWait(driver, 1)

  def click(self, locator, retries=2):
    """Executa um clique em um elemento na pagina."""
    for _ in range(retries):
      try:
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        return
      except StaleElementReferenceException:
        pass
    raise Exception(f"Element {locator} not clickable after {retries} retries.")

  def navigate_to(self):
    """Navega para a pagina."""
    full_url = f"{settings.CIC_URL}{self.route}"
    self.driver.get(full_url)
     
  def js_click(self, locator):
    """Executa um clique diretamente via JavaScript para evitar problemas de UI."""
    element = self.wait.until(EC.presence_of_element_located(locator))
    self.driver.execute_script("arguments[0].click();", element)

  def enter_text(self, locator, text):
    """Insere texto em um elemento da pagina"""
    element = self.wait.until(EC.visibility_of_element_located(locator))
    element.clear()
    element.send_keys(text)

  def enter_text_and_return(self, locator, text):
    """Insere texto em um elemento da pagina e pressiona enter"""
    element = self.wait.until(EC.visibility_of_element_located(locator))
    element.clear()
    element.send_keys(text, Keys.RETURN)
  
  def find_elements(self, locator):
    """Retorna uma lista de elementos ou vazios se nenhum for encontrado rapidamente"""
    self.wait.until(EC.presence_of_all_elements_located(locator))
    return self.driver.find_elements(*locator)

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
