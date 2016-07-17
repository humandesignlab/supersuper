#!/usr/local/bin/python
# -*- coding: utf-8 -*-


from HTMLParser import HTMLParser
pars = HTMLParser()
test = pars.unescape('&copy; &euro; &#225;')
print test.encode('utf-8')
