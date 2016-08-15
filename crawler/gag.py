# -*- coding: utf-8 -*-
import reg
import requests
import random
def randGag():

	link = 'http://9gag.com/'
	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'pl-PL,pl;q=0.8',
       'Connection': 'keep-alive'}
	try:
		req = requests.get(link, headers=hdr)
	except urllib2.HTTPError, e:
	    print e.fp.read()
	html = req.content
	tags = reg.findTags(html)
	fliped = reg.filtering('src', tags, None)
	alltags = []
	for i in fliped:
		if '.jpg' in str(i) and 'photo' in str(i):
			alltags.append(i)
	res = random.choice(alltags)
	print res
	return res
