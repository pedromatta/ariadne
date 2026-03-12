import sys
from data.workflow import Workflow

# Lista dos workflows disponiveis
WORKFLOWS = [
  Workflow(
    id = "1",
    nome = "Conta de Agua",
    col_key = "COPASA_MATRICULA",
    route = "contaagua",
    input_id = "matricula",
  ),
  Workflow(
    id = "2",
    nome = "Conta de Energia",
    col_key = "NUMERO_DA_INSTALACAO",
    route = "contaenergia",
    input_id = "numero_instalacao"
  ),
  Workflow(
    id = "3",
    nome = "Conta de Telefonia",
    col_key = "TELEFONES_FIXOS_DA_UNIDADE",
    route = "contatelefonia",
    input_id = "numero_telefone"
  )
]

def show_menu() -> Workflow :
  """Mostra o menu e retorna o workflow selecionado"""
  workflows_dict = {workflow.id: workflow for workflow in WORKFLOWS}

  print("=== Menu de Vinculacao ===")
  for workflow in WORKFLOWS:
    print(f"[{workflow.id}] - {workflow.nome}")
  print("[0] - Sair")

  while True:
    choice = input("Escolha o tipo de conta que deseja vincular: ")

    if choice == "0":
      print("Saindo do programa...")
      sys.exit(0)

    elif choice in workflows_dict:
      workflow_selecionado = workflows_dict[choice]
      print(f"\nIniciando o fluxo para {workflow_selecionado.nome}...")
      return workflow_selecionado

    else:
      print("Opcao invalida. Tente novamente.")
