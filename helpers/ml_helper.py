from bs4 import BeautifulSoup

import time
from operator import itemgetter

url_ml = "https://lista.mercadolivre.com.br/"

products_list = list()

def parse_data():
  # Get all listings
   product_list = site_ml.find_all('li', class_="ui-search-layout__item")

   # Loop all products
   for product in product_list:
     product_title = product.find("a", class_="poly-component__title").text

     product_price_frac = product.find('span', class_="andes-money-amount__fraction").text.replace('.', '')
     product_price_cents = "00"

     product_price_cents_element = product.find('span', 'andes-money-amount__cents andes-money-amount__cents--superscript-24')
     if (product_price_cents_element != None):
       product_price_cents = product_price_cents_element.text

     product_final_price = (float)(product_price_frac + "." + product_price_cents)

     product_link = product.find('a', class_="poly-component__title")['href']

     products_list.append(list([product_title, product_final_price, product_link]))

def search_ml(driver, nomeProduto):
  print('Procurando no Mercado Livre')

  driver.get(url_ml + nomeProduto)
  time.sleep(3)
  page = driver.page_source

  global site_ml
  site_ml = BeautifulSoup(page, 'html.parser')

  parse_data()

  sorted_list = sorted(products_list, key=itemgetter(1))

  return sorted_list
