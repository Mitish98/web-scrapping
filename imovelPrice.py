import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.brognoli.com.br/imoveis/?sort=newest&search_type=3&search_city=FLORIAN%C3%93POLIS&search_neighborhood%5B%5D=CAMPECHE&search_neighborhood%5B%5D=LAGOA+DA+CONCEI%C3%87%C3%83O&search_neighborhood%5B%5D=PRAIA+MOLE&search_neighborhood%5B%5D=RIO+TAVARES&search_min_price=&search_max_price=&search_bedrooms=0&search_garages=0'
response = requests.get(url)
content = response.content

soup = BeautifulSoup(content, 'html.parser')

titles = []
prices = []

div_list = soup.find_all('div', {'class': 'col-xs-12 col-sm-6 col-md-3 col-lg-3 property-gamd-box alugar no-hand'})

for div in div_list:
    title = div.find('div', {'class': 'description-property-data'}).text.strip()
    price = div.find('div', {'class': 'label-search-price'}).text.strip()
    
    title = title.replace('\n', '').replace('\t', '')
    price = price.replace('\n', '').replace('\t', '')
    
    titles.append(title)
    prices.append(price)


data = {'Title': titles, 'Price': prices}
df = pd.DataFrame(data)

print(df)

df.to_excel('imoveis.xlsx', index=False)



"""

import smtplib
import os
import imghdr
from email.message import EmailMessage

# Define o endereço de email do remetente e o destinatário
remetente = "matheus.iotti98@gmail.com"
senha = "maloirinho123"
destinatario = "matheus_iotti98@hotmail.com"

# Cria uma mensagem de email
msg = EmailMessage()
msg["Subject"] = "Planilha de imóveis"
msg["From"] = remetente
msg["To"] = destinatario
msg.set_content("Segue em anexo a planilha de imóveis.")

# Anexa o arquivo em excel à mensagem de email
with open("imoveis.xlsx", "rb") as f:
    arquivo = f.read()
    msg.add_attachment(arquivo, maintype="application", subtype="octet-stream", filename="imoveis.xlsx")

# Envia o email
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(remetente, senha)
    smtp.send_message(msg)

print("Email enviado com sucesso!")

"""