# -*- coding: utf8 -*-
# coding: utf8
import codecs
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        for attr in attrs:
            print "attr:", attr

    def handle_data(self, data):
        print "Data:", data

    def handle_comment(self, data):
        print "Comment  :", data

    def handle_entityref(self, name):
        c = unichr(name2codepoint[name])
        print "Named ent:", c

    def handle_charref(self, name):
        if name.startswith('x'):
            c = unichr(int(name[1:], 16))
        else:
            c = unichr(int(name))
        print "Num ent  :", c

    def handle_decl(self, data):
        print "Decl     :", data
fout=codecs.open('data/rss.txt','r',encoding='utf-8')
#print(fout.read())
parser = MyHTMLParser()
parser.feed(fout.read())