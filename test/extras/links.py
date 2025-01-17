import requests
from bs4 import BeautifulSoup


def adicionar_https(url):
    if not url.startswith('http'):
        url = 'https://' + url
    return url

def extrair_links(url):
    try:
        url = adicionar_https(url)
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        links = []

        for link in soup.find_all('a', href=True):
            links.append(link['href'])

        return links
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar o site: {e}")
        return []

# Exemplo de uso
url = input("Digite o site: ")
links = extrair_links(url)
print("Links encontrados:")
for link in links:
    print(link)








