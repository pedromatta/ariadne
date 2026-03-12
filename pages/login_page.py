from config import settings
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
  # --- Locators ---
  USERNAME_INPUT = (By.ID, "username")   
  PASSWORD_INPUT = (By.ID, "password")     

  def __init__(self, driver):
    super().__init__(driver)

  def load_website(self):
    """Navega o driver para a url definida"""
    if not settings.CIC_URL:
      raise ValueError("CIC_URL not found in .env file.")
    self.driver.get(settings.CIC_URL)

  def login(self):
    """Insere as credenciais e pressiona enter"""
    if not settings.CIC_USERNAME or not settings.CIC_PASSWORD:
      raise ValueError("Credentials missing in .env file.")
        
    # Using the methods inherited from BasePage
    self.enter_text(self.USERNAME_INPUT, settings.CIC_USERNAME)
    self.enter_text_and_return(self.PASSWORD_INPUT, settings.CIC_PASSWORD)
