# -*- coding: utf-8 -*-
import urllib2
import reg
import requests
def torta(query):

	
	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'pl-PL,pl;q=0.8',
       'Connection': 'keep-alive'}
       
    
	try:
	    link = 'https://kat.cr/usearch/%s/' %query
	    req = requests.get(link, headers=hdr)
	except urllib2.HTTPError, e:
	    print e.fp.read()
	
	html = req.content
	tags = reg.findTags(html)
	fliped = reg.filtering('href', tags, None)
	titles = []
	torrents = []

	for i in fliped:
		if '/' in str(i) and '.torrent'  in i:
			try:
				i = i.split('?')
				i = i[0]
				if torrents.count(i) == 1:
				    pass
				else:
					torrents.append("https:{}".format(i))

			except IndexError:
				pass
		elif i.endswith('.html'):
			i = i.replace('.html', '')
			titles.append(i)
		else:
			pass

	titles = list(set(titles))
	torrents = list(set(torrents))
	dicres = { 'titles': titles, 'linked': torrents}

	return dicres