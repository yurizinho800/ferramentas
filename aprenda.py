import subprocess
import os

# Função para executar o script
def executar_script(script):
    try:
        subprocess.run(["python", script], check=True)
    except subprocess.CalledProcessError:
        print(f"Erro ao executar o script {script}")

# Função para mostrar o menu de opções
def mostrar_menu():
    print("Escolha um dos scripts abaixo:")
    for i, script in enumerate(scripts):
        print(f"{i + 1} - {script}")
    print("0 - Sair")

# Lista com os nomes dos scripts
scripts = ["Osint.py", "número-celular.py", "pesquisa.py"]

# Caminho para a pasta "test"
pasta_test = "test"

# Verifica se a pasta "test" existe
if os.path.exists(pasta_test):
    # Lista os arquivos na pasta "test"
    arquivos_test = os.listdir(pasta_test)
    # Filtra apenas os arquivos que correspondem aos nomes dos módulos
    modulos_encontrados = [arquivo for arquivo in arquivos_test if arquivo in scripts]
    if modulos_encontrados:
        print(f"Módulos encontrados na pasta 'test': {', '.join(modulos_encontrados)}")
    else:
        print("Nenhum módulo encontrado na pasta 'test'.")
else:
    print("A pasta 'test' não existe.")

# Loop para repetir o menu até o usuário sair
while True:
    mostrar_menu()
    opcao = input("Digite o número da opção: ")
    if opcao.isdigit() and 0 <= int(opcao) <= len(scripts):
        opcao = int(opcao)
        if opcao == 0:
            print("Programa finalizado")
            break
        else:
            script = scripts[opcao - 1]
            print(f"Executando o script {script}")
            executar_script(os.path.join(pasta_test, script))
    else:
        print("Opção inválida, tente novamente")



