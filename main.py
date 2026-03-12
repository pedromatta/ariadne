import pandas as pd
import time
import sys
from datetime import datetime
from utils.webdriver_setup import get_driver
from utils.menu import show_menu 
from data.data_handler import DataHandler
from data.log import Log
from pages.login_page import LoginPage
from pages.solucionar_integracao_page import SolucionarIntegracaoPage
from pages.solucionar_integracao_editar_page import SolucionarIntegracaoEditarPage
from pages.conta_page import ContaPage
from pages.conta_vincular_page import ContaVincularPage


def main():

  workflow = show_menu()

  handler = DataHandler(input_file_path="./fidedignas.xlsx")
  df_fidedignas = handler.load_fidedignas()
  conta_dict = handler.create_mapping_dict(
    df=df_fidedignas,
    col_codigo_lotacao="CODIGO_DE_LOTACAO",
    col_key=workflow.col_key,
    skip=0
  )

  log_data = []

  # Setup WebDirver
  driver = get_driver()

  try:
    # Login
    login_page = LoginPage(driver)
    login_page.load_website()
    login_page.login()
    time.sleep(2)

    conta_page = ContaPage(driver, workflow.route, workflow.input_id)
    conta_vincular_page = ContaVincularPage(driver)
    solucionar_integracao_page = SolucionarIntegracaoPage(driver)
    solucionar_integracao_editar_page = SolucionarIntegracaoEditarPage(driver)

    for identifier, codigo_lotacao in conta_dict.items():

      # Inicia o registro do log para esse item
      log_current = Log()
      log_current.identificador = identifier
      log_current.codigo_lotacao = codigo_lotacao

      # Navega para a página de Conta de Água
      conta_page.navigate_to()

      # Pesquisa pela matricula
      conta_page.search_identifier(identifier)
      registro_encontrado = conta_page.select_first_result()

      if not registro_encontrado:
        log_data.append(log_current)
        continue
      
      # Registra que o registro esta pendente de vinculacao
      log_current.registro_a_vincular = True

      # Navegamos ate a pagina de integracao
      solucionar_integracao_page.navigate_to()
      solucionar_integracao_page.search_codigo_lotacao(codigo_lotacao)
      codigo_lotacao_encontrado = solucionar_integracao_page.select_first_result()

      if not codigo_lotacao_encontrado:
        log_data.append(log_current)
        continue

      # Registra que a unidade está vinculada
      log_current.unidade_vinculada = True

      name = solucionar_integracao_editar_page.get_name()
      conta_page.navigate_to()
      conta_page.search_identifier(identifier)

      conta_vinculada = conta_vincular_page.executar_vinculo(name)

      if not conta_vinculada :
        log_data.append(log_current)
        continue

      # Registra que a conta foi vinculada
      log_current.conta_vinculada = True
      log_data.append(log_current)

  finally:
    # Salva o arquivo de log
    df_log = pd.DataFrame([log.to_dict() for log in log_data])
    log_path = f"log/{workflow.nome} - {datetime.now().strftime('%Y%m%d%H%M')}.csv"
    df_log.to_csv(log_path, index=False, sep=';')
    driver.quit()

if __name__ == "__main__":
  main()
