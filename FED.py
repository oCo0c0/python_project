import requests
from bs4 import BeautifulSoup


def get_exchange_rate():
    url = "https://www.federalreserve.gov/releases/h10/20231218/"
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, "html.parser")
    rows = soup.find_all('tr')

    for row in rows:
        cells = row.find_all(['th', 'td'])
        for cell in cells:
            print(cell.text.strip())
        print('---')

exchange_rate = get_exchange_rate()