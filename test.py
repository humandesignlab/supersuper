#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import urllib2
import json
import pandas as pd
# TODO: scroll programatically with selenium to load every item: http://stackoverflow.com/questions/21006940/how-to-load-all-entries-in-an-infinite-scroll-at-once-to-parse-the-html-in-pytho
productNames = []
allPrices = []
searchQuery = 'leche alpura'
req = urllib2.Request("http://www.lacomer.com.mx/GSAServices/searchArt?col=lacomer_2&orden=-1&p=1&pasilloId=false&s="+searchQuery+"&succId=14")
req1 = urllib2.Request("http://www.lacomer.com.mx/GSAServices/searchArt?col=lacomer_2&orden=-1&p=2&pasilloId=false&s=leche&succId=14")

opener = urllib2.build_opener()
f = opener.open(req)
json1 = json.loads(f.read())

print 'number of pages: ', json1['numpages']
print 'number of products: ', json1['total']

for page in range(0,json1['numpages']):
	#print page
	data = opener.open("http://www.lacomer.com.mx/GSAServices/searchArt?col=lacomer_2&orden=-1&p="+str(page)+"&pasilloId=false&s="+searchQuery+"&succId=14")
	completeJson = json.loads(data.read())
	#print page, completeJson['res']
	names = [lin['artDes'] for lin in completeJson['res']]
	productNames.append(names)
	#print names
	prices = [lip['artPrven'] for lip in completeJson['res']]
	allPrices.append(prices)
	#print prices
print productNames
print allPrices