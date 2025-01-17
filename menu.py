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
        print(Fore.GREEN + "Escolha um dos scripts abaixo:")
        linha_tamanho = 40  # Tamanho da linha do quadrado
        print(Back.BLACK + Fore.RED + "┌" + "─" * linha_tamanho + "┐" )

        # Exibir os primeiros 5 scripts na primeira coluna
        for i in range(5):
            numero = Fore.GREEN + str(i + 1)  # Número em verde
            nome_script = Fore.BLUE + scripts[i]  # Script em azul
            conteudo = f"{numero} : {nome_script}"
            espacos_faltantes = linha_tamanho - len(conteudo) - 1
            linha = f"│ {conteudo}" + " " * espacos_faltantes 
            # Verificar se há scripts restantes para a segunda coluna
            if i + 5 < len(scripts):
                numero2 = Fore.GREEN + str(i + 6)
                nome_script2 = Fore.BLUE + scripts[i + 5]
                conteudo2 = f"{numero2} : {nome_script2}"
                espacos_faltantes2 = linha_tamanho - len(conteudo2) - 1
                linha2 = f" {conteudo2}" + " " * espacos_faltantes2 
                print(Back.BLACK + Fore.RED + linha + " " + Back.BLACK + Fore.RED + linha2)
            else:
                print(Back.BLACK + Fore.RED + linha)

        saida = Fore.GREEN + "0"
        linha_saida = f"│ {saida} : Sair" + " " * (linha_tamanho - len(f"0 : Sair"))
        print(Back.BLACK + Fore.RED + linha_saida)
        
        print(Back.BLACK + Fore.RED + "└" + "─" * linha_tamanho + "┘" + Fore.RESET)
        
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
