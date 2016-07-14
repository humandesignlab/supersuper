#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys
from bs4 import BeautifulSoup
import urllib2
from cookielib import CookieJar
import pandas as pd

chedrauiUrl = 'http://www.chedraui.com.mx/index.php/interlomas/catalogsearch/result/?cat=0&q='

searchQuery = 'leche'
productNames = []
allPrices = []

def theSoup(searchUrl, searchTerm):
	cj = CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	p = opener.open(searchUrl + searchTerm)
	mySoup = BeautifulSoup(p, "lxml")
	return mySoup


chedrauiSoup = theSoup(chedrauiUrl, searchQuery)

chedraui_products = chedrauiSoup.find_all('div', class_='f-fix')
for name in chedraui_products:
	names = name.find_all('a', class_='name-product')
	productNames.append(names[0].find(text=True).strip())
print "Total de productos: ", len(productNames)

chedraui_prices = chedrauiSoup.find_all('div', class_='price-box')
for price in chedraui_prices:
	prices = price.find_all('span', class_='price')
	allPrices.append(prices[-1].find(text=True).strip())
print "Total de precios: ", len(allPrices)




df = pd.DataFrame(productNames, columns=['Producto'])
df['Precio']=allPrices

print df