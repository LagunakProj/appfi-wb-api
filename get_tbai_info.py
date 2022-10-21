import requests
from bs4 import BeautifulSoup


url_web = "https://tbai.egoitza.gipuzkoa.eus/qr/?id={}"


CLASE_HTML = "form-control-static text-success"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
    "Accept": "*/*"
}

def get_page(url: str) -> str:
    res = requests.get(url, headers=HEADERS)
    # print(res.content)
    return res.content


def get_currency_info(html: str):
    soup = BeautifulSoup(html,'html.parser')
    our_text = soup.find_all('p')[-3].text.strip().replace('''\r\n''', '').replace('''\t''', '').replace('€', '')
    # our_text = soup.find('p', {'class':'form-control-static text-success'}).text
    # print(our_text)
    return our_text
    # return CLASE_HTML in html


def main_tbai(id: str) -> None:
    html = get_page(url_web.format(id))
    tbai_number = get_currency_info(html)
    # print(currency_number)
    return (tbai_number)
