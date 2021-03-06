#!/usr/bin/env python3

import requests
#import texttable as tt
#import smtplib
import email.message
import operator
from tabulate import tabulate
from bs4 import BeautifulSoup
res = requests.get('https://docs.google.com/spreadsheets/d/1rBV78LxZcu2J2L5rCEaBPAujnY4NJEbxLMqsfQXxh0g/pubhtml/sheet?headers=false&gid=0').text
res2 = requests.get('https://zerodha.com/margin-calculator/Equity/').text
soup = BeautifulSoup(res, 'html.parser')
soup2= BeautifulSoup(res2, 'html.parser')
heading = [soup.tbody.tr.contents[j].text for j in {1,7,9,5}]
heading.append('ZERODHA')
for i in soup.tbody.contents:
    if i.contents[1].text == 'NIFTY' or i.contents[1].text == 'BANKNIFTY':
        nifty=[i.contents[j].text for j in {1,7,9,5}]
        print(nifty[0],'',nifty[3])

tab_conts=[]
for i in soup.tbody.contents:
    if i.contents[9].text == 'OPEN=HIGH' or i.contents[9].text == 'OPEN=LOW':
        contents = [i.contents[j].text for j in {1,7,9,5}]
        stock=contents[0]
        st=stock+':EQ'
        for row in soup2.tbody.findAll('tr'):
            for td in row.findAll('td'):
                if td.text == st:
                    contents.append(td.findNext(attrs='mis').text.strip())
        tab_conts.append(contents)
tabnew=[]
tabnew.append(heading)
tabnew += sorted(tab_conts, key=operator.itemgetter(3), reverse=True)
print(tabulate(tabnew[1:], headers=tabnew[0]))
