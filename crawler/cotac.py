# -*- coding: utf-8 -*-
import reg
import requests
import random
from lxml import html
def cota(arg):
    page = requests.get('https://www.google.com/finance?q={}&ei=1NZaV6GhKYuwmAHHyKvICg'.format(str(arg)))
    tree = html.fromstring(page.content)
    moeda = tree.xpath('//span[@class="bld"]/text()')
    return str(moeda)

