# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 00:44:19 2022

@author: rohan
"""
import random
#a)
lowercase=[chr(i+97) for i in range(26)]
random.shuffle(lowercase)
randomCipher = {}

for i in range(26):
    randomCipher[chr(i+97)]=lowercase[i]

print("Cipher:")    
print(randomCipher)

#b)
def encode(s):
    ans=''
    for ch in s:
        if 'a'<=ch<='z':
            ans+=randomCipher[ch]
        else:
            ans+=ch
    return ans        
            
#c)
def decode(s):
    decoder={v:k for k,v in randomCipher.items()}
    ans=""
    for ch in s:
        if 'a'<=ch<='z':
            ans+=decoder[ch]
        else:
            ans+=ch
    return ans  
print('-'*95)
print("String to be encoded: 'hello world!' ")
encoded=encode('hello world!')
print("Encoded string:",encoded)
print("Decoded string:",decode(encoded))

