#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import urllib2
import json
import pandas as pd
from BeautifulSoup import BeautifulStoneSoup
import cgi

def HTMLEntitiesToUnicode(text):
    text = unicode(BeautifulStoneSoup(text, convertEntities=BeautifulStoneSoup.ALL_ENTITIES))
    return text

productNames = []
brandNames = []
allPrices = []
searchQuery = 'leche+alpura'
req = urllib2.Request("http://www.superama.com.mx/buscador/resultado?busqueda="+searchQuery)

opener = urllib2.build_opener()
f = opener.open(req)
json1 = json.loads(f.read())

print 'Number of products: ', len(json1['Products'])

for item in range(0, len(json1['Products'])):
	names = json1['Products'][item]['Description']
	cleanNames = HTMLEntitiesToUnicode(names).encode('utf-8')
	productNames.append(cleanNames)
	prices = json1['Products'][item]['Precio']
	allPrices.append(prices)
	#print cleanNames

df = pd.DataFrame(productNames, columns=['Producto'])
df['Precio']=allPrices

print df
df.to_csv('searches/outsuperama.csv', encoding='utf-8')


