import socket
from server.handler import search_vehicles, get_available_filters
from database.seed import popular_bank
from utils.protocol import unpack_data, pack_data, receive_data

HOST = 'localhost'
PORT = 9090

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen()
        print(f"🚀 Servidor executando em {HOST}:{PORT}...")

        while True:
            conn, addr = server.accept()
            with conn:
                print(f"📡 Conexao recebida de {addr}")

                try:
                    data = receive_data(conn)
                    filters = unpack_data(data)
                    print("⛓️ Solicitacao recebida:", filters)

                    if filters.get("get_filters"):
                        available_filters = get_available_filters()
                        conn.sendall(pack_data(available_filters))

                    elif filters.get("populate"):
                        popular_bank()
                        conn.sendall(pack_data("🗂️ Banco populado com sucesso."))

                    else:
                        response = search_vehicles(filters)
                        conn.sendall(pack_data(response))

                except Exception as e:
                    print(f"❌ Erro ao processar requisicao: {e}")
