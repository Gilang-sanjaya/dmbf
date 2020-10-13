#!/usr/bin/python
#-*-coding:utf-8-*-

import os, sys

sys.path.append('lib')
sys.path.append('lib/language')

import dmbf

path = ['result', 'cache', 'dump']

for f in path:
    if os.path.exists(f) == False:
        os.mkdir(f)

if (__name__ == '__main__'):
    dmbf.main()