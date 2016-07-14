#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import urllib2
import json
import pandas as pd

productNames = []
allPrices = []
searchQuery = 'leche alpura'
req = urllib2.Request("http://www.lacomer.com.mx/GSAServices/searchArt?col=lacomer_2&orden=-1&p=1&pasilloId=false&s="+searchQuery+"&succId=14")
opener = urllib2.build_opener()
f = opener.open(req)
json = json.loads(f.read())

for articulo in json['res']:
	productNames.append(articulo['artDes'])
	allPrices.append(articulo['artPrven'])

df = pd.DataFrame(productNames, columns=['Producto'])
df['Precio']=allPrices

print df