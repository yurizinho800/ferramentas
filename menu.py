import subprocess
import os
import sys
from colorama import Fore, Back, Style, init

init(autoreset=True)

scripts = ["sql.py", "ip.py", "info.py", "ipv6.py",  "cell.py", "pesquisa.py", "porta.py", "tecno.py", "dados.py", "ajuda.py"]

sys.path.append(os.path.join(os.path.dirname(__file__), 'test'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'test', 'extras'))

def executar_script(script):
    try:
        caminho_completo_extras = os.path.join("test", "extras", script)
        if os.path.exists(caminho_completo_extras):
            subprocess.run(["python", caminho_completo_extras], check=True)
        else:
            caminho_completo_test = os.path.join("test", script)
            if os.path.exists(caminho_completo_test):
                subprocess.run(["python", caminho_completo_test], check=True)
            else:
                print(f"Script {script} não encontrado nas pastas 'extras' e 'test'")
    except subprocess.CalledProcessError:
        print(f"Erro ao executar o script {script}")

def mostrar_menu():
    while True:
        print(Fore.CYAN + "┌──────────────────────────────┐")
        print(Fore.CYAN + "│" + Fore.YELLOW + " 1 : sql.py   6 : pesquisa.py " + Fore.CYAN + "│")
        print(Fore.CYAN + "│" + Fore.YELLOW + " 2 : ip.py    7 : porta.py    " + Fore.CYAN + "│")
        print(Fore.CYAN + "│" + Fore.YELLOW + " 3 : info.py  8 : tecno.py    " + Fore.CYAN + "│")
        print(Fore.CYAN + "│" + Fore.YELLOW + " 4 : ipv6.py  9 : dados.py    " + Fore.CYAN + "│")
        print(Fore.CYAN + "│" + Fore.YELLOW + " 5 : cell.py  10 : ajuda.py   " + Fore.CYAN + "│")
        print(Fore.CYAN + "│" + Fore.RED + " 0 : Sair                     " + Fore.CYAN + "│")
        print(Fore.CYAN + "└──────────────────────────────┘")
        print(Fore.GREEN + "Escolha um dos scripts acima:")

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

mostrar_menu()