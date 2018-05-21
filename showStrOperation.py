#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'znlccy znlccy0603@163.com'

class ShowStrOperation(object):

    def __init__(self):
        self.strCase()
        self.strFind()
        self.strSplit()
        self.strCode()
        self.strTest()

    def strCase(self):
        print(u"*********************字符串大小写转换**********************")
        print(u"演示字符串大小写转换")
        print "演示字符串S赋值为: 'ThIs is a PYTHON  '"
        S = '  ThIs is a PYTHON  '
        print "大写转换成小写: \tS.lower() \t= %s" %(S.lower())
        print "小写转换成大写: \tS.upper() \t= %s" %(S.upper())
        print "大小写转换: \t\tS.swapcase() \t= %s" %(S.swapcase())
        print "首字母大写: \t\tS.title() \t= %s" %(S.title())
        print "\n"

    def strFind(self):
        print(u"*********************字符串搜索、替换**********************")
        print "演示字符串搜索、替换"
        print "演示字符串S赋值为: 'ThIs is a PYTHON  '"
        S = 'ThIs is a PYTHON  '
        print "字符串搜索: \t\tS.find('is') \t= %s" %(S.find('is'))
        print "字符串统计: \t\tS,count('s') \t= %s" %(S.count('s'))
        print "字符串替换: \t\tS.replace('Is', 'is') \t= %s" %(S.replace('Is', 'is'))
        print "去左右空格: \t\tS.strip() \t=#%s#" %(S.strip())
        print "去左边空格: \t\tS.lstrip() \t=#%s#" %(S.lstrip())
        print "去右边空格: \t\tS.rstrip() \t=#%s#" %(S.rstrip())
        print "\n"

    def strSplit(self):
        print(u"*********************字符串分隔、组合**********************")
        print "演示字符串分割、组合"
        print "演示字符串S赋值为: 'ThIs is a PYTHON  '"
        S = 'ThIs is a PYTHON  '
        print "字符串分割: \t\tS.split() \t= %s" %(S.split())
        print "字符串组合1:  '#'.join(['This', 'is', 'a', 'python']) \t= %s" %('#'.join(['This', 'is', 'a', 'python']))
        print "字符串组合2:  '$'.join(['This', 'is', 'a', 'python']) \t= %s" %('$'.join(['This', 'is', 'a', 'python']))
        print "字符串组合3:  ' '.join(['This', 'is', 'a', 'python']) \t= %s" %(' '.join(['This', 'is', 'a', 'python']))
        print "\n"

    def strCode(self):
        print(u"*********************字符串编码、解码**********************")
        print "演示字符串编码、解码"
        print "演示字符串S赋值为: '编码解码测试'"
        S = '编码解码测试'
        print "GBK编码的S \t = %s" %(S)
        print "GBK编码的S转换unicode编码"
        print "S.decode('GBK') = %s" %(S.decode("GBK"))
        print "GBK编码的S转换UTF8"
        print "S.decode('GBK').encode('UTF8') = %s" %(S.decode("GBK").encode("UTF8"))
        print "注意: 不管是编码还是解码针对的都是Unicode字符编码， \n所以要编码或者解码之前必须先将源字符串转换为Unicode编码格式"
        print "\n"

    def strTest(self):
        print(u"*********************字符串测试**********************")
        print "演示字符串测试"
        print "演示字符串S赋值为: 'abcd'"
        S1 = 'abcd'
        print "测试S.isalpha() = %s" %(S1.isalpha())
        print "测试S.isdigit() = %s" %(S1.isdigit())
        print "测试S.isspace() = %s" %(S1.isspace())
        print "测试S.islower() = %s" %(S1.islower())
        print "测试S.isupper() = %s" %(S1.isupper())
        print "测试S.istitle() = %s" %(S1.istitle())

if __name__ == '__main__':
    showStrOperation = ShowStrOperation()