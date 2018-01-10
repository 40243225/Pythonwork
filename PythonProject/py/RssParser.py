# -*- coding: utf8 -*-
# coding: utf8
import os
import codecs
import xml.etree.cElementTree
from xml.etree import ElementTree as ET
import re
import xml.dom.minidom
def xml_create(dom,root,ns,text):
    item = dom.createElement(ns)
    text=dom.createCDATASection(text)
    item.appendChild(text)
    root.appendChild(item)
    return root

def getFileName():
    fileName =list()
    for dirname, dirnames, filenames in os.walk('./rss'):
        # print path to all subdirectories first.
        for subdirname in dirnames:
            os.path.join(dirname, subdirname)
        # print path to all filenames.
        for filename in filenames:
            fileName.append(os.path.join(dirname, filename))
    return fileName;

def cleanhtml(raw_html):
  raw_html= raw_html.replace('【'.decode("utf-8"), "<a href=")
  raw_html= raw_html.replace('】'.decode("utf-8"), ">")
  cleantext = re.sub('<.*?>' ,'', raw_html)
  return cleantext
def newFileName(path):
    newfileName=path.replace(".",'')
    newfileName=newfileName.replace("/rss/",'')
    newfileName=newfileName.replace("xml",'')
    return newfileName
def xmldecode(path):
    #fopen=codecs.open("./rss/2017-12-21_1/國際/國際頭條.xml","r",encoding='utf-8')
    ET= xml.etree.cElementTree
    tree=ET.ElementTree(file=path)
    newfileName=newFileName(path)
    root = tree.getroot()
    temp =0;
    print newfileName
    if not os.path.exists("./data/News/orignalfile/"+newfileName):
        os.makedirs("./data/News/orignalfile/"+newfileName)
    for child in root:
        for data in child.findall('item'):
             title=data.find('title').text
             dscription =data.find('description').text
             pubDate=data.find('pubDate').text
             link=data.find('link').text
             dom = xml.dom.minidom.getDOMImplementation().createDocument(None, 'data', None)
             root = dom.documentElement
             root =xml_create(dom,root, "title",title)
             root =xml_create(dom,root, "dscription",cleanhtml(dscription))
             root =xml_create(dom,root, "pubDate",pubDate)
             root =xml_create(dom,root, "link",link)
             print root.toxml()
             f=file("./data/News/orignalfile/"+newfileName+"/"+str(temp)+".xml", 'w')
             writer = codecs.lookup('utf-8')[3](f)
             dom.writexml(writer, encoding='utf-8')
             writer.close()
             #f = codecs.open("./data/News/"+newfileName+"/"+str(temp)+".xml",'w',encoding='utf-8')
             #f.write(str1)
             #f.close()
             temp=temp+1 
                
fileName=getFileName()
for data in fileName:
    xmldecode(data) 



