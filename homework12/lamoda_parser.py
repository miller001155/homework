import json

import requests
from bs4 import BeautifulSoup

JSON = 'cards.json'
HOST = 'https:www.lamoda.by/'
URL = ''
HEADERS = {
    'accept': '',
    'user-agent': ''
}


def get_html(url, params=''):
    request = requests.get(url, headers=HEADERS, params=params)
    return request


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', 'class=')
    cards = []
    for item in items:
        cards.append(
            {
                'title': item.find('div', 'class=''').get_text(),
                'brand': item.find('div', 'class=''').get_text(),
                'price': item.find('div', 'class=''').get_text(strip=True),

            }
        )
    return cards


def save_doc(items, path):
    with open(path, 'w') as file:
        json.dump(items, file, indent=3, ensure_ascii=False)


def parser():
    PAGENATION = int(input('Укажите количество страниц: ').strip())
    html = get_html(URL)
    if html.status_code == 200:
        cards = []
        for page in range(1, PAGENATION + 1):
            html = get_html(URL, params={'page': page})
            cards.extend(get_content(html.text))
            print(f'Спарсена страница: {page}')
            save_doc(cards, JSON)


if __name__ == '__main__':
    parser()
