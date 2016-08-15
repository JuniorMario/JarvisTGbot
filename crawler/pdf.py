import urllib2
import reg
import urllib
import random
import requests
def apostilando(message):
	if ' ' in message:
		message.replace(' ','+')
	else:
		pass
	oficina = "https://www.bing.com/search?q=%s+pdf" %message
	header = {
	    'User-Agent': 'Mozilla/5.0',
	    
	}
	html = requests.get(oficina, headers = header)
	html = html.content
	tags = reg.findTags(html)
	filtrando = reg.filtering('href', tags, 'pdf')
	response = random.choice(filtrando)
	filename = response.split('/')
	indice = len(filename)
	indice = indice - 1
	filename = filename[indice]
	try:
		print('Baixando...')
		urllib.urlretrieve(response, filename)
		doc = open('{filename}'.format(filename = filename), 'rb')
		print doc
		oficina = None
		return doc
	except:
		print('Smile, and fix it.')