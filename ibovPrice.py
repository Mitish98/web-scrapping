import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://br.financas.yahoo.com/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

titles = []
prices = []

div_list = soup.find_all('div', {'class': 'Carousel-Mask Pos(r) Ov(h) market-summary M(0) Pos(r) Ov(h) D(ib) Va(t)'})

for div in div_list:
    title = div.find('a', {'class': 'Fz(s) Ell Fw(600) C($linkColor)'}).text.strip()
    price = div.find('fin-streamer', {'class': 'Fz(s) Mt(4px) Mb(0px) Fw(b) D(ib)'}).text.strip()
    
    title = title.replace('\n', '').replace('\t', '')
    price = price.replace('\n', '').replace('\t', '')
    
    titles.append(title)
    prices.append(price)

data = {'Title': titles, 'Price': prices}
df = pd.DataFrame(data)

print(df)

