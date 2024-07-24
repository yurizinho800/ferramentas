import subprocess
import os

from colorama import Fore, Style

print("███████▓█████▓▓╬╬╬╬╬╬╬╬▓███▓╬╬╬╬╬╬╬▓╬╬▓█")
print("████▓▓▓▓╬╬▓█████╬╬╬╬╬╬███▓╬╬╬╬╬╬╬╬╬╬╬╬╬█")
print("███▓▓▓▓╬╬╬╬╬╬▓██╬╬╬╬╬╬▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█")
print("████▓▓▓╬╬╬╬╬╬╬▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█")
print("███▓█▓███████▓▓███▓╬╬╬╬╬╬▓███████▓╬╬╬╬▓█")
print("████████████████▓█▓╬╬╬╬╬▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬█")
print("███▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█")
print("████▓▓▓▓▓▓▓▓▓▓▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█")
print("███▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█")
print("█████▓▓▓▓▓▓▓▓█▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█")
print("█████▓▓▓▓▓▓▓██▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██")
print("█████▓▓▓▓▓████▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██")
print("████▓█▓▓▓▓██▓▓▓▓██╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██")
print("████▓▓███▓▓▓▓▓▓▓██▓╬╬╬╬╬╬╬╬╬╬╬╬█▓╬▓╬╬▓██")
print("█████▓███▓▓▓▓▓▓▓▓████▓▓╬╬╬╬╬╬╬█▓╬╬╬╬╬▓██")
print("█████▓▓█▓███▓▓▓████╬▓█▓▓╬╬╬▓▓█▓╬╬╬╬╬╬███")
print("██████▓██▓███████▓╬╬╬▓▓╬▓▓██▓╬╬╬╬╬╬╬▓███")
print("███████▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬████")
print("███████▓▓██▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓████")
print("████████▓▓▓█████▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█████")
print("█████████▓▓▓█▓▓▓▓▓███▓╬╬╬╬╬╬╬╬╬╬╬▓██████")
print("██████████▓▓▓█▓▓▓▓▓██╬╬╬╬╬╬╬╬╬╬╬▓███████")
print("███████████▓▓█▓▓▓▓███▓╬╬╬╬╬╬╬╬╬▓████████")
print("██████████████▓▓▓███▓▓╬╬╬╬╬╬╬╬██████████")
print("███████████████▓▓▓██▓▓╬╬╬╬╬╬▓███████████")

# Função para executar o script
def executar_script(script):
    try:
        subprocess.run(["python", script], check=True)
    except subprocess.CalledProcessError:
        print(f"Erro ao executar o script {script}")

# Função para mostrar o menu de opções
def mostrar_menu():
    print(Fore.GREEN + "Escolha um dos scripts abaixo:")
    for i, script in enumerate(scripts):
        print(f"{i + 1} - {script}")
    print(Fore.RED + "0 - Sair" + Fore.RESET)
# Lista com os nomes dos scripts
scripts = ["ip.py", "Osint.py", "whois.py", "fundamento.py",  "número-celular.py", "pesquisa.py", "portas_e_serviços.py", "ajuda.py"]

# Caminho para a pasta "test"
pasta_test = "test"



# Loop para repetir o menu até o usuário sair
while True:
    mostrar_menu()
    opcao = input("Digite o número da opção: ")
    if opcao.isdigit() and 0 <= int(opcao) <= len(scripts):
        opcao = int(opcao)
        if opcao == 0:
            print(Fore.YELLOW + "Programa finalizado")
            break
        else:
            script = scripts[opcao - 1]
            print(f"Executando o script {script}")
            executar_script(os.path.join(pasta_test, script))
    else:
        print(Fore.RED + "Opção inválida, tente novamente")



