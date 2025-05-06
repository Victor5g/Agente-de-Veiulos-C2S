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

Para configurar o ambiente, instalar dependências, popular o banco de dados e executar o projeto, basta rodar:

```bash 
bash setup.sh
```

Caso tenha problemas de permissão, rode antes!!

```bash 
chmod +x setup.sh
```