# C2S – Agente Virtual de Veículos

Sistema cliente-servidor em Python, que simula um agente virtual para consulta de veículos.

## 🚗 Funcionalidades

- Comunicação via protocolo MCP (Model Context Protocol)
- Consulta de veículos a partir de filtros como marca, ano, tipo de combustível etc.
- Agente conversacional que interpreta frases naturais
- Banco de dados local com mais de 500 veículos fictícios
- Arquitetura limpa e modular

## 🛠️ Tecnologias Utilizadas

- Python 3.10+
- SQLite + SQLAlchemy
- Faker
- tabulate
- Socket TCP/IP
- Scripts automatizados com Bash

## 📁 Estrutura do Projeto

```bash
c2s/
├── client/ # Agente usados pelo cliente
├── database/ # Modelos, banco de dados e seed
├── server/ # Agente usado pelo servidor MCP
├── main_client.py # Inicializa o cliente
├── main_server.py # Inicializa o servidor
├── setup.sh # Executa tudo de forma automática
├── requirements.txt # Dependências
└── README.md # Documentação
```
## 🚀 Execução Rápida

1. **Clone o repositório:**

Para baixar o repositorio rode o comando abaixo.

```bash
git clone https://github.com/Victor5g/Agente-de-Veiculos-C2S.git
cd Agente-de-Veiculos-C2S
```

2. **Configurar ambiente:**

Para configurar o ambiente, instalar dependências, e executar o projeto, rode o comando abaixo na raiz do projeto em c2s/

```bash 
bash setup.sh
```

Caso tenha problemas de permissão, rode antes!!

```bash 
chmod +x setup.sh
```

Dica, na primeira execução, digite s para aceitar a opcao de popular o banco de dados antes de realizar a pesquisa!!!

```bash 
🗄️  Deseja popular o banco de dados com dados randomicos ? (s/n): s
```