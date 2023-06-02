import requests
from bs4 import BeautifulSoup

link = "https://ti.saude.rs.gov.br/covid19/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}


def extrair_casos_confirmados(link, headers):
    requisicao = requests.get(link, headers=headers)
    site = BeautifulSoup(requisicao.text, "html.parser")
    confirmados = site.find(
        "div", class_="h5 mb-0 font-weight-bold text-gray-800")
    quantidade_confirmados = confirmados.get_text()
    total, variacao = quantidade_confirmados.split()
    return total, variacao


def extrair_incidencia(link, headers):
    requisicao = requests.get(link, headers=headers)
    site = BeautifulSoup(requisicao.text, "html.parser")
    incidencia = site.find_all(
        "div", class_="h5 mb-0 font-weight-bold text-gray-800")
    total_incidencia = incidencia[1].get_text()
    return total_incidencia


def taxa_ocupacao_leitos(link, headers):
    requisicao = requests.get(link, headers=headers)
    site = BeautifulSoup(requisicao.text, "html.parser")
    tx_ocupacao = site.find_all(
        "div", class_='h5 mb-0 mr-3 font-weight-bold text-gray-800')
    qtd_ocupacao = tx_ocupacao[0].get_text()
    hospitalizacoes = tx_ocupacao[1].get_text()
    return qtd_ocupacao, hospitalizacoes


if __name__ == "__main__":

    total_confirmados, variacao_confirmados = extrair_casos_confirmados(
        link, headers)
    total_incidencia = extrair_incidencia(link, headers)
    tx_ocupacao, hospitalizacoes = taxa_ocupacao_leitos(link, headers)

    print('\n-=-=-=-=-Painel Coronavírus RS-=-=-=-=-')
    print(f'\nCasos confirmados: {total_confirmados}')
    print(f'Aumento de {variacao_confirmados} casos')
    print(f'Incidência {total_incidencia}')
    print(f'Taxa de ocupação de leitos: {tx_ocupacao}')
    print(f'Hospitalizações: {hospitalizacoes}')
    print('\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')
