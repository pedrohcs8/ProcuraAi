from simple_term_menu import TerminalMenu

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

import os
import time
from bs4 import BeautifulSoup
from operator import itemgetter

url_amazon = "https://www.amazon.com.br/s?k="

products_list = list()

def parse_data():
  product_list = site_amazon.find_all("div", class_="sg-col-4-of-4 sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-8 sg-col-4-of-20")

  for product in product_list:
    product_title = product.find('a', class_="a-link-normal s-line-clamp-4 s-link-style a-text-normal").find('span').text

    product_price_whole_element = product.find('span', class_="a-price-whole")
    if (product_price_whole_element == None):
      continue
    product_price_whole = product_price_whole_element.text.replace('.', '')
    product_price_frac = product.find('span', class_="a-price-fraction").text

    product_final_price = (float)((product_price_whole + product_price_frac).replace(",", "."))

    product_link = "https://www.amazon.com.br/" + product.find('a', class_="a-link-normal s-line-clamp-4 s-link-style a-text-normal")['href']

    products_list.append(list([product_title, product_final_price, product_link]))

def search_amazon(driver, nomeProduto):
  print('Procurando na Amazon')

  driver.get(url_amazon + nomeProduto)
  time.sleep(3)
  page = driver.page_source

  global site_amazon
  site_amazon = BeautifulSoup(page, 'html.parser')

  driver.quit()

  parse_data()

  sorted_list = sorted(products_list, key=itemgetter(1))

  return sorted_list
