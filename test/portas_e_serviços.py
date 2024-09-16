import socket
from colorama import init, Fore, Back, Style

logo = """
┏━━━┓
┃┏━┓┃
┃┗━━┳━━┳━┳┓┏┳┓┏━━┳━━┓
┗━━┓┃┃━┫┏┫┗┛┣┫┃┏┓┃━━┫
┃┗━┛┃┃━┫┃┗┓┏┫┃┃┗┛┣━━┃
┗━━━┻━━┻┛╋┗┛┗┛┗━━┻━━┛
"""
print(Fore.YELLOW + logo + Fore.RESET + Back.RESET)

# Lista de serviços e portas
servicos = {
    'ftp': 21,
    'ssh': 22,
    'sql': 1433,
    'php': 80,  # PHP geralmente roda sobre o servidor web na porta 80
    'cloud': 80,  # Serviços de nuvem também geralmente usam a porta 80 para HTTP
    'http': 80,
    'https': 443,
    'smtp': 25,
    'imap': 143,
    'pop3': 110,
    'rdp': 3389,
    'telnet': 23,
    'ldap': 389,
    'mysql': 3306,
    'postgresql': 5432,
    'mongodb': 27017,
    'redis': 6379
}

# Função para verificar o serviço
def verificar_servico(host):
    for servico, porta in servicos.items():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout de 1 segundo para a conexão
        try:
            if sock.connect_ex((host, porta)) == 0:
                print(Fore.GREEN + f"O site {host} está usando {servico} na porta {porta}.")
            else:
                print(Fore.RED + f"O site {host} não está usando {servico}.")
        except socket.gaierror:
            print(f"Não foi possível resolver o host: {host}")
        finally:
            sock.close()

# Entrada do usuário
host = input("Digite o site que deseja verificar: ")
verificar_servico(host)

while True:
    resposta = input(Fore.YELLOW + "Digite 'sair' para encerrar loop: ")
    if resposta == 'sair':
        break
    print("Você digitou:", resposta)
