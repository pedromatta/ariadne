# config

## Utilização

Esse diretório é responsável pelo armazenamento e leitura das variáveis de ambiente.

Da raiz do repositório, navegue até esse diretório
```.zsh
cd config
```

Copie e cole o arquivo .env.example como .env 
```zsh
cp .env.example .env
```

Edite o arquivo .env e preencha suas credenciais válidas:
```zsh
notepad .env
```
```.env
CIC_URL="http://localhost:84/cic-datacenter/"
CIC_USERNAME=usernamevalidoparaocic
CIC_PASSWORD=senhavalidaparaousername
```

## Manutenção

Esse diretório possui o script `settings.py` que lê o arquivo .env em `config/.env`.
Ele utiliza as bibliotecas `os` e `dotenv`.
