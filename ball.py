#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = 'znlccy znlccy0603@163.com'

import random

class SelectBall(object):

    '''初始化方法'''
    def __init__(self):
        self.run()

    def run(self):
        while True:
            numStr = raw_input("请输入测试的次数: ")
            try:
                num = int(numStr)
            except ValueError:
                print(u"要求输入一个整数")
                continue
            else:
                break
        ball = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in xrange(num):
            n = random.randint(1,10)
            ball[n-1] += 1
        for i in xrange(1, 11):
            print(u"获取第%d号球的概率为%f" %(i, ball[i-1]*1.0/num))

if __name__ == '__main__':
    ball = SelectBall()