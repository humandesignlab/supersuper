from lxml import html
import requests

searchTerm = "huevo"
page = requests.get('http://www.chedraui.com.mx/index.php/polanco/catalogsearch/result/?cat=0&q='+searchTerm+'')
tree = html.fromstring(page.content)

item = tree.xpath('//a[@class="name-product"]/text()')
prices = tree.xpath('//span[@class="price"]/text()')
specialPrice = tree.xpath('//p[@class="special-price"]/text()')

if (specialPrice):
	print 'Items: ', item, len(item)
	print 'special Price ', specialPrice
else:
	print 'Items: ', item, len(item)
	print 'Prices: ', prices, len(prices)
