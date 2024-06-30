from colorama import Fore, init
init()
init(strip=False)
print(Fore.LIGHTMAGENTA_EX +  "_" )       
print(" _                 _")
print("| |               | |")
print("| | ___   ___ __ _| |_  __")
print("| |/ _ \ / __/ _` | \ \/ /")
print("| | (_) | (_| (_| | |>  <")
print("|_|\___/ \___\__,_|_/_/\_\+ ATUALIZADO")


import phonenumbers

p = input("Digite o prefixo do país: ") # pede ao usuário que digite o prefixo
n = input("Digite o número de telefone: ") # pede ao usuário que digite o número

numero = p + n

numero_ajustado = phonenumbers.parse(numero)

phonenumbers.is_possible_number(numero_ajustado)

# Importa o módulo textwrap
import textwrap

# Define um texto longo
texto = "esse é um script, analizado e criado pelo intuito de saber da onde vem a procedencia de um número."

# Usa a função fill do módulo textwrap para ajustar o texto em 20 colunas
texto_formatado = textwrap.fill(texto, width=20)

# Imprime o texto formatado
print(texto_formatado)

# Importa o módulo timezone do pacote phonenumbers
from phonenumbers import timezone


import phonenumbers # importa o módulo phonenumbers
from phonenumbers import geocoder # importa o geocoder do phonenumbers
from phonenumbers import carrier # importa o carrier do phonenumbers
from colorama import Fore, init # importa o colorama
init(autoreset=True) # inicializa o colorama

fuso_horario = timezone.time_zones_for_number(numero_ajustado) # obtém o fuso horário do número
print(Fore.LIGHTGREEN_EX + "Fuso horário do número: " + fuso_horario[0]) # imprime o fuso horário do número

rfc3966 = phonenumbers.format_number(numero_ajustado, phonenumbers.PhoneNumberFormat.RFC3966)
print(Fore.LIGHTGREEN_EX + "Número no formato RFC3966: " + rfc3966)

def rastrear(p, n): # define a função rastrear
    print(Fore.LIGHTMAGENTA_EX + "Resultados do rastreamento:")
    numero_ajustado = phonenumbers.parse(numero)
    if phonenumbers.is_valid_number(numero_ajustado):
      va = "Verdadeiro" # atribui a variável va como "Verdadeiro"
    else:
        va = "Falso" # atribui a variável va como "Falso"
    print(Fore.LIGHTGREEN_EX + "Número válido: " + va) # imprime se o número é válido ou não
    pais = geocoder.description_for_number(numero_ajustado, "pt-br") # obtém o país do número
    print(Fore.LIGHTGREEN_EX + "País do número: " + pais) # imprime o país do número
    local = geocoder.description_for_number(numero_ajustado, "en")
    print(Fore.LIGHTGREEN_EX + "Localização do número: " + local)
    nacional = phonenumbers.format_number(numero_ajustado, phonenumbers.PhoneNumberFormat.NATIONAL) # obtém o número no formato nacional
    print(Fore.LIGHTGREEN_EX + "Número no formato nacional: " + nacional)
    internacional = phonenumbers.format_number(numero_ajustado, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    print(Fore.LIGHTGREEN_EX + "Número no formato internacional: " + internacional)
    prefixo = phonenumbers.format_number(numero_ajustado, phonenumbers.PhoneNumberFormat.E164)
    print(Fore.LIGHTGREEN_EX + "Prefixo do país: " + prefixo[:3]) # imprime o prefixo do país
    operadora = carrier.name_for_number(numero_ajustado, "pt-br") # obtém a operadora do número
    print(Fore.LIGHTGREEN_EX + "Operadora do telefone: " + operadora)
    tipo = phonenumbers.number_type(numero_ajustado) # obtém o tipo do número
    if tipo == 1: # verifica se o tipo é 1
        tipo = "Fixo" # atribui a variável tipo como "Fixo"
    elif tipo == 2: # verifica se o tipo é 2
        tipo = "Celular" # atribui a variável tipo como "Celular"
    else: # caso contrário
        tipo = "Desconhecido" # atribui a variável tipo
    print(Fore.LIGHTGREEN_EX + "Tipo de número: " + tipo) 
    

rastrear(p, n) 
