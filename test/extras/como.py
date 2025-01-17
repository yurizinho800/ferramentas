from colorama import Fore

def abrir_menu():
    try:
        print(Fore.WHITE + "Qual desses, não consegue usar ?")
        opcoes = [
            "ip.py",
            "número-celular",
            "tecnologia",
            "protocolo",
            "info",
            "whois",
            "keylogger"
        ]
        for i, opcao in enumerate(opcoes, start=1):
            print(f"{i}. {opcao}")

        selecao = int(input("\nEscolha uma opção (1 a 7): "))

        if selecao == 1:
            print(Fore.BLUE + "Basta inserir o domínio do site. Exemplo: www.site.com.br")
        elif selecao == 2:
            print(Fore.BLUE + "Primeiro, insira o prefixo (por exemplo: +55), depois o número.")
        elif selecao == 3:
            print(Fore.YELLOW + "Coloque o domínio do site com http ou https.")
        elif selecao == 4:
            print(Fore.BLUE + "Não é necessário incluir http ou https. Exemplo: www.site.com.")
        elif selecao == 5:
            print(Fore.BLUE + "Você pode usar o Osint para pesquisar informações como e-mails ou sites semelhantes.se deseja procurar por links, pode começar pelo ´www....com´.  já o personalizado precisa de http ou https.")
        elif selecao == 6:
            print(Fore.BLUE + "Para usar o whois, insira o domínio. Exemplo: www.site.com.br.")
        elif selecao == 7:
            print(Fore.BLUE + "na proxima atualização.")
        else:
            print(Fore.RED + "Opção inválida. Escolha um número de 1 a 7.")

    except ValueError:
        print(Fore.RED + "Erro: insira um número válido.")

# Exemplo de uso:
abrir_menu()

