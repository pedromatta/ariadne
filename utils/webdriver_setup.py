from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service

def get_driver():
  """Configura o WebDriver para o Microsoft Edge"""
  edge_options = Options()
  edge_options.add_argument("--start-maximized")
  edge_options.add_argument("--disable-extensions")
  edge_options.add_argument("--ignore-certificate-errors")
  driver = webdriver.Edge(options=edge_options)
  return driver
