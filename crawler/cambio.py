from lxml import html
import requests
def dolar():
	page = requests.get('http://www.dolarhoje.net.br/')
	tree = html.fromstring(page.content)
	dolar = tree.xpath('//span[@id="moeda"]/text()')
	dolar = str(dolar)
	dolar = dolar.strip('= \'[ ]')
	return dolar
