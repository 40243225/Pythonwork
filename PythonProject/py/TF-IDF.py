# -*- coding: utf8 -*-
# coding: utf8
import xml.etree.cElementTree
import urllib2
import jieba
import codecs
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn import feature_extraction
import os
import codecs
import sys
import string
import time
import re
from bokeh.core.validation.errors import codes
from sklearn.feature_extraction import stop_words
from sympy.combinatorics.generators import symmetric
from networkx.algorithms.operators.binary import symmetric_difference

def jieba_article(stopw):
	print ("開始斷詞食品opendata.xml")
	global title
	global cat
	global context
	global date
	cat =[]
	title=[]
	context=[]
	date=[]
	jieba.load_userdict("./dict/userdict.txt")
	jieba.load_userdict("./dict/stop_words.txt")
	ET= xml.etree.cElementTree
	web=urllib2.urlopen('https://data.fda.gov.tw/cacheData/159_1.xml' )
	tree=ET.ElementTree(file=web)
	root = tree.getroot()
	for data in root.findall('rows'):
	    cat.append(data[0].text)
	    title.append(data[1].text)
	    context.append(data[2].text)
	    date.append(data[4].text)
	
	jia=list()
	
	for i in range(len(cat)):
		text=re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', context[i])
		text=re.sub("[\s+\.\!\/_,$%^:*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+".decode("utf8"), "".decode("utf8"),text)
		str1="".join(title[i].split())
		str2="".join(text.split())
		seg_list = jieba.cut(str1+str2)
		seg_list=list(seg_list)
		
		count=0
		for j in seg_list:
			if j not in stopw:
				if count==0:
					seg=""+j
				else:
					seg=seg+" "+j
				count+=1
		jia.append(str(i)+"|"+title[i]+"|"+context[i]+"|"+seg)
	fout=codecs.open('data/food/food.txt','w',encoding='utf-8')
	
	for i in jia:
		fout.write(i)
		fout.write("\n") 
	fout.close()
	print("完成斷詞")
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False
def getFilelist(path):
    filelist = []
    files = os.listdir(path)
    for f in files :
        if(f[0] == '.') :
            pass
        else :
            filelist.append(f)
    return filelist
def setstopwords():
    fopen=codecs.open("./dict/stop_words.txt","r",encoding='utf-8')
    linelist=[]
    while True:
        line=fopen.readline()
        line=line.strip('\n')
        linelist.append(line)
        if not line: 
            break
    return linelist
    fopen.close()
def Tfidf(filelist ,path,fdic,stop_w) :
    corpus = []
    
    for ff in filelist :
        fname = path +"/"+ ff
        f = codecs.open(fname, 'r3' ,encoding='utf-8')
        content = f.read()
        f.close()
        corpus.append(content)    
    
    
    vectorizer = CountVectorizer()    
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
    
    word = vectorizer.get_feature_names() #所有文本的关键字
    weight = tfidf.toarray()              #对应的tfidf矩阵
    sFilePath = './data/tfidffile'
    stop_temp=list()
    '''紀錄停止字位置'''
    for i in range(len(word)):
    	temp=word[i]+"\n".decode('utf-8')
    	if temp in stop_w:
    		stop_temp.append(i)
    if not os.path.exists(sFilePath) : 
        os.mkdir(sFilePath)
    # 这里将每份文档词语的TF-IDF写入tfidffile文件夹中保存
    for i in range(len(weight)) :
        print u"--------Writing all the tf-idf in the",fdic[i]
        f = codecs.open(sFilePath+'/'+fdic[i],'w',encoding='utf-8')
        for j in range(len(word)) :
            temp=word[j]+"\n".decode('utf-8')
            if j not in stop_temp and is_number(word[j])==False and weight[i][j]>0.15: 
                    f.write(word[j]+","+str(weight[i][j])+"\n")
        f.close()
if __name__ == "__main__" :
	start = time.time()
	path ="./data/food"
	stopw=setstopwords()
	jieba_article(stopw)
	'''
	allfile=getFilelist(path)
	fdic=dict()
	count =0
	for ff in allfile :
	    fdic[count]=ff
	    #print fdic[count]
	    count+=1
   
	print("開始TF-IDF演算法")
	print allfile[0]
	Tfidf(allfile,path,fdic,stopw)
	print("完成")
	end = time.time()
	elapsed = end - start
	print "Time taken: ", elapsed, "seconds."
	'''