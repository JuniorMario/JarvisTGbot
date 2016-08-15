# -*- coding: utf-8 -*-
import feedparser, ast
def send_feed(arg):
    d = feedparser.parse('http://globoesporte.globo.com/servico/semantica/editorias/plantao/futebol/times/{}/feed.rss'.format(arg))
    posts = []
    for post in d.entries:
        x =  str(unicode(post.title).encode('utf-8')) + ";" +  str(unicode(post.link).encode('utf-8')) + ""
        posts.append(x)
    return posts
