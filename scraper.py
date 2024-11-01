import requests
from bs4 import BeautifulSoup
import json

base_url = "https://quotes.toscrape.com/"

all_quotes_info = []

url = base_url

while url:

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    quotes = soup.find_all('div', class_='quote')

    for quote in quotes:
        text = quote.find('span', class_='text').get_text(strip=True)

        author = quote.find('small', class_='author').get_text(strip=True)

        tags = [tag.get_text(strip=True) for tag in quote.find_all('a', class_='tag')]

        all_quotes_info.append({
            "text": text,
            "author": author,
            "tags": tags
        })

    # Проверяем наличие следующей страницы
    next_button = soup.find('li', class_='next')
    url = base_url + next_button.find('a')['href'] if next_button else None

print(json.dumps(all_quotes_info, indent=4, ensure_ascii=False))