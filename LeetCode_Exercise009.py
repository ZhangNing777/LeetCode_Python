#!/usr/bin/python2
# -*- coding: UTF-8 -*-

'''
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
'''

def Palindrome_Number(int):
    a = int
    d = 0
    if(int < 0):
        return False
    else:
        while(int != 0):
            b = int // 10
            c = int - b * 10
            d = d * 10 + c
            int = b
        if(a == d):
            return True
        else:
            return False

print(Palindrome_Number(12321))
        
        
