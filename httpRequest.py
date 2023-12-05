import requests
from bs4 import BeautifulSoup


def get_exchange_rate(date):
    url = "https://www.cnb.cz/en/financial-markets/foreign-exchange-market/central-bank-exchange-rate-fixing/central-bank-exchange-rate-fixing/"
    response = requests.get(url, params={"date": date})
    data = response.text
    soup = BeautifulSoup(data, "html.parser")

    tbody_tags = soup.select("tbody")

    exchange_rates = []
    # 获取tbody标签中的tr标签
    for tbody in tbody_tags:
        tr_tags = tbody.find_all("tr")
        for tr in tr_tags:
            td_tags = tr.find_all("td")
            set_currency = td_tags[0].text
            set_amount = td_tags[4].text
            exchange_rates.append((set_currency, set_amount))

    return exchange_rates


pull_date = '05.12.2023'
exchange_rate = get_exchange_rate(pull_date)
print(f"The exchange rates on {pull_date} are:")
for currency, amount in exchange_rate:
    print(f"Currency: {currency}, Amount: {amount}")
