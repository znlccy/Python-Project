#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = 'znlccy znlccy@126.com'

import os
import platform
import itertools
import time

def main():
    '''主程序'''
    global rawList                  #原始数据列表
    rawList = []
    global denyList                 #非法单词列表
    denyList = [' ', '', '@']
    global pwList                   #最终密码列表
    pwList = []
    global minLen                   #密码最小长度
    minLen = 6
    global maxLen                   #密码最大长度
    maxLen = 16
    global timeout                  #超时时间
    timeout = 3
    global flag                     #标签
    flag = 0
    run = {
        '0' : exit,                 #退出
        '1' : getRawList,           #创建原始列表
        '2' : addDenyList,          #添加不可能出现的元素
        '3' : clearRawList,         #清空列表
        '4' : setRawList,           #原始列表排序
        '5' : modifyPasswordLen,    #修改最终的密码长度
        '6' : createPasswordList,   #创建最终的字典列表
        '7' : showPassword,         #显示密码
        '8' : createPasswordFile    #创建密码文件
    }
    while True:
        mainMenu()
        op = raw_input("输入选项:")
        if op in map(str, range(len(run))):
            run.get(op)()
        else:
            tipMainMenuInputError()
            continue

def mainMenu():
    '''主菜单'''
    global denyList
    global rawList
    global pwList
    global flag
    clear()
    print(u'=' * 40)
    print(u'||                                      ||')
    print(u'|| 0:退出程序                           ||')
    print(u'|| 1:输入密码原始字符串                 ||')
    print(u'|| 2:添加非法字符到列表                 ||')
    print(u'|| 3:清空原始密码列表                   ||')
    print(u'|| 4:整理原始密码列表                   ||')
    print(u'|| 5:改变默认密码长度(%d-%d)             ||' %(minLen, maxLen))
    print(u'|| 6:创建密码列表                       ||')
    print(u'|| 7:显示所有密码                       ||')
    print(u'|| 8:创建字典文件                       ||')
    print(u'||')
    print(u'='*40)
    print(u'当前非法字符为: %s' %denyList)
    print(u'当前原始密码元素为: %s' %rawList)
    print(u'共有密码%d个' %len(pwList))
    if flag:
        print(u'已在当前目录创建密码文件dic.txt')
    else:
        print(u'尚未创建密码文件')

def clear():
    '''清屏函数'''
    OS = platform.system()
    if (OS == u'Windows'):
        os.system('cls')
    else:
        os.system('clear')

def tipMainMenuInputError():
    '''错误提示'''
    clear()
    print(u"只能输入0-7的整数，等待%d秒后重新输入" %timeout)
    time.sleep(timeout)

def getRawList():
    '''获取原始数据列表'''
    clear()
    global denyList
    global rawList
    print(u"输入回车后直接退出")
    print(u"当前原始面列表为: %s" %rawList)
    st = None
    while not st == '':
        st = raw_input("请输入密码元素字符串: ")
        if st in denyList:
            print(u"这个字符串是预先设定非法字符串")
            continue
        else:
            rawList.append(st)
            clear()
            print(u"输入回车后直接退出")
            print(u"当前原始面列表为: %s" % rawList)

def addDenyList():
    '''添加非法词'''
    clear()
    print(u"输入回车后直接退出")
    print(u"当前非法字符为:%s" %denyList)
    st = None
    while not st == '':
        st = raw_input("请输入需要添加的非法字符串: ")
        denyList.append(st)
        clear()
        print(u"输入回车后直接退出")
        print(u"当前非法字符列表为:%s" %denyList)

def clearRawList():
    '''清空原始数据列表'''
    global rawList
    rawList = []

def setRawList():
    '''整理原始数据列表'''
    global rawList
    global denyList
    a = set(rawList)
    b = set(denyList)
    rawList = []
    for str in set(a-b):
        rawList.append(str)


def modifyPasswordLen():
    print(u"清空")

def createPasswordList():
    print(u"清空")

def showPassword():
    print(u"清空")

def createPasswordFile():
    print(u"清空")

if __name__ == '__main__':
    main()