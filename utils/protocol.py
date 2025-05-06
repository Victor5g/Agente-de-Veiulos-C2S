import json
import socket

ENCODING = 'utf-8'

def pack_data(dados: list) -> bytes:
    body = json.dumps(dados).encode(ENCODING)
    size = len(body).to_bytes(4, byteorder='big')
    return size + body

def unpack_data(dados_bytes: bytes) -> list:
    try:
        return json.loads(dados_bytes.decode(ENCODING))
    except json.JSONDecodeError as e:
        return [{"erro": f"Dados invalidos: {str(e)}"}]
    
def recv_all(sock, n):
    data = b""
    while len(data) < n:
        part = sock.recv(n - len(data))
        if not part:
            raise EOFError("Conexao encerrada durante recebimento do dado")
        data += part
    return data

def receive_data(sock: socket.socket) -> bytes:
    size_data = sock.recv(4)
    if not size_data:
        raise ConnectionError("Tamanho da mensagem nao recebido.")
    total_size = int.from_bytes(size_data, byteorder='big')

    received = b''
    while len(received) < total_size:
        chunk = sock.recv(min(4096, total_size - len(received)))
        if not chunk:
            break
        received += chunk
    return received
