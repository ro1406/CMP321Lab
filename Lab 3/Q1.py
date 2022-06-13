# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 10:17:28 2022

@author: rohan
"""

#part a)

def fib(n):
    if n<=1:
        return 1
    return fib(n-1)+fib(n-2)

print([fib(i) for i in range(11)])

#part b)

def fibAcc(n):
    def fibAcc(n,prev=0,acc=1):
        if n<=0:
            return acc
        return fibAcc(n-1,acc,prev+acc)
    return fibAcc(n)

print([fibAcc(i) for i in range(11)])

#part c)

def fibMemoized(n):
    memo={0:1,1:1}
    def fibMemoized(n):
        if n in memo:
            return memo[n]

        memo[n]=fibMemoized(n-1)+fibMemoized(n-2)
        return memo[n]
    
    return fibMemoized(n)
print([fibMemoized(i) for i in range(11)])

#part d)
def fibAccList(n):
    arr=[1,1]
    def fibAccList(n,arr):
        if n==0:
            return [1]
        if n==1:
            return [1,1]
        if len(arr)==n:
            return arr
        arr.append(arr[-1]+arr[-2])
        return fibAccList(n,arr)
        
    return fibAccList(n,arr)


print(fibAccList(11))
