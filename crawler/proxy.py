# -*- coding: utf-8 -*-
import urllib
import requests
import reg
def proxando():
	arg = 'python'
	link = 'https://www.us-proxy.org/'
	header = {
	    'User-Agent': 'Mozilla/5.0',
	    
	}
	html = requests.get(link, headers = header)
	html = html.content
	filen = open('writable.txt', 'w+')
	filen.write(html)
	proxys = reg.getContent(html, 'td')
	proxer = []
	dat = '-' * 50
	for i in proxys:
	    if 'td' in i:
	        i = i.replace('td','')
	        proxer.append(i)
	    else:
	        pass
	compiler = "IP/PORT: {}/{}\nCoutry:{}/{}\nAnonimity: {} \nGoogle: {}\nhttps: {}\nTempo: {}\n\n{}\n\nIP/PORT: {}/{}\nCoutry: {}/{}\nAnonimity: {}\nGoogle: {}\nhttps: {}\nTempo: {}\n\n{}".format(proxer[0], proxer[1], proxer[2], proxer[3], proxer[4], proxer[5],proxer[6],  proxer[7], dat, proxer[8], proxer[9], proxer[10], proxer[11], proxer[12],proxer[13], proxer[14], proxer[15], dat)
	return compiler
