#!/usr/bin/env python
#coding: utf-8

__author__ = 'znlccy znlccy0603@163.com'

class PrintTable(object):

    '''初始化程序'''
    def __init__(self):
        print(u"开始打印9x9的乘法表格")
        self.print99()

    def print99(self):
        for i in xrange(1,10):
            for j in xrange(1, i+1):
                print('%dX%d=%2s    ' %(j, i, i*j))
            print('\n')

if __name__ == '__main__':
    py = PrintTable()