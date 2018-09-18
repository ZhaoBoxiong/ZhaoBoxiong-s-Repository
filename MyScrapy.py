import urllib2
import os
MyInterface = urllib2.urlopen("http://www.baidu.com")
MyHtmlData = MyInterface.read()

MyWorkPath = os.getcwd()
MyScrapyPtah = MyWorkPath +'/MyScrapyfile.txt'
f=open(MyScrapyPtah,'w+')
f.write(MyHtmlData)
f.close()