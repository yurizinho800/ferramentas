
# importa as bibliotecas
import requests
from bs4 import BeautifulSoup
import colorama # importa a biblioteca colorama

# cria um dicionário com os nomes e as URLs dos sites que você quer buscar
sites = {"Google": "https://www.google.com/search?q=",
         "Gmail": "https://www.gmail.com/search?q=",
         "Instagram": "https://www.instagram.com/search?q=",
         "Facebook": "https://www.facebook.com/search?=q",
         "Ichi.pro": "https://ichi.pro/pt/search?q="}

# cria uma lista com os nomes dos sites em ordem alfabética
nomes = sorted(sites.keys())

# imprime os nomes dos sites com números para o usuário escolher
print(colorama.Fore.MAGENTA + "Escolha um dos sites abaixo para pesquisar:\n")
for i, nome in enumerate(nomes, start=1):
    print(f"{i}. {nome}")
print(colorama.Style.RESET_ALL)

# pergunta ao usuário qual site e qual termo de pesquisa ele quer usar
site = input("Digite o número do site que você quer pesquisar: \n")
termo = input("Digite o termo que você quer pesquisar: \n")

# verifica se o site escolhido é válido
try:
    # converte o número do site em um índice da lista de nomes
    indice = int(site) - 1
    # obtém o nome do site correspondente ao índice
    nome = nomes[indice]
    # obtém a URL do site correspondente ao nome
    url = sites[nome]
    # faz a requisição para a URL
    response = requests.get(url + termo)
    # cria a variável soup usando o objeto BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    # extrai os dados que quiser do site, como o título, o snippet, a url, etc.
    # usa um seletor CSS mais genérico para encontrar os elementos que contêm os títulos dos artigos
    titles = soup.select("h1, h2, h3, h4, h5, h6")
    # cria uma variável para numerar os resultados
    count = 1
    # faz um loop sobre os títulos encontrados
    for title in titles:
        text = title.string
        # imprime o número e o texto do resultado com a margem verde
        print(colorama.Back.GREEN + str(count) + ". " + text + colorama.Style.RESET_ALL)
        # incrementa o contador
        count += 1
except (ValueError, IndexError):
    # imprime uma mensagem de erro se o site não for válido
    print("Site inválido. Tente novamente.")


