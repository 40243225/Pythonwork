# -*- coding: utf8 -*-
# coding: utf8
import xml.etree.cElementTree
import urllib2
import jieba
import jieba.analyse
import codecs

jieba.load_userdict("./dict/userdict.txt")
#jieba.analyse.set_stop_words("./dict/stop_words.txt")
ET= xml.etree.cElementTree
web=urllib2.urlopen('https://data.fda.gov.tw/cacheData/159_1.xml' )
tree=ET.ElementTree(file=web)
root = tree.getroot()
global title
global cat
global context
global date
cat =[]
title=[]
context=[]
date=[]

count=0

for data in root.findall('rows'):
    cat.append(data[0].text)
    title.append(data[1].text)
    context.append(data[2].text)
    date.append(data[4].text)
for i in range(len(cat)):
    #print cat[i]
    print count
    a=str(count)
    str1="".join(context[i].split())
    seg_list = jieba.cut(str1)
    #seg_list=jieba.analyse.textrank(context[i], topK=20, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v'))
    #tags = jieba.analyse.extract_tags(context[i], topK=10, withWeight=False, allowPOS=('nz','nr','ns', 'n', 'vn','v'))
    fout=codecs.open('data/food/'+a+'.txt','w',encoding='utf-8')
    fout.write(" ".join(seg_list))
    fout.write("\n")
    fout.close()
    count+=1
    #print date[i]

    
#seg_list = jieba.cut("朋友說中藥西藥可以同時吃，不會有問題，是真的嗎", HMM=True)
#print("Full Mode: " + "/ ".join(seg_list))  # 全模式    
    
    