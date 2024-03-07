# whois_custom.py

import socket

def obter_informacoes_whois(dominio):
    """
    Obtém informações WHOIS para um domínio.

    Args:
        dominio (str): O domínio para o qual deseja obter informações.

    Returns:
        str: A resposta WHOIS do servidor.
    """
    whois_server = "whois.iana.org"
    whois_port = 43

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((whois_server, whois_port))
            s.sendall(f"{dominio}\r\n".encode())
            response = b""
            while True:
                data = s.recv(1024)
                if not data:
                    break
                response += data
        return response.decode()
    except Exception as e:
        return f"Erro ao obter informações WHOIS: {str(e)}"

if __name__ == "__main__":
    dominio_digitado = input("Digite o domínio para obter informações WHOIS: ")
    informacoes_whois = obter_informacoes_whois(dominio_digitado)

    print("Resposta WHOIS:")
    print(informacoes_whois)
