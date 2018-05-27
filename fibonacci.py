#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'znlccy znlccy0603@163.com'

class Fibonacci(object):

    '''初始化方法'''
    def __init__(self):
        self.fList = [0,1]
        self.main()

    def main(self):
        listLen = raw_input("请输入Fibonacci数列的长度(3-50): ")
        self.checkLen(listLen)
        while len(self.fList) < int(listLen):
            self.fList.append(self.fList[-1] + self.fList[-2])
        print(u"得到的fibonacci数列为:\n %s " %self.fList)

    def checkLen(self, length):
        lenList = map(str, xrange(3,51))
        if length in lenList:
            print(u"输入的长度符合标准，继续运行")
        else:
            print(u"只能输入3-50，太长了不是算不出，只是没必要")
            exit()

if __name__ == '__main__':
    fn = Fibonacci()