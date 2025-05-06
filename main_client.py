from client.client import start_client

if __name__ == "__main__":
    try:
        start_client()
    except KeyboardInterrupt:(
        print("\n⏸️ Cliente encerrado manualmente."))

