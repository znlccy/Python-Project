#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'znlccy znlccy0603@163.com'

class ShowList(object):

    def __init__(self):
        self.L1 = []
        self.L2 = []

        self.createList()           #创建列表
        self.insertData()           #插入数据
        self.appendData()           #追加数据
        self.deleteData()           #删除数据
        self.subList()              #列表切片

    #创建列表方法
    def createList(self):
        print(u"创建列表: ")
        print("L1 = list('abcdefg')")
        self.L1 = list('abcdefg')
        print("L2 = []")
        print("for i in xrange(0, 10):")
        print("\tL2.append(i)")
        for i in xrange(0, 10):
            self.L2.append(i)
        print("L1 = ")
        print(self.L1)
        print("L2 = ")
        print(self.L2)
        print("\n")

    def insertData(self):
        print(u"插入数据")
        print(u"L1列表中第3个位置插入数字100，执行命令: L1.insert(3,100)")
        self.L1.insert(3, 100)
        print("L1 = ")
        print(self.L1)
        print(u"L2列表中第10个位置插入字符串'python',执行命令: L2.insert(10, 'python')")
        self.L2.insert(10, 'python')
        print("L2 = ")
        print(self.L2)
        print("\n")

    def appendData(self):
        print(u"追加数据")
        print(u"L1列表尾追加一个列表[1,2,3], 执行命令: L1.append([1,2,3])")
        self.L1.append([1,2,3])
        print("L1 = ")
        print(self.L1)
        print(u"L2列表尾追加一个元组('a', 'b', 'c'), 执行命令L2.append(('a', 'b', 'c'))")
        self.L2.append(('a', 'b', 'c'))
        print("L2 = ")
        print(self.L2)
        print("\n")

    def deleteData(self):
        print(u"删除数据")
        print(u"删除L1的最后一个元素,执行命令:L1.pop()")
        self.L1.pop()
        print("L1 = ")
        print(self.L1)
        print(u"删除L1的第一个元素,执行命令:L1.pop(0)")
        self.L1.pop(0)
        print("L1 = ")
        print(self.L1)
        print(u"删除L2的第四个元素,执行命令:L2.pop(3)")
        self.L2.pop(3)
        print("L2 = ")
        print(self.L2)
        print("\n")

    def subList(self):
        print(u"列表切片")
        print(u"取得列表L1的第3到最后一个元素组成新的列表,执行命令:L1[2:]")
        print(self.L1[2:])
        print(u"取列表L2的第2个到倒数第2个元素组成的新列表,步长为2,执行命令:L2[1:-1:2]")
        print(self.L2[1:-1:2])
        print("\n")

if __name__ == '__main__':
    showList = ShowList()