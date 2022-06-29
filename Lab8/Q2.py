# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 14:45:05 2022

@author: rohan
"""
import re


def convert(s):
    s=re.sub("<(\w+)>", "<code>\\1</code>", s) #Code Tags
    s=re.sub("`&(.+);`", "<code>\\1</code>", s) #Code Tags
    
    s=re.sub(r'(###)(.*?)(###)',r'<h3>\2</h3>\n',s) #H3 Tags
    s=re.sub(r'(###)(.*?)(\n)',r'<h3>\2</h3>\n',s) #H3 Tags
    
    s=re.sub(r'(.*?)\n(--+)',r'<h2>\1</h2>',s) #H2 Tags
    s=re.sub(r'(##)(.*?)(##)',r'<h2>\2</h2>\n',s) #H2 Tags
    s=re.sub(r'(.*?)\n(=+)',r'<h1>\1</h1>',s) #H1 Tags
    
    
    s=re.sub(r'(\*\*|__)(.*?)(\*\*|__)',r'<strong>\2</strong>',s) #Strong
    s=re.sub(r'(\*|_)(.*?)(\*|_)',r'<em>\2</em>',s) #Emphasis
    
    s=re.sub(r'(:)\n\n([123])',r'\1<ol>\2',s) #Ordered list start
    s=re.sub(r'([123].*?)\n\n',r'\1</ol>',s) #Ordered list end
    
    s=re.sub(r'(:)\n\n([+\*\-]  )',r'\1<ul>\2',s) #Unordered list start
    s=re.sub(r'([+\*\-].*?)\n\n',r'\1</ul>',s) #Unordered list end
    
    s=re.sub(r'[\*+\-]  (.*?\.)',r'<li>\1</li>',s) #Li tag UL
    s=re.sub(r'[123]\.(.*)',r'<li>\1</li>',s) #Li tag OL
    
    res = ""
    for i in s.split('\n\n'):
        res += "".join('<p>' + i + '</p>')
    res=re.sub(r'  \n','<br>',res)
    return res
    


with open("Lab8-InputFile.txt",'r') as f:
    text=f.read()
    s=convert(text)
    myfile=open("Q2 Ans.html",'w')
    myfile.write(s)
    myfile.close()