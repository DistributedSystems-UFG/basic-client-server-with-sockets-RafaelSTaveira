from socket import *
from constCS import SERVER_HOST, PORT, BUFFER_SIZE

def main():
    print("Cliente iniciado.")
    print(f"Conectando em {SERVER_HOST}:{PORT}")

    while True:
        requisicao = input("\nDigite a requisição (ou 'sair'): ").strip()

        if requisicao.lower() == "sair":
            print("Encerrando cliente.")
            break

        if not requisicao:
            print("Digite algum comando.")
            continue

        s = socket(AF_INET, SOCK_STREAM)
        s.connect((SERVER_HOST, PORT))
        s.send(requisicao.encode())

        data = s.recv(BUFFER_SIZE)
        resposta = data.decode()

        print("\nResposta do servidor:")
        print(resposta)

        s.close()

if __name__ == "__main__":
    main()
