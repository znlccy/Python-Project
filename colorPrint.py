#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = 'znlccy znlccy0603@163.com'

import sys

class ColorPrint(object):

    def __init__(self, color, msg):
        self.color = color
        self.msg = msg
        self.cPrint(self.color, self.msg)

    def cPrint(self, color, msg):
        colors = {
            'black' : '\033[1;30;47m',      #黑色
            'red' : '\033[1;31;47m',        #红色
            'green' : '\033[1;32;47m',      #绿色
            'yellow' : '\033[1;33;47m',     #黄色
            'blue' : '\033[1;34;47m',       #蓝色
            'white' : '\033[1;37;47m'       #白色
        }
        if color not in colors.keys():
            print(u"输入的颜色暂时没有，按系统默认设置的颜色打印")
        else:
            print(u"输入的颜色有效，开始色彩打印")
            print(u"%s" %colors[color])
            print(msg)
            print(u"\033[0m")

if __name__ == '__main__':
    cp = ColorPrint(sys.argv[1], sys.argv[2])