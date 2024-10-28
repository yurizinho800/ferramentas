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
    print(Fore.GREEN + "Escolha um dos scripts abaixo:")
    linha_tamanho = 40  # Tamanho da linha do quadrado
    print("┌" + "─" * linha_tamanho + "┐")

    for i, script in enumerate(scripts):
        print(f"│ {i + 1} : {script}*" + " " * (linha_tamanho - len(f"{i + 1} : {script}*")) + "│")

    print(f"│ {0} : Sair" + " " * (linha_tamanho - len(f"{0} : Sair")) + "│")
    print("└" + "─" * linha_tamanho + "┘" + Fore.RESET)
# Lista com os nomes dos scripts
scripts = ["sql.py", "ip.py", "Osint.py", "whois.py", "fundamento.py",  "número-celular.py", "pesquisa.py", "portas_e_serviços.py", "ajuda.py", "ipv6.py"]

# Caminho para a pasta "test"
pasta_test = "test"



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
            executar_script(os.path.join(pasta_test, script))
    else:
        print("Opção inválida, tente novamente")



