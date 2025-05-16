# C2S – Virtual Vehicle Agent  

A client-server system in Python that simulates a virtual agent for vehicle queries.  

## 🚗 Features  
- **MCP Protocol**: Communication via Model Context Protocol.  
- **Vehicle Queries**: Filter by brand, year, fuel type, etc.  
- **Conversational Agent**: Interprets natural language inputs.  
- **Local Database**: 500+ fictional vehicles with SQLite.  
- **Modular Architecture**: Clean and scalable design.  

## 🛠️ Technologies  
- Python 3.10+  
- SQLite + SQLAlchemy (ORM)  
- Faker (test data generation)  
- `tabulate` (CLI table formatting)  
- TCP/IP Sockets  
- Bash (automation scripts)  

## 📁 Project Structure  
```bash
c2s/
├── client/          # Client-side agent
├── database/        # DB models, migrations, and seeding
├── server/         # MCP protocol server
├── main_client.py   # Client entry point
├── main_server.py   # Server entry point
├── setup.sh         # 1-click setup script
├── requirements.txt # Dependencies
└── README.md        # You’re here :)
```
## 🚀 Quick Start

1. **Clone the repo::**

To download the repository, run the command below.

```bash
git clone https://github.com/Victor5g/Agente-de-Veiculos-C2S.git
cd Agente-de-Veiculos-C2S
```

2. **Set up the environment:**

To set up the environment, install dependencies, and run the project, execute the command below in the root directory of the project under `c2s/`.

```bash 
bash setup.sh
```

If you encounter permission issues, run this first!!

```bash 
chmod +x setup.sh
```

Tip: On the first run, type **y** to accept the option to populate the database before performing the search!!!

```bash 
🗄️  Deseja popular o banco de dados com dados randomicos ? (s/n): s
```
