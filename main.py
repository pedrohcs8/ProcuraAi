from helpers.ml_helper import search_ml
from helpers.amazon_helper import search_amazon

from simple_term_menu import TerminalMenu

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

import os
import time

products_list = list()

menu_options = ['Mercado Livre', 'Amazon', 'Kabum', 'Pichau']

def writeToFile(amount):
  product_counter = 0
  store_index = 0

  with open('produtos.txt', 'w') as file:
    for store in products_list:
      file.write(menu_options[store_index])
      file.write('\n')
      file.write('\n')

      for product in store:
        if (amount != 0):
          product_counter += 1

          if (product_counter > amount):
            return

        file.write(product[0])
        file.write('\n')
        file.write("R$" + str(product[1]))
        file.write('\n')
        file.write(product[2])
        file.write('\n')
        file.write('\n')

      store_index += 1

terminal_menu = TerminalMenu(menu_options, multi_select=True, show_multi_select_hint=True, multi_select_empty_ok=True, multi_select_select_on_accept=False, title="Selecione a(as) lojas")
menu_entry_indices = terminal_menu.show()

selectedStores = terminal_menu.chosen_menu_entries
if selectedStores is None or len(selectedStores) < 1:
    print('Você precisa selecionar pelo menos uma loja')
    exit(1)

nomeProduto = input('Qual o produto desejado? ')
quantidadeProdutos = 0
quantidadeProdutosBruto = input('Quantos produtos por loja devo exibir? ')


if quantidadeProdutosBruto.isnumeric():
    quantidadeProdutos = int(quantidadeProdutosBruto)

if os.path.isfile('produtos.txt'):
    os.remove('produtos.txt')
    time.sleep(5)
    print('Deletei o arquivo antigo')

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Firefox(options=options)
driver.set_window_size(1920, 1080)

for store in selectedStores:
    match store:
        case 'Mercado Livre':
          products_list.append(search_ml(driver, nomeProduto))
        case 'Amazon':
          products_list.append(search_amazon(driver, nomeProduto))
        case 'Kabum':
          print("Kabum")
        case 'Pichau':
          print("Pichau")

driver.quit()
writeToFile(quantidadeProdutos)

print("Pesquisa Concluída")
