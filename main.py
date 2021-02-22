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
  #Printa a msg de conexão bem sucedida
  print(f'Conexão bem sucedida com o site {name_url}')
  #Salva na variavel o conteudo html do site
  txt_site = url_conn.text
else:
  #Print a msg abaixo, caso haja algum erro na conexão
  print('Site FORA DO AR!')


#HORA DE FAZER A SOPA!

#Salvo na váriavel soup, o html do site, que foi
#pego na váriavel txt_site
soup = BeautifulSoup(txt_site, 'html.parser')










