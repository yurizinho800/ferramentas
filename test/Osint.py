
from colorama import Fore,Back,Style
from extras import *
import extras.exemplo
import extras.novo
import extras.modulo

print(Fore.BLUE + 
      ".___________________.")
print(f"|{Fore.YELLOW} ATENÇÃO{Fore.BLUE}           |        ^")
print("|                   |        |")
print("|resultado acima    |        |")
print("|                   |        |")
print("|arrasta para cima  |        |")
print("|___________________|")

def continuar():
  continuar = int(1)
  return continuar

def sair():
  sair = int(2)
  return sair

if __name__ == '__main__':
  continuar()
  sair()
print(input(Fore.GREEN + "clica em enter para sair:.."))
