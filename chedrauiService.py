#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys
from bs4 import BeautifulSoup
import lxml
import lxml.etree
import urllib2
from cookielib import CookieJar
import pandas as pd

#chedrauiUrl = 'http://www.chedraui.com.mx/index.php/interlomas/catalogsearch/result/?cat=0&q='

def searchService(searchString):

	searchTerm = searchString
	searchQuery = searchTerm.replace(" ", "+")
	productNames = []
	allPrices = []
	cj = CookieJar()

	preOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	prep = preOpener.open('http://www.chedraui.com.mx/index.php/interlomas/catalogsearch/result/?cat=0&p=1&q=' + searchQuery)
	preSoup = BeautifulSoup(prep, "lxml")
	pagerTotal = preSoup.find('div', class_='pager')
	children = pagerTotal.find_all("li")

	if len(children) == 0:
		pages = len(children) +2
	else:
		pages = len(children)

	#print pages
	for page in range(1,pages):
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
	print productNames
	print allPrices
	print dict(zip(productNames, allPrices))

	# df = pd.DataFrame(productNames, columns=['Producto'])
	# df['Precio']=allPrices
	# df.to_csv('searches/outchedraui.csv', encoding='utf-8')
	# print df

searchService('jabon zote')
