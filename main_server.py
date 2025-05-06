from server.run import start_server
from database.seed import create_bank

if __name__ == "__main__":
    try:
        create_bank()
        start_server()
    except KeyboardInterrupt:(
        print("\n⏸️ Servidor encerrado manualmente."))