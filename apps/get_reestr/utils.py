from bs4 import BeautifulSoup as Bs
from datetime import datetime

import requests


def get_date_from_html(url: str):
    page = requests.get(url)  # Получаем страницу
    soup = Bs(page.text, 'html.parser')
    rows = soup.findAll('tr', class_='b-table__row')

    date = rows[14].findAll('td', class_='b-table__cell')[2]['content']  # возвращает дату последнего изменения yyyy-mm-dd

    date = datetime.strptime(date, '%Y-%m-%d')  # конвертируем строку в объект класса datetime

    return date

