# -*- coding: utf-8 -*-
from pygoogles import pygoogle

def search(nome):
	dis = pygoogle(nome)
	dis.pages = 1
	result = dis.res()
	return result