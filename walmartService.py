#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import urllib2
import os, sys
from bs4 import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup
import lxml
import lxml.etree
import urllib2
import json
from cookielib import CookieJar
import pandas as pd
from decimal import *

def HTMLEntitiesToUnicode(text):
    text = unicode(BeautifulStoneSoup(text, convertEntities=BeautifulStoneSoup.ALL_ENTITIES))
    return text


searchTerm = 'jamon serrano'
productNames = []
brandNames = []
allPrices = []
searchQuery = searchTerm.replace(" ", "%20")
req = urllib2.Request("https://www.walmart.com.mx/super/WebControls/hlSearch.ashx?Text="+searchQuery)

opener = urllib2.build_opener()
f = opener.open(req)
json1 = json.loads(f.read())

print "RESULTS WALMART: "
print 'Number of products: ', len(json1['Products'])

for item in range(0, len(json1['Products'])):
	names = json1['Products'][item]['Description']
	cleanNames = HTMLEntitiesToUnicode(names)
	productNames.append(cleanNames)
	prices = json1['Products'][item]['Precio']
	allPrices.append(prices)

dfWalmart = pd.DataFrame(productNames, columns=['Producto'])
dfWalmart['Precio']=[Decimal('%.2f' % float(element.strip("$").replace(",", ""))) for element in allPrices]
#dfSuperama.to_csv('searches/outsuperama.csv', encoding='utf-8')
print dfSuperama


