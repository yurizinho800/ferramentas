import subprocess
import os

from colorama import Fore, Style


# Função para executar o script
def executar_script(script):
    try:
        subprocess.run(["python", script], check=True)
    except subprocess.CalledProcessError:
        print(f"Erro ao executar o script {script}")

# Função para mostrar o menu de opções
def mostrar_menu():
    print(Fore.YELLOW + "_______________________________________________________________________")
    print(Fore.YELLOW + "|Para usar o ipv-6_mtrrt.py é nescessario usar o kali linux ou umbunto|" )
    print(Fore.YELLOW + "-----------------------------------------------------------------------")
    print(Fore.GREEN + "caso contrario pode usar o ipv-6")
    for i, script in enumerate(scripts):
        line_length = len(script) + 6  # Tamanho do nome do script + espaços e b>
        print(f"┌{'─' * line_length}┐")
        print(f"│ {i + 1} : {script} │")
        print(f"└{'─' * line_length}┘")
    print(Fore.RED + "0 - Sair" + Fore.RESET)

# Lista com os nomes dos scripts
scripts = ["install.py", "ipv-6.py", "ipv-6_mtrrt.py"]

# Caminho para a pasta "test"
pasta_extras = "test/extras" 



# Loop para repetir o menu até o usuário sair
while True:
    mostrar_menu()
    opcao = input("Digite o número da opção: ")
    if opcao.isdigit() and 0 <= int(opcao) <= len(scripts):
        opcao = int(opcao)
        if opcao == 0:
            print(Fore.BLUE  + "Programa finalizado")
            break
        else:
            script = scripts[opcao - 1]
            print(f"Executando o script {script}")
            executar_script(os.path.join(pasta_extras, script))
    else:
        print("Opção inválida, tente novamente")
