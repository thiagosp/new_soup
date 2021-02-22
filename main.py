#Project Name: Scrapping_Vagas_Python
#Version: 1.0 - Beta
#Author: Thiago Ferreira

#Importando pacote de requests(requisições HTTP)
import requests

#Importando pacote do BeautifulSoap
from bs4 import BeautifulSoup

#URL que vamos trabalhar!
name_url = 'https://br.indeed.com/empregos-de-python'

#Faço a requisição na url
url_conn = requests.get(name_url)

#Verifico se a conexão foi bem sucedida
if url_conn.status_code == 200:
  print(f'Conexão bem sucedida com o site {url_conn}')
else:
  print('Site FORA DO AR!')






