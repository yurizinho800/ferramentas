import subprocess
import os
import sys
from colorama import Fore, Back, Style, init

# Inicializa o Colorama
init(autoreset=True)

# Adiciona a pasta 'test' e 'extras' ao sys.path para garantir que os módulos podem ser encontrados
sys.path.append(os.path.join(os.path.dirname(__file__), 'test'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'test', 'extras'))

# Função para executar o script
def executar_script(script):
    try:
        # Tentar executar o script na pasta 'test/extras'
        caminho_completo_extras = os.path.join("test", "extras", script)
        if os.path.exists(caminho_completo_extras):
            subprocess.run(["python", caminho_completo_extras], check=True)
        else:
            # Tentar executar o script na pasta 'test'
            caminho_completo_test = os.path.join("test", script)
            if os.path.exists(caminho_completo_test):
                subprocess.run(["python", caminho_completo_test], check=True)
            else:
                print(f"Script {script} não encontrado nas pastas 'extras' e 'test'")
    except subprocess.CalledProcessError:
        print(f"Erro ao executar o script {script}")

# Função para mostrar o menu de opções
def mostrar_menu():
    while True:

        print(Fore.CYAN + "┌──────────────────────────────┐")
        print(Fore.YELLOW + "│ 1 : sql.py   6 : pesquisa.py | ")
        print(Fore.YELLOW + "│ 2 : ip.py    7 : porta.py    │ ")
        print(Fore.YELLOW + "│ 3 : info.py  8 : tecno.py    │ ")
        print(Fore.YELLOW + "│ 4 : ipv6.py  9 : dados.py    │ ")
        print(Fore.YELLOW + "│ 5 : cell.py  10 : ajuda.py   │ ")
        print(Fore.RED + "│ 0 : Sair                     │")
        print(Fore.CYAN + "└──────────────────────────────┘")
        print(Fore.GREEN + "Escolha um dos scripts acima:")

        # Solicitar a entrada do usuário
        escolha = input(Style.RESET_ALL + "Digite o número do script que deseja executar: ")

        if escolha == "0":
            print(Fore.GREEN + "Saindo...")
            break
        else:
            try:
                escolha_num = int(escolha)
                if 1 <= escolha_num <= len(scripts):
                    executar_script(scripts[escolha_num - 1])
                else:
                    print(Fore.RED + "Escolha inválida. Tente novamente.")
            except ValueError:
                print(Fore.RED + "Entrada inválida. Por favor, digite um número.")

# Lista com os nomes dos scripts
scripts = ["sql.py", "ip.py", "info.py", "ipv6.py",  "cell.py", "pesquisa.py", "porta.py", "tecno.py", "dados.py", "ajuda.py"]

# Chamar a função mostrar_menu
mostrar_menu()
