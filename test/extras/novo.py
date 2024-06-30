import colorama
from colorama import Fore,Back,Style
import requests
from bs4 import BeautifulSoup
import re # importe a biblioteca re

print(Fore.YELLOW + "-------------------------------------------------------")

# Defina a função do módulo de extração de e-mails
def extracao_emails(urls):
    # Crie uma lista vazia para armazenar os resultados
    resultados = []
    # Itere sobre a lista de URLs
    for url in urls:
        # Faça a requisição para a URL do site
        res = requests.get(url)
        # Verifique se a resposta foi bem-sucedida
        if res.status_code == 200:
            # Crie o objeto BeautifulSoup a partir do conteúdo da resposta
            soup = BeautifulSoup(res.text, "html.parser")
            # Encontre todos os elementos HTML que contêm links de e-mail
            emails = soup.find_all("a", href=lambda x: x and x.startswith("mailto:"))
            # Extraia o texto dos links de e-mail
            emails_texto = [email.text for email in emails]
            # Adicione os e-mails extraídos à lista de resultados
            resultados.append(emails_texto)
        else:
            # Adicione uma mensagem de erro à lista de resultados
            resultados.append(Fore.RED + "Erro ao acessar o site")
    # Retorne a lista de resultados
    return resultados

# Defina a função do módulo de extração de palavras
def extracao_palavras(urls):
    # Crie uma lista vazia para armazenar os resultados
    resultados = []
    # Itere sobre a lista de URLs
    for url in urls:
        # Faça a requisição para a URL do site
        res = requests.get(url)
        # Verifique se a resposta foi bem-sucedida
        if res.status_code == 200:
            # Crie o objeto BeautifulSoup a partir do conteúdo da resposta
            soup = BeautifulSoup(res.text, "html.parser")
            # Encontre todo o texto do site
            texto = soup.get_text()
            # Use uma expressão regular para encontrar as palavras que têm escrito a localização e o Gmail
            palavras = re.findall(r"\b[A-Z][a-z]+,\s[A-Z]{2}\b|\b[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+\b", texto)
            # Adicione as palavras encontradas à lista de resultados
            resultados.append(palavras)
        else:
            # Adicione uma mensagem de erro à lista de resultados
            resultados.append(Fore.RED + "Erro ao acessar o site")
    # Retorne a lista de resultados
    return resultados

# Defina a função do módulo de extração de números
def extracao_numeros(urls):
    # Crie uma lista vazia para armazenar os resultados
    resultados = []
    # Itere sobre a lista de URLs
    for url in urls:
        # Faça a requisição para a URL do site
        res = requests.get(url)
        # Verifique se a resposta foi bem-sucedida
        if res.status_code == 200:
            # Crie o objeto BeautifulSoup a partir do conteúdo da resposta
            soup = BeautifulSoup(res.text, "html.parser")
            # Encontre todo o texto do site
            texto = soup.get_text()
            # Use uma expressão regular para encontrar todos os números
            numeros = re.findall(r"\b\d+\b", texto)
            # Adicione os números encontrados à lista de resultados
            resultados.append(numeros)
        else:
            # Adicione uma mensagem de erro à lista de resultados
            resultados.append(Fore.RED + "Erro ao acessar o site")
    # Retorne a lista de resultados
    return resultados

# Peça ao usuário que digite as URLs que ele quer extrair os contatos, separadas por vírgula
urls = input(Fore.GREEN + "Digite as URLs que você quer extrair os contatos: ")
# Converta a string de entrada em uma lista de URLs
urls = urls.split(",")
# Peça ao usuário que escolha qual opção ele quer
opcao = input(Fore.YELLOW + "Escolha uma opção: \n1 - Extrair e-mails \n2 - Extrair palavras \n3 - Extrair números \n" + Fore.RESET)
# Chame a função do módulo de extração correspondente à opção escolhida e imprima o resultado para os sites
if opcao == "1":
    print(extracao_emails(urls))
elif opcao == "2":
    print(extracao_palavras(urls))
elif opcao == "3":
    print(extracao_numeros(urls))
else:
    print(Fore.RED + "Opção inválida")
