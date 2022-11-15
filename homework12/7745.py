import requests
from bs4 import BeautifulSoup
import json

JSON = '7745.json'
HOST = 'https://7745.by/'
URL = 'https://7745.by/catalog/mikrovolnovye-pechi-vstraivaemye'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0'
}


def get_html(url, params=''):
    request = requests.get(url, headers=HEADERS, params=params)
    return request


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_="catalog-item__wrapper")
    cards = []
    for item in items:
        cards.append(
            {
                'title': item.find('div', class_='item-block_text').get_text(),
                'description': item.find('a', class_='item-block_name item-block_name--tile').get_text(),
                'price': item.find('div', class_='item-block_main-price-block').get_text(strip=True),

    }
    )
    return cards


def save_doc(items, path):
    with open(path, 'w') as file:
        json.dump(items, file, indent=4, ensure_ascii=False)


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
