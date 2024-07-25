# Importando as bibliotecas necessárias
import requests
from bs4 import BeautifulSoup
from colorama import Fore, init

# Inicializando o colorama
init()

# Definindo uma função que recebe uma URL e retorna o domínio
def get_domain(url):
  # Removendo o protocolo (http:// ou https://)
  url = url.replace("http://", "").replace("https://", "")
  # Dividindo a URL pelo caractere /
  parts = url.split("/")
  # Retornando a primeira parte, que é o domínio
  return parts[0]

# Definindo uma função que recebe uma URL e retorna uma lista de links encontrados na página
def get_links(url):
  # Fazendo uma requisição HTTP para a URL
  response = requests.get(url)
  # Verificando se a requisição foi bem sucedida
  if response.status_code == 200:
    # Criando um objeto BeautifulSoup com o conteúdo HTML da resposta
    soup = BeautifulSoup(response.text, "html.parser")
    # Criando uma lista vazia para armazenar os links
    links = []
    # Encontrando todas as tags <a> que tenham o atributo href
    for a in soup.find_all("a", href=True):
      # Adicionando o valor do atributo href à lista de links
      links.append(a["href"])
    # Retornando a lista de links
    return links
  else:
    # Retornando uma lista vazia em caso de erro
    return []

# Pedindo ao usuário que digite uma URL
url = input(Fore.BLUE + "Digite uma URL com o https://:..  ")

# Chamando a função get_links para obter uma lista de links da URL digitada
links = get_links(url)

# Imprimindo o domínio da URL digitada em amarelo
print(Fore.YELLOW + get_domain(url))

# Percorrendo a lista de links
for link in links:
  # Imprimindo o domínio de cada link em amarelo
  print(Fore.YELLOW + get_domain(link))

