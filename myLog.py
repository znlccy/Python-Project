#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = 'znlccy znlccy0603@163.com'

import logging
import getpass
import sys

#定义MyLog类

class MyLog(object):
    '''这个类用于创建一个自用的log'''

    def __init__(self):

        user = getpass.getuser()
        self.logger = logging.getLogger(user)
        self.logger.setLevel(logging.DEBUG)
        logFile = './' + sys.argv[0][0:-3] + '.log'
        formatter = logging.Formatter('%(asctime)-12s %(levelname)-8s %(name)-10s %(message)-12s')

        '''日志显示到屏幕上并输出到日志文件内'''
        logHand = logging.FileHandler(logFile)
        logHand.setFormatter(formatter)
        logHand.setLevel(logging.ERROR)


        logHandSt = logging.StreamHandler()
        logHandSt.setFormatter(formatter)

        self.logger.addHandler(logHand)
        self.logger.addHandler(logHandSt)

    '''日志的5个级别对应以下的5个函数'''
    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warn(self, msg):
        self.logger.warn(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)

if __name__ == '__main__':
    mylog = MyLog()
    mylog.debug("I'm debug")
    mylog.info("I'm info")
    mylog.warn("I'm warn")
    mylog.error("I'm error")
    mylog.critical("I'm error")