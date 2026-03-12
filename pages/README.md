# pages

Concentra a lógica de interação com o webdriver a partir da página especifica, mesmo que pouca interação seja feita em uma página, julguei importante separá-la do fluxo para que não se confundam as responsabilidades.

`base_page.py`
Todas as páginas herdam os métodos da página base. Ela declara métodos auxiliares para a abstração da interação com o webdriver, além de locadores comuns para todas as pǵinas que possuem tabelas;

`conta_page.py`
Página genérica de contas, na versão atual do CIC, todas as páginas de contas funcionam de forma semelhante, com as peculiaridades de cada uma sendo enviadas dinâmicamente por parâmetros.

`conta_vincular_page.py`
A mesma lógica da página genérica de contas, mas para as páginas de vinculação (edição).

`login_page.py`
Essa página recebe as credenciais obtidas no `settings.py` e utiliza-as para realizar o login no cic.

`solucionar_integracao_page.py`
Lógica de navegação especifica para a página "solucionar integracao". O fluxo utiliza o codigo de lotação de um registro para encontrar a unidade.

`solucionar_integracao_editar_page.py`
Salva o nome da unidade encontrada na página solucionar_integracao.
