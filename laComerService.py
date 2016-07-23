#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import urllib2
import json
import pandas as pd

productNames = []
brandNames = []
allPrices = []
searchQuery = 'leche lala'
req = urllib2.Request("http://www.lacomer.com.mx/GSAServices/searchArt?col=lacomer_2&orden=-1&p=1&pasilloId=false&s="+searchQuery+"&succId=14")

opener = urllib2.build_opener()
f = opener.open(req)
json1 = json.loads(f.read())

print 'number of pages: ', json1['numpages']
print 'number of products: ', json1['total']

for page in range(0,json1['numpages']):
	data = opener.open("http://www.lacomer.com.mx/GSAServices/searchArt?col=lacomer_2&orden=-1&p="+str(page)+"&pasilloId=false&s="+searchQuery+"&succId=14")
	completeJson = json.loads(data.read())
	#print page, completeJson['res']

	names = [lin['artDes'] for lin in completeJson['res']]
	productNames.append(names)

	brand = [lin['marDes'] for lin in completeJson['res']]
	brandNames.append(brand)

	prices = [lip['artPrven'] for lip in completeJson['res']]
	allPrices.append(prices)

productNamesList  = sum(productNames, [])
allPricesList = sum(allPrices, [])
brandNamesList = sum(brandNames, [])	

df = pd.DataFrame(productNamesList, columns=['Producto'])
df['Marca']=brandNamesList
df['Precio']=allPricesList

print df
df.to_csv('searches/outlacomer.csv', encoding='utf-8')



