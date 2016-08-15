# -*- coding: utf-8 -*-
import reg
import requests
def pornando(query):
    link = "http://www.xvideos.com/?k=" + query
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'pl-PL,pl;q=0.8',
       'Connection': 'keep-alive'}
    req = requests.get(link, headers=hdr)
    html = req.content
    tags = reg.findTags(html)
    fliped = reg.filtering('href', tags, 'dir')
    links = []
    titles = []
    for i in fliped:
        if 'video' in i:
            if '>' in i and query in i:
                i = i.replace('>','')
                links.append(i)
            else:
                links.append(i)
        else:
            pass

    for a in links:

        a = a.split('/')
        titles.append(a[2])
    dic = {'links': links, 'titles': titles}


    return dic
    