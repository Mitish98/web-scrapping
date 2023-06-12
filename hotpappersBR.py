from bs4 import BeautifulSoup
import requests

url = "https://br.financas.yahoo.com/noticias/acoes-mais-negociadas?offset=0&count=100"
response = requests.get(url)
content = response.content

soup = BeautifulSoup(content, "html.parser")

secao = soup.find("section", {"id": "screener-results"})

tabela = secao.find("table")

linhas = tabela.find_all("tr")

titles = []
prices = []

for linha in linhas[1:]:
    dados = linha.find_all("td")
    titles.append(dados[1].text.strip())
    prices.append(dados[2].text.strip())

data = {'Title': titles, 'Price': prices}

for item in data['Title']:
    print(item)

for i in range(len(data['Title'])):
    print(f"{data['Title'][i]}: {data['Price'][i]}")

import pandas as pd

df = pd.DataFrame(data)
print(df)
df.to_excel('hotpappersBR.xlsx', index=False)
