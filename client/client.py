import random
import socket
from utils.protocol import pack_data, unpack_data, receive_data
from utils.replace import format_value_to_brl
from tabulate import tabulate

from data.questions import FILTER_QUESTIONS

HOST = 'localhost'
PORT = 9090

def get_filters():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        client.sendall(pack_data({"get_filters": True}))
        response = receive_data(client)
        available_filters = unpack_data(response)

    print("\n🙂 Olá! Eu seu agente seu assistente de busca de veiculos.")
    print("🚗 Vou fazer algumas perguntas para te ajudar a encontrar o carro ideal para voce!")
    print("\n🌀 Para ignoras as perguntas basta deixar as opcoes vazias, para fazer isso basta passar para a proxima pergunta clicando Enter/Proximo!\n")

    filters = {}
    for field in available_filters:
        if field == 'id':
            continue
        question = random.choice(FILTER_QUESTIONS.get(field, [f"{field}:"]))
        answer = input(f"👉 {question} ").strip()
        if answer:
            filters[field] = int(answer) if answer.isdigit() else answer
    return filters

def start_client():
    choice = input("🗄️  Deseja popular o banco de dados com dados randomicos ? (s/n): ").strip().lower()
    if choice == 's':
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((HOST, PORT))
            client.sendall(pack_data({"populate": True}))
            response = receive_data(client).decode()
            print(response)

    while True:
        try:
            filters = get_filters()
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
                client.connect((HOST, PORT))
                client.sendall(pack_data(filters))
                response = receive_data(client)
                vehicles = unpack_data(response)

                print("\n=== Veiculos encontrados ===")
                if vehicles:
                    headers = vehicles[0].keys()
                    rows = []

                    for v in vehicles:
                        row = []
                        for key in headers:
                            value = v.get(key, '')
                            if key == 'preco':
                                value = f"R${format_value_to_brl(value)}"
                            row.append(value)
                        rows.append(row)
                    print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))

                else:
                    print("🚗 Nenhum veiculo encontrado com base nos filtros fornecidos ⚠️.")

            again = input("\n🔎 Deseja fazer uma nova pesquisa ? (s/n): ").strip().lower()
            if again != 's':
                print("👋🏻 Ate logo. ")
                break
        except ConnectionRefusedError:
            print('❌ Erro ao conectar ao servidor.')
            break
