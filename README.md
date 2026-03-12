# Bot de Vinculação de Contas

**Versão do CIC: 3.0.0**

### Obtenção dos Arquivos

O único arquivo necessário para a execução desse script é a planilha de fidedignas consolidada. O arquivo está disponível no drive da GCUST:

- Vá até o drive da GCUST e baixe o arquivo em PowerBI -> Fontes -> Fidedignas_Consolidadas

Coloque esse arquivo na raíz desse repositório com o nome "fidedignas.xlsx".

### Execução

Navegue até o diretório config. Copie o arquivo .env.example para um arquivo .env. Preencha as variáveis de ambiente com suas credenciais válidas e com uma url válida do CIC.

Navegue de volta para a raíz do repositório. Crie um ambiente virtual para executar o script.
```zsh
python -m venv .venv
```

Ative ambiente virtual.
```zsh
source ./.venv/Scripts/activate
```

Instale as dependencias.
```zsh
pip install
```

Execute o arquivo `main.py`, direto da raíz do projeto.
```zsh
python main.py
```

Siga os passos no menu interativo e acompanhe a execução do bot.

### Manutenção

O código dessa automação foi desenvolvido em python na versão 3.14.2

O código está dividido em 4 diretórios de scripts e a raíz, o propósito geral de cada diretório é o que segue:

| Diretório | Propósito                                                                                                                  |
| :---:     | :---                                                                                                                       |
| ./        | Na raíz se encontram o arquivo Fidedignas de fonte de dados e o arquivo main.py que serve como orquestrador da execução.   |
| data/     | Estruturas utilizadas no código: Workflow e Log. Além da classe DataHandler, que gerencia a leitura do arquivo de fidedignas |
| utils/    | Funções utilitárias: Definição do menu cli para escolher o workflow e setup do navegador Edge.                             |
| config/   | Armazenamento e leitura das variáveis de ambiente.                                                                         |
| pages/    | Definição das páginas da aplicação, todas as páginas herdam os métodos básicos da classe BasePage e implementam navegações específicas internamente |
