import requests
from bs4 import BeautifulSoup
from numpy import *
import matplotlib.pyplot as plt
import pylab

r = requests.get("https://hotels24.ua/news/top-15-najkrasivіshix-mіst-ukraini-nezabutnya-podorozh-najkrashhimi-kutochkami-kraini-11232295.html")
page = BeautifulSoup(r.text,'html.parser')
print(r.status_code)
ryad1 = page.head.title.text
ryad2 = page.body.text
names = ["Розповідні", "Питальні", "Окличні", "Не завершені"]

frequency = [0, 0, 0, 0]
frequency[0] = ryad2.count('. ')
frequency[1] = ryad2.count('? ')
frequency[2] = ryad2.count('! ')
frequency[3] = ryad2.count('... ')

xdata = names
ydata = frequency

pylab.bar(xdata, ydata)
pylab.savefig('sentences.png',dpi=200)
plt.title('Кількість речень на сайті')
pylab.show()
plt.savefig('gistograma.png')
