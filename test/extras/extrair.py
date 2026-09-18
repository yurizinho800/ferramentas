import requests
from bs4 import BeautifulSoup
import re
from colorama import Fore, Style

print(Fore.YELLOW + "┌--------------------------------------------------------┐")

# Função para extrair e-mails
def extracao_emails(urls):
    resultados = []
    for url in urls:
        try:
            res = requests.get(url, timeout=10)
            if res.status_code == 200:
                soup = BeautifulSoup(res.text, "html.parser")

                # Captura links mailto
                emails_mailto = [a["href"].replace("mailto:", "") 
                                 for a in soup.find_all("a", href=lambda x: x and x.startswith("mailto:"))]

                # Captura e-mails no texto da página
                emails_texto = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", res.text)

                encontrados = list(set(emails_mailto + emails_texto))
                resultados.extend(encontrados)
            else:
                resultados.append(Fore.RED + f"Erro ao acessar {url}")
        except Exception as e:
            resultados.append(Fore.RED + f"Erro em {url}: {e}")
    return resultados

# Função para extrair palavras (exemplo: localidades e e-mails)
def extracao_palavras(urls):
    resultados = []
    for url in urls:
        try:
            res = requests.get(url, timeout=10)
            if res.status_code == 200:
                soup = BeautifulSoup(res.text, "html.parser")
                texto = soup.get_text()

                # Localidades tipo "Cidade, UF" ou e-mails
                palavras = re.findall(r"\b[A-Z][a-z]+,\s[A-Z]{2}\b|[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", texto)
                resultados.extend(palavras)
            else:
                resultados.append(Fore.RED + f"Erro ao acessar {url}")
        except Exception as e:
            resultados.append(Fore.RED + f"Erro em {url}: {e}")
    return resultados

# Função para extrair números
def extracao_numeros(urls):
    resultados = []
    for url in urls:
        try:
            res = requests.get(url, timeout=10)
            if res.status_code == 200:
                soup = BeautifulSoup(res.text, "html.parser")
                texto = soup.get_text()

                # Captura números inteiros
                numeros = re.findall(r"\b\d+\b", texto)
                resultados.extend(numeros)
            else:
                resultados.append(Fore.RED + f"Erro ao acessar {url}")
        except Exception as e:
            resultados.append(Fore.RED + f"Erro em {url}: {e}")
    return resultados

# Entrada do usuário
urls = input(Fore.GREEN + "Digite as URLs separadas por vírgula: ").split(",")

opcao = input(
    Fore.YELLOW + "Escolha uma opção:\n"
    "1 - Extrair e-mails\n"
    "2 - Extrair palavras\n"
    "3 - Extrair números\n"
    "4 - Extrair tudo\n" + Style.RESET_ALL
)

# Execução conforme escolha
if opcao == "1":
    print("E-mails encontrados:", extracao_emails(urls))
elif opcao == "2":
    print("Palavras encontradas:", extracao_palavras(urls))
elif opcao == "3":
    print("Números encontrados:", extracao_numeros(urls))
elif opcao == "4":
    print("E-mails:", extracao_emails(urls))
    print("Palavras:", extracao_palavras(urls))
    print("Números:", extracao_numeros(urls))
else:
    print(Fore.RED + "Opção inválida")
