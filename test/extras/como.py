from colorama import Fore

def abrir_menu():
    try:
        print(Fore.WHITE + "Qual desses, não consegue usar ?")
        opcoes = [
            "ip.py",
            "número-celular",
            "tecnologia",
            "ipv6",
            "info",
            "portas",
            "pesquisa",
            "dados",
            "sql"
        ]
        for i, opcao in enumerate(opcoes, start=1):
            print(f"{i}. {opcao}")

        selecao = int(input("\nEscolha uma opção (1 a 9): "))

        if selecao == 1:
            print(Fore.BLUE + "Basta inserir o domínio do site. Exemplo: www.site.com.br")
        elif selecao == 2:
            print(Fore.BLUE + "Primeiro, insira o prefixo (por exemplo: +55), depois o número.")
        elif selecao == 3:
            print(Fore.YELLOW + "Coloque o domínio do site com http ou https.")
        elif selecao == 4:
            print(Fore.BLUE + "ainda em desenvolvimento.")
        elif selecao == 5:
            print(Fore.BLUE + "Você pode usar o Osint para pesquisar informações como e-mails ou sites semelhantes.se deseja procurar por links, pode começar pelo ´www....com´.  já o personalizado precisa de http ou https.")
        elif selecao == 6:
            print(Fore.BLUE + "não precisa usar protocolos, apenas o domínio")
        elif selecao == 7:
            print(Fore.BLUE + "por enquanto essa opção só pode ser usada no linux.")
        elif selecao == 8:
            print(Fore.BLUE + "Para usar o whois, insira o domínio. Exemplo: www.site.com.br.")
        elif selecao == 9:
            print(Fore.BLUE + "usa-se protocolo http ou https.")
        else:
            print(Fore.RED + "Opção inválida. Escolha um número de 1 a 9.")

    except ValueError:
        print(Fore.RED + "Erro: insira um número válido.")


abrir_menu()

