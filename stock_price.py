from bs4 import BeautifulSoup
from urllib import request
#import datetime
from dataclasses import dataclass


@dataclass
class Get:
    code: str
    price: int
    year_high_price: int
    year_low_price: int


class StockPrice:
    @staticmethod
    def get_stockprice(code:str):
        url = "https://finance.yahoo.co.jp/quote/" + code + ".T/history"
        res = request.urlopen(url)
        soup = BeautifulSoup(res, 'html.parser')
        res.close()

        #株価取得
        div1 = soup.find('div', class_='nOmR5zWz')
        span1 = div1.find('span', class_='_3rXWJKZF')


        #年初来高値、年初来安値取得
        div2 = soup.find('div', class_='_1eHgciMX _3KTA0Qmv')
        span2 = div2.find_all('span', class_='_3rXWJKZF')

        price = span1.text.replace(',','')
        year_high_price = span2[0].text
        year_low_price = span2[1].text

        get = Get(code, float(price), year_high_price, year_low_price)
        return get

