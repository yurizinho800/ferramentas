import socket
import ipaddress
import subprocess

while True:
    opcao = input("Digite 1 para obter o IP, 2 para rastrear ou 3 para sair: ")

    if opcao == "1":
        url = input("Digite o URL do site desejado: ")
        try:
            # Obtém informações de endereço para o URL
            addr_info = socket.getaddrinfo(url, None, socket.AF_INET6)
            for info in addr_info:
                family, _, _, _, address = info
                if family == socket.AF_INET6:
                    ipv6_address = ipaddress.ip_address(address[0])
                    print(f"Endereço IPv6 do {url}: {ipv6_address}")
                    break
            else:
                print(f"Não foi possível encontrar um endereço IPv6 para {url}.")
        except (socket.gaierror, ValueError):
            print(f"Erro ao obter o endereço IPv6 para {url}.")
    elif opcao == "2":
        # Obtendo as informações do IP
        ip = input("Digite o IP que você quer rastrear: ")
        try:
            # Rastreia o endereço IPv6 usando o comando traceroute
            subprocess.run(["traceroute", "-6", "-I", str(ip)])
        except (subprocess.CalledProcessError, FileNotFoundError):
            print(f"Erro ao rastrear o endereço IPv6 {ip}.")
    elif opcao == "3":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Digite 1, 2 ou 3.")

