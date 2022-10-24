import requests
from bs4 import BeautifulSoup


url_web = "https://www.xe.com/es/currencyconverter/convert/?Amount=1&From=EUR&To={}"


CLASE_HTML = "result__BigRate-sc-1bsijpp-1 iGrAod"

PRODUCTOS = {
    'USD': url_web.format('USD'),
    'GBP': url_web.format('GBP'),
    'CAD': url_web.format('CAD'),
    }

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
    "Accept": "*/*"
}

def get_page(url: str) -> str:
    res = requests.get(url, headers=HEADERS)
    return res.content[100000:1000000]


def get_currency_info(html: str):
    soup = BeautifulSoup(html,'html.parser')
    our_text = soup.find('p', {'class':'result__BigRate-sc-1bsijpp-1 iGrAod'}).text
    return our_text[:6]
    # return CLASE_HTML in html


def main(divisa: str) -> None:
    html = get_page(PRODUCTOS.get(divisa))
    currency_number = get_currency_info(html).replace(',',  '.')
    # print(float(currency_number))
    return float(currency_number)


