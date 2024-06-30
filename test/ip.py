from colorama import init, Fore, Back, Style
init()
logo = ("""
░ ▄ ▀ 　▀ █ ▀ 　█ ▀ ▀ █ 　▀ █ ░ █ ▀ 　░ █ ▀ █ ░ 　▀ ▄ ░ 　
█ ░ ░ 　▒ █ ░ 　█ ░ ░ █ 　░ █ ▄ █ ░ 　█ ▄ ▄ █ ▄ 　░ ░ █ 　
░ ▀ ▄ 　▄ █ ▄ 　█ ▀ ▀ ▀ 　░ ░ ▀ ░ ░ 　░ ░ ░ █ ░ 　▄ ▀ ░ 　
""")

script = "qual é o site que você quer rastrear?"
print(Fore.RED + logo + Fore.RESET + Back.RESET)
print(Fore.RED + script + Fore.RESET)

# Removendo a interface de linha de comando usando o módulo argparse
# import argparse # Não precisa mais disso

import socket
import requests
import json

# Criando um loop para perguntar ao usuário o que ele quer fazer
while True:
    opcao = input(" Digite 1 para obter o IP, 2 para rastrear ou 3 para sair: ")

    if opcao == "1":
        # Obtendo o IP do domínio
        dominio = input("Digite o domínio do site que você quer obter o IP: ")
        try:
            ip = socket.gethostbyname(dominio)
            # Desenhando o quadrado com o resultado
            print(Fore.GREEN + "┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐")
            print(f"│ O IP do site {dominio} é {ip}                                                                                                        │")
            print("└──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘" + Fore.RESET)
        except:
            print(Fore.GREEN + f"Não foi possível obter o IP do site {dominio}" + Fore.RESET)
    elif opcao == "2":
        # Obtendo as informações do IP
        ip = input("Digite o IP que você quer rastrear: ")
        try:
            response = requests.get("http://ip-api.com/json/" + ip)
            data = response.json()
            json_string = json.dumps(data, indent=4, ensure_ascii=False)
            # Desenhando o quadrado com o resultado
            print(Fore.GREEN + "┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐")
            print(f"│ {json_string}                                                                                                                        │")
            print("└──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘" + Fore.RESET)
        except:
            print(Fore.GREEN + f"Não foi possível obter as informações do IP {ip}" + Fore.RESET)
    elif opcao == "3":
        # Saindo do loop e do script
        print(Fore.GREEN + "Obrigado por usar o rastreador de IP. Até mais!" + Fore.RESET)
        break
    else:
        # Mostrando uma mensagem de erro se a opção digitada não for válida
        print(Fore.GREEN + "Você precisa digitar uma opção válida. Digite 1 para obter o IP, 2 para rastrear ou 3 para sair." + Fore.RESET)































