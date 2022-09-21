import requests
from bs4 import BeautifulSoup

URL_AUTOMOVEIS = 'https://django-anuncios.solyd.com.br/automoveis/'


def buscar(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return resposta.text
        else:
            print('Erro ao fazer requisição')
    except Exception as error:
        print('Erro ao fazer requisição')
        print(error)

def parsing(resposta_html):
    try:
        soup = BeautifulSoup(resposta_html, 'html.parser')
        return soup
    except Exception as error:
        print('Erro ao fazer parsing HTML')
        print(error)


resposta = buscar(URL_AUTOMOVEIS)
if resposta:
    soup = parsing(resposta)