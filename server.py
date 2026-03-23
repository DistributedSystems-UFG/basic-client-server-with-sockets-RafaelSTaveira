from socket import *
from constCS import PORT, BUFFER_SIZE

def formatar_numero(valor):
    if isinstance(valor, float) and valor.is_integer():
        return int(valor)
    return valor

def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
    return True

def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def processar_comando(comando):
    partes = comando.strip().split()

    if not partes:
        return "Comando vazio."

    op = partes[0].lower()

    try:
        if op == "soma":
            if len(partes) != 3:
                return "Uso: soma a b"
            a = float(partes[1])
            b = float(partes[2])
            r = a + b
            return f"soma {formatar_numero(a)} {formatar_numero(b)} = {formatar_numero(r)}"

        elif op == "subtrai":
            if len(partes) != 3:
                return "Uso: subtrai a b"
            a = float(partes[1])
            b = float(partes[2])
            r = a - b
            return f"subtrai {formatar_numero(a)} {formatar_numero(b)} = {formatar_numero(r)}"

        elif op == "multiplica":
            if len(partes) != 3:
                return "Uso: multiplica a b"
            a = float(partes[1])
            b = float(partes[2])
            r = a * b
            return f"multiplica {formatar_numero(a)} {formatar_numero(b)} = {formatar_numero(r)}"

        elif op == "divide":
            if len(partes) != 3:
                return "Uso: divide a b"
            a = float(partes[1])
            b = float(partes[2])
            if b == 0:
                return "Erro: divisão por zero."
            r = a / b
            return f"divide {formatar_numero(a)} {formatar_numero(b)} = {formatar_numero(r)}"

        elif op == "fatorial":
            if len(partes) != 2:
                return "Uso: fatorial n"
            n = int(partes[1])
            if n < 0:
                return "Erro: fatorial só aceita inteiro não negativo."
            r = fatorial(n)
            return f"fatorial {n} = {r}"

        elif op == "primo":
            if len(partes) != 2:
                return "Uso: primo n"
            n = int(partes[1])
            r = eh_primo(n)
            return f"primo {n} = {r}"

        else:
            return f"Operação '{op}' não reconhecida."

    except ValueError:
        return f"Erro no comando '{comando}': use números válidos."

def main():
    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(('0.0.0.0', PORT))
    s.listen(5)

    print(f"Servidor ouvindo na porta {PORT}...")

    while True:
        conn, addr = s.accept()
        print(f"Cliente conectado: {addr}")

        data = conn.recv(BUFFER_SIZE)

        if not data:
            conn.close()
            continue

        requisicao = data.decode().strip()
        print(f"Requisição recebida: {requisicao}")

        comandos = [c.strip() for c in requisicao.split(";") if c.strip()]

        if not comandos:
            resposta = "Nenhum comando recebido."
        else:
            resultados = []
            for comando in comandos:
                resultados.append(processar_comando(comando))
            resposta = "\n".join(resultados)

        conn.send(resposta.encode())
        conn.close()
        print("Conexão encerrada.\n")

if __name__ == "__main__":
    main()
