# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 12:17:42 2022

@author: rohan
"""

'''
a.	Write a function that prints any given integer, such as 3141592653589793, in the following (readable) format:
3_141_592_653_589_793 

'''

def addUnderScores(x):
    x=str(x)
    ans=list()
    while(x):
        ans.append(x[-3:])
        x = x[:-3]
    return ('_'.join(ans[::-1]))

print(addUnderScores(3141592653589793))


'''
b.	Write a function that takes as parameters a phone number and a (country-specific) phone number format and returns a string that represents the formatted phone number.
    Examples: 
   UAE:  phoneNumber = 971506455734, phoneFormat = "3+2+3+4"
  formatted output:  971-50-645-5734
France:  phoneNumber = 33109758351, phoneFormat = "2+1+2+2+2+2"
  formatted output:  33-1-09-75-83-51
   India:  phoneNumber = 918966428361, phoneFormat = "2+3+7"
  formatted output:  91-896-6428361

'''
print('-'*95)
def splitNum(num,form):
    num=str(num)
    arr=list(map(int,form.split('+')))
    ans=""
    currIndex=0
    for x in arr:
        ans+=num[currIndex:currIndex+x]+"-"
        currIndex+=x
    return ans[:-1]


print(splitNum(num = 971506455734, form = "3+2+3+4"))
print(splitNum(num = 33109758351, form = "2+1+2+2+2+2"))
print(splitNum(num = 918966428361, form = "2+3+7"))
