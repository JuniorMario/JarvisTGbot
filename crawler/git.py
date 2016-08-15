# -*- coding: utf-8 -*-
import urllib2
import reg
import requests
import urllib
import random

def gith(message):
	if ' ' in message:
		message.replace(' ','+')
	else:
		pass
	
	header = {
	    'User-Agent': 'Mozilla/5.0',
	    
	}
	oficina = 'https://github.com/search?utf8=✓&q='+ message
	html = requests.get(oficina + message, headers = header)
	html = html.content
	tags = reg.findTags(html)
	filtrando = reg.filtering('href', tags, 'dir')
	res = []
	validar = str(message).lower()

	for i in filtrando:
		a = i.split('/')
		if len(a) < 3 or "?"  in i:
			pass
		elif 'reward' in i or '=' in i:
			pass
		else:
			if '.' not in i:
				compiled =  'https://github.com{}\n\n'.format(i)

			else:
				pass
	
	try:	
		num = len(res)- 1
		strires = "{}\n {}\n {}\n".format(res[num], res[num-1], res[num - 2])
		print('res:{}\n\noficina:{}\nfiltrando:{}\n\nstrires:{}'.format(res, oficina, filtrando, strires))
		return strires
		strires = None
	except IndexError:
		strires = "Argumento vazio ou invalido."

