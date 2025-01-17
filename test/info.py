# /home/kali/ferramentas/test/info2.py

import subprocess
from colorama import Fore, Style
import os

def menu():
    print(Style.RESET_ALL + "Voçê quer as informações de:")
    print(Fore.GREEN + "1 - todos os links")
    print(Style.RESET_ALL + "ou")
    print(Fore.GREEN + "2 - personalizado")
    escolha = input(Style.RESET_ALL + "Digite o número :  ")

    # Caminho absoluto da pasta extras
    extras_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'extras')
    
    if escolha == "1":
        # Ajuste o caminho para apontar corretamente para 'test/extras/links.py'
        script_path = os.path.join(extras_dir, 'links.py')
        subprocess.run(["python", script_path])
    elif escolha == "2":
        # Ajuste o caminho para apontar corretamente para 'test/extras/extrair.py'
        script_path = os.path.join(extras_dir, 'extrair.py')
        subprocess.run(["python", script_path])
    else:
        print(Fore.RED + "Escolha inválida, por favor tente novamente.")
        menu()  # Chama a função menu() novamente

# Chama a função menu() se este arquivo for executado diretamente
if __name__ == "__main__":
    menu()
