#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
from tabulate import tabulate
import operator
url_moneycontrol = 'https://m.moneycontrol.com/sensex.php?index=2&id=4'
res_moneycontrol = requests.get(url_moneycontrol).text
soup_moneycontrol = BeautifulSoup(res_moneycontrol, 'html.parser')
volstock_moneycontrol = []
for i in soup_moneycontrol.find_all(cellpadding="3"):
    for tr in i:
        for td in tr:
            for td2 in td:
                for table in td2:
                    stock_moneycontrol = []
                    for td in table:
                        stock_moneycontrol.append(td.text.strip('\xa0\xa0'))
                    volstock_moneycontrol.append(stock_moneycontrol)
table_data = sorted(volstock_moneycontrol, key=operator.itemgetter(int(2)), reverse=True)
print(tabulate(table_data))
