# -*- coding: utf-8 -*-
#!/usr/bin/env python
# encoding: utf-8
import requests
import json
def send_weather(arg):
    if ' ' in arg:arg = arg.replace(' ','')
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q={}&APPID=14afd252482d9db2e7d1becb6a249d08'.format(arg))
    juca = json.loads(r.content)
    return juca