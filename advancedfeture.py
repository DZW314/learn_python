#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from baserole import fun_SplitLine

def fun_TestListTuple():
    fun_SplitLine('list and tuple')
    x=1
    y=2
    list_a = [1,2,3,4,5,6,7,8,9,10]
    tuple_a = (1,2,3,[x,y])
    print(tuple_a[-1][-1])
    y=3
    print(tuple_a[-1][-1])