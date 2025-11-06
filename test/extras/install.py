import subprocess

def install_mtraceroute():
    try:
        subprocess.run(["pkg", "update"])
        subprocess.run(["pkg", "install", "python3-pip"])
        subprocess.run(["pip3", "install", "mtraceroute"])
        subprocess.run(["sudo", "apt", "install", "mtraceroute"])
        print("O mtraceroute foi instalado com sucesso!")
    except subprocess.CalledProcessError:
        print("Erro ao instalar o mtraceroute. Verifique se o pip3 está configurado corretamente.")

if __name__ == "__main__":
    install_mtraceroute()


import subprocess

def install_mtraceroute():
    try:
        subprocess.run(["pip", "install", "mtraceroute"], check=True)
        print("O mtraceroute foi instalado com sucesso!")
    except subprocess.CalledProcessError:
        print("Erro ao instalar o mtraceroute. Verifique se o pip está configurado corretamente.")

if __name__ == "__main__":
    install_mtraceroute()