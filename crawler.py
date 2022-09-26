import requests
from bs4 import BeautifulSoup

DOMINIO = 'https://django-anuncios.solyd.com.br'
URL_AUTOMOVEIS = 'https://django-anuncios.solyd.com.br/automoveis/'


def requisição(url):
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


def encontrar_links(soup):
    try:
        cards_pai = soup.find('div', class_='ui three doubling link cards')
        cards = cards_pai.find_all('a')
    except:
        print('Erro ao encontar links')
        return None
    
    links = []
    for card in cards:
        try:
            link = card['href']
            links.append(link)
        except:
            pass

    return links


def encontrar_telefone(soup):
    try:
        descricao = soup.find_all('div', class_='sixteen wide column')[2].p.get_text().strip()
    except:
        print("Erro ao encontrar descrição")
        return None
    
    print(descricao)


resposta_busca = requisição(URL_AUTOMOVEIS)
if resposta_busca:
    soup_busca = parsing(resposta_busca)
    if soup_busca:
        links = encontrar_links(soup_busca)
        resposta_anuncio = requisição(DOMINIO + links[0])
        if resposta_anuncio:
            soup_anuncio = parsing(resposta_anuncio)
            if soup_anuncio:
                encontrar_telefone(soup_anuncio)