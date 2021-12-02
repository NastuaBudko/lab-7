import requests
from bs4 import BeautifulSoup
from array import *
from requests.sessions import session
import matplotlib.pyplot as plt

from sqlalchemy.sql.expression import column

r = requests.get("https://hotels24.ua/news/top-15-najkrasivіshix-mіst-ukraini-nezabutnya-podorozh-najkrashhimi-kutochkami-kraini-11232295.html")
page = BeautifulSoup(r.text,'html.parser')
print(r.status_code)
row1 = page.head.title.text
row2 = page.body.text
words = row2.split(' ')
unik_words = []
for elem in words:
    if elem in unik_words:
        continue
    else:
        unik_words.append(elem)

L = len(unik_words)
numbers = array('i',[])
n = 0
for elem in unik_words:
    n = words.count(elem)
    numbers.append(n)
print(numbers)
print(unik_words[10],' ',numbers[10])

d=dict()
i = 0
for i in range(L):
    elem = unik_words[i]
    d[elem] = numbers[i]
print(d['Місто'])


plt.show()
plt.savefig('gist.png')
