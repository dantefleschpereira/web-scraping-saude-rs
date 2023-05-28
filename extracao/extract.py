import requests
from bs4 import BeautifulSoup

link = "https://ti.saude.rs.gov.br/covid19/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}


def extrair_dados(link, headers):
    requisicao = requests.get(link, headers=headers)
    site = BeautifulSoup(requisicao.text, "html.parser")
    confirmados = site.find(
        "div", class_="h5 mb-0 font-weight-bold text-gray-800")
    quantidade_confirmados = confirmados.get_text()
    total, variacao = quantidade_confirmados.split()
    return total, variacao


if __name__ == "__main__":

    total, variacao = extrair_dados(link, headers)

    print(f'Casos confirmados: {total}')
    print(f'Aumento de {variacao} casos')
