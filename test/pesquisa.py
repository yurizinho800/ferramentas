import requests
from bs4 import BeautifulSoup
import colorama

# Inicializa o colorama para usar cores no terminal
colorama.init(autoreset=True)

# Dicionário com os sites que permitem scraping
sites = {
    "Ichi.pro": "https://ichi.pro/pt/search?q="
}

# Lista com os nomes dos sites em ordem alfabética
nomes = sorted(sites.keys())

# Exibe os sites disponíveis para o usuário escolher
print(colorama.Fore.BLUE + "Escolha um dos sites abaixo para pesquisar:\n")
for i, nome in enumerate(nomes, start=1):
    print(f"{i}. {nome}")
print(colorama.Style.RESET_ALL)

# Recebe a escolha do usuário
site = input("Digite o número do site que você quer pesquisar: \n")
termo = input("Digite o termo que você quer pesquisar: \n")

try:
    # Converte a escolha em índice e obtém o nome e URL
    indice = int(site) - 1
    nome = nomes[indice]
    url = sites[nome]

    # Define cabeçalho para simular navegador
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    # Faz a requisição HTTP
    response = requests.get(url + termo, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # Seleciona títulos de artigos
    titulos = soup.select("h2, h3")
    count = 1

    # Exibe os títulos encontrados
    for titulo in titulos:
        texto = titulo.get_text(strip=True)
        if texto:
            print(colorama.Back.GREEN + f"{count}. {texto}" + colorama.Style.RESET_ALL)
            count += 1

    if count == 1:
        print("Nenhum resultado relevante encontrado.")

except (ValueError, IndexError):
    print("Site inválido. Tente novamente.")

# Loop para encerrar o programa
while True:
    resposta = input("Digite 'sair' para encerrar o loop: ")
    if resposta.lower() == 'sair':
        break
    print("Você digitou:", resposta)