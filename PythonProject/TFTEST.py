# -*- coding: utf8 -*-
# coding: utf8
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn import feature_extraction
import os
import codecs
import sys
import string
from bokeh.core.validation.errors import codes
from sklearn.feature_extraction import stop_words


path ="./data/food"

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
    if not os.path.exists(sFilePath) : 
        os.mkdir(sFilePath)
    # 这里将每份文档词语的TF-IDF写入tfidffile文件夹中保存
    for i in range(len(weight)) :
        print u"--------Writing all the tf-idf in the",fdic[i]
        f = codecs.open(sFilePath+'/'+fdic[i],'w',encoding='utf-8')
        for j in range(len(word)) :
            temp=word[j]+"\n".decode('utf-8')
            if is_number(word[j])==False and temp not in stop_w and weight[i][j]>0.1: 
                    f.write(word[j]+","+str(weight[i][j])+"\n")
        f.close()

def setstopwords():
    fopen=codecs.open("./dict/stop_words.txt","r",encoding='utf-8')
    linelist=[]
    while True:
        line=fopen.readline()
        linelist.append(line)
        if not line: 
            break
    return linelist
    fopen.close()
        
stopw=setstopwords()
allfile=getFilelist(path)
fdic=dict()

count =0
for ff in allfile :
    fdic[count]=ff
    #print fdic[count]
    count+=1
    
Tfidf(allfile,path,fdic,stopw)
