# -*- coding: utf-8 -*-
import requests
import reg, sys
from lxml import html
def playSt(arg):
	header = {
	    'User-Agent': 'Mozilla/5.0',
	    
	}
	link = "https://play.google.com/store/search?q=%s&hl=pt_BR" %arg
	arg = None
	page = requests.get(link, headers = header)
	htm = page.content
	tags = reg.findTags(htm)
	filtrando = reg.filtering('href', tags, 'dir')
	print filtrando
	apps = []
	appsf = []
	tree = html.fromstring(page.content)
	titu = tree.xpath('//a[@class="title"]/text()')
	print type(titu)
	titles = []
	for i in titu:
		if len(i) >= 2:
			titles.append(i)
		else:
			pass
	try:
		for i in filtrando:
			if 'id=com.' in i:
				i = "{}{}".format('https://play.google.com', i)
				apps.append(i)
			else:
				pass
		
		for a in apps:
			if a in str(appsf):
				pass
			else:
				appsf.append(a)
		appsf = list(set(appsf))
		num = len(appsf) - 1
		compiler = "📱[{}]({})\n📱[{}]({})\n📱[{}]({})\n📱[{}]({})\n📱[{}]({})".format(titles[0], appsf[num], titles[1], appsf[num-1],titles[2], appsf[num-2],titles[3], appsf[num-3],titles[4], appsf[num-4]),	

		return compiler
	except:
		pass