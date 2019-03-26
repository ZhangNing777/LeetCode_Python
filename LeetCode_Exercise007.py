#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
注意:
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31−1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

'''

def Reverse_Integer(int):
    c = 0
    if (int > (2**31-1)) or (int < (-2**31)):
        print("This number is out of range")
    elif (int < 0):
        int = -1 * int
        while(int != 0):
            a = int / 10
            b = int - a * 10
            c = c * 10 - b
            int = a
        if(c<-2**31):
            print 0
        else:
            print c
    else:
        while(int != 0):
            a = int / 10
            b = int - a * 10
            c = c * 10 + b
            int = a
        if(c > 2**31-1):
            print 0
        else:
            print c
    


Reverse_Integer(-134634563)

