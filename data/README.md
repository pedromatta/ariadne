# data

Este diretório centraliza a criação de classes estruturas e manipulação de dados.

## Manutenção

`log.py`:
Define a estrutura que será usada nos objetos do log, o log será iniciado com todos os booleanos em false e eles serão preenchidos para cada registro durante o fluxo de execução orquestrado pelo `main`

`workflow.py`:
Define a estrutura que mapeia as informações específicas do fluxo de interação de cada conta que deve ser vinculada.

`data_handler.py`:
Realiza a leitura e limpeza dos dados da planilha de fidedignas, o path para a planilha é enviado dinâmicamente.
