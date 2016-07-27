#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys
from bs4 import BeautifulSoup
import lxml
import lxml.etree
import urllib2
from cookielib import CookieJar
import pandas as pd

chedrauiUrl = 'http://www.chedraui.com.mx/index.php/interlomas/catalogsearch/result/?cat=0&q='

searchTerm = 'pechuga pavo bernina'
searchQuery = searchTerm.replace(" ", "+")
productNames = []
allPrices = []
cj = CookieJar()
for page in range(1,6):
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	p = opener.open('http://www.chedraui.com.mx/index.php/interlomas/catalogsearch/result/?cat=0&p=' + str(page) + '&q=' + searchQuery)
	mySoup = BeautifulSoup(p, "lxml")


	chedraui_products = mySoup.find_all('div', class_='f-fix')
	for name in chedraui_products:
		names = name.find_all('a', class_='name-product')
		productNames.append(names[0].find(text=True).strip())

	chedraui_prices = mySoup.find_all('div', class_='price-box')
	for price in chedraui_prices:
		prices = price.find_all('span', class_='price')
		allPrices.append(prices[-1].find(text=True).strip())

	print "Retreived data from page: " + str(page)

print "Total de productos: ", len(productNames)
print "Total de precios: ", len(allPrices)

df = pd.DataFrame(productNames, columns=['Producto'])
df['Precio']=allPrices

print df
df.to_csv('searches/outchedraui.csv', encoding='utf-8')