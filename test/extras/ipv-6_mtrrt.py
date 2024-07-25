import subprocess

def get_ipv6_and_trace():
    try:
        url = input("Digite o URL ou endereço IPv6 desejado: ")

        # Obter o endereço IPv6
        addr_info = subprocess.check_output(["mtrrt", "-t", url]).decode().split()[-1]
        print(f"Endereço IPv6: {addr_info}")

        # Rastrear o endereço IPv6
        subprocess.run(["mtrrt", "-t", addr_info])
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Erro ao obter o endereço IPv6 ou rastrear.")

if __name__ == "__main__":
    get_ipv6_and_trace()
