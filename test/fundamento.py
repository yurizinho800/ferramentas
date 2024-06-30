# tech_checker.py
import colorama
from colorama import Fore, Back, Style

# Resto do seu código...

print(colorama.Fore.MAGENTA + "--------𝖋𝖚𝖓𝖉𝖆𝖒𝖊𝖓𝖙𝖔--------")

import requests
from bs4 import BeautifulSoup

def obter_tecnologias(site_url):
    try:
        response = requests.get(site_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            tecnologias = set()

            # Exemplos de tecnologias que você pode procurar
            palavras_chave = ["wholshostingthis", "buildwith", "wappalyzer", "cloud", "wordpress", "django", "react", "angular", "vue"]

            for palavra in palavras_chave:
                if palavra in soup.text.lower():
                    tecnologias.add(palavra)

            return tecnologias
        else:
            return None
    except requests.RequestException:
        return None

if __name__ == "__main__":
    site_digitado = input("Digite a URL do site com https:// ou http:// que deseja verificar: ")
    tecnologias_encontradas = obter_tecnologias(site_digitado)

    if tecnologias_encontradas:
        print("Tecnologias encontradas no site:")
        for tecnologia in tecnologias_encontradas:
            print(tecnologia)
    else:
        print("Não foi possível acessar o site ou não foram encontradas tecnologias.")
