from helpers.ml_helper import search_ml
from helpers.amazon_helper import search_amazon

from simple_term_menu import TerminalMenu

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
<<<<<<< HEAD
from simple_term_menu import TerminalMenu

import time
import atexit
import os
import re
from operator import itemgetter
=======

import os
import time
>>>>>>> 78b047b (V1.1.2)

products_list = list()

menu_options = ['Mercado Livre', 'Amazon', 'Kabum', 'Pichau']

<<<<<<< HEAD
# Acha os produtos no Mercado Livre
def produtosMl(useStrictTerm, strictTerm):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Firefox(options=options)
=======
def writeToFile(amount):
  product_counter = 0
  store_index = 0
>>>>>>> 78b047b (V1.1.2)

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

<<<<<<< HEAD
    for produto_ml in produtos_ml:
        tituloProduto = produto_ml.find('h2', 'ui-search-item__title').text

        if useStrictTerm:
            if strictTerm not in tituloProduto:
                    continue

        linkProduto = produto_ml.find('a', 'ui-search-item__group__element ui-search-link__title-card ui-search-link')['href']
        precoProduto = int(produto_ml.find('span', 'andes-money-amount__fraction').text.replace('.', ''))

        list_ml.append(list([tituloProduto, precoProduto, linkProduto]))

    sorted_list = sorted(list_ml, key=itemgetter(1))

    return sorted_list[:quantidadeProdutos]

# Acha os produtos na Kabum
def produtosKabum(useStrictTerm, strictTerm):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Firefox(options=options)

    print('Procurando na Kabum')

    driver.get(url_kabum + nomeProduto)
    time.sleep(3)
    page = driver.page_source
    driver.quit()

    site_kabum = BeautifulSoup(page, 'html.parser')

    produtos_kabum = site_kabum.find_all('div', attrs={'class': 'sc-cdc9b13f-7 gHEmMz productCard'})

    if len(produtos_kabum) < 1:
        return "Produto não encontrado"

    for produto in produtos_kabum:
        tituloProduto = produto.find('span', 'sc-d79c9c3f-0 nlmfp sc-cdc9b13f-16 eHyEuD nameCard').text

        if useStrictTerm:
            if strictTerm not in tituloProduto:
                    continue

        linkProduto = produto.find('a', 'sc-cdc9b13f-10 jaPdUR productLink')['href']
        precoProdutoBruto = produto.find('span', 'sc-620f2d27-2 bMHwXA priceCard').text
        precoProdutoSelecionado = re.findall(r'\d+', precoProdutoBruto)

        precoProduto = int(''.join(precoProdutoSelecionado[:2]))

        list_kabum.append(list([tituloProduto, precoProduto, linkProduto]))

    sorted_list = sorted(list_kabum, key=itemgetter(1))

    return sorted_list[:quantidadeProdutos]

def produtosPichau(useStrictTerm, strictTerm):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Firefox(options=options)

    print('Procurando na Pichau')

    driver.get(url_pichau + nomeProduto)
    time.sleep(5)
    page = driver.page_source
    driver.quit()

    site_pichau = BeautifulSoup(page, 'html.parser')
    produtos_pichau = site_pichau.find_all('div', attrs={'class': 'MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12 MuiGrid-grid-sm-6 MuiGrid-grid-md-4 MuiGrid-grid-lg-3 MuiGrid-grid-xl-2'})

    i = 0
    for produto in produtos_pichau:
        tituloProduto = produto.find('h2', "MuiTypography-root jss80 jss81 MuiTypography-h6").text

        if useStrictTerm:
            if strictTerm not in tituloProduto:
                    continue

        if produto.find('a', 'jss12') is not None:
            linkBruto = produto.find('a', 'jss12')['href']
        else:
            linkBruto = produto.find('a', 'jss16')['href']

        linkProduto = 'https://pichau.com.br/' + linkBruto
        precoProduto = produto.find('div', 'jss110').text

        list_pichau.append(list([tituloProduto, precoProduto, linkProduto]))
        i = i + 1

    sorted_list = sorted(list_pichau, key=itemgetter(1))

    return sorted_list[:quantidadeProdutos]

def produtosAmazon(useStrictTerm, strictTerm):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Firefox(options=options)

    print('Procurando na Amazon')

    driver.get(url_amazon + nomeProduto)
    time.sleep(3)
    page = driver.page_source
    driver.quit()

    site_amazon = BeautifulSoup(page, 'html.parser')
    produtos_amazon = site_amazon.find_all('div', attrs={'class': 'sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20'})

    for produto in produtos_amazon:
        tituloProduto = produto.find('span', 'a-size-base-plus a-color-base a-text-normal').text

        if useStrictTerm:
            if strictTerm not in tituloProduto:
                continue

        linkProduto = 'https://amazon.com.br' + produto.find('a', 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal')['href']

        if (produto.find('span', 'a-size-base a-color-secondary') is None or produto.find('span', 'a-size-base a-color-secondary').text == 'Nenhuma opção de compra em destaque'):
            continue

        precoInteiro = produto.find('span', 'a-price-whole').text
        precoProduto = precoInteiro.replace('.', '').replace(',', '')

        list_amazon.append(list([tituloProduto, int(precoProduto), linkProduto]))

    sorted_list = sorted(list_amazon, key=itemgetter(1))

    return sorted_list[:quantidadeProdutos]

options = ['Mercado Livre', 'Amazon', 'Kabum', 'Pichau']
terminal_menu = TerminalMenu(options, multi_select=True, show_multi_select_hint=True, multi_select_empty_ok=True, multi_select_select_on_accept=False, title="Selecione a(as) lojas")
=======
terminal_menu = TerminalMenu(menu_options, multi_select=True, show_multi_select_hint=True, multi_select_empty_ok=True, multi_select_select_on_accept=False, title="Selecione a(as) lojas")
>>>>>>> 78b047b (V1.1.2)
menu_entry_indices = terminal_menu.show()

selectedStores = terminal_menu.chosen_menu_entries
if selectedStores is None or len(selectedStores) < 1:
    print('Você precisa selecionar pelo menos uma loja')
    exit(1)

nomeProduto = input('Qual o produto desejado? ')
<<<<<<< HEAD

quantidadeProdutos = 0
quantidadeProdutosBruto = input('Quantos produtos por loja devo exibir? ')
if quantidadeProdutosBruto.isnumeric():
    quantidadeProdutos = int(quantidadeProdutosBruto)
else:
    print('Você deve colocar um número!')
    exit(1)

strict_menu = TerminalMenu(['Não', 'Sim'], title='Usar palavra chave?')
menu_entry_index = strict_menu.show()

useStrictTerm = False
strictTerm = ''

if menu_entry_index == 1:
    strictTerm = input("Qual será a palavra chave? ")
    useStrictTerm = True
=======
>>>>>>> 78b047b (V1.1.2)

quantidadeProdutos = 0
quantidadeProdutosBruto = input('Quantos produtos por loja devo exibir? ')

<<<<<<< HEAD
if int(quantidadeProdutos) > 10:
    print('Só posso exibir até 10 produtos!')
    exit(1)
elif int(quantidadeProdutos) < 1:
    print('A quantidade de produtos deve ser maior que 1!')
    exit(1)
=======
if quantidadeProdutosBruto.isnumeric():
    quantidadeProdutos = int(quantidadeProdutosBruto)
>>>>>>> 78b047b (V1.1.2)

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
<<<<<<< HEAD
            productList.append('Mercado Livre')
            productList.append(produtosMl(useStrictTerm, strictTerm))
        case 'Amazon':
            productList.append('Amazon')
            productList.append(produtosAmazon(useStrictTerm, strictTerm))
        case 'Kabum':
            productList.append('Kabum')
            productList.append(produtosKabum(useStrictTerm, strictTerm))
        case 'Pichau':
            productList.append('Pichau')
            productList.append(produtosPichau(useStrictTerm, strictTerm))
=======
          products_list.append(search_ml(driver, nomeProduto))
        case 'Amazon':
          products_list.append(search_amazon(driver, nomeProduto))
        case 'Kabum':
          print("Kabum")
        case 'Pichau':
          print("Pichau")
>>>>>>> 78b047b (V1.1.2)

driver.quit()
writeToFile(quantidadeProdutos)

<<<<<<< HEAD
    with open('produtos.txt', 'w') as file:
        for products in productList:
            if type(products) == str:
                file.write(products)
                file.write('\n')
                file.write('\n')
                continue

            for product in products:
                file.write(product[0])
                file.write('\n')
                file.write(str(product[1]))
                file.write('\n')
                file.write(product[2])
                file.write('\n')
                file.write('\n')

    print('Pesquisa Pronta!')


atexit.register(final)
=======
print("Pesquisa Concluída")
>>>>>>> 78b047b (V1.1.2)
