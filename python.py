#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def fun_SplitLine(tmp):
    print()
    print('//////////////////////////////////////////////')
    print("Test for %s" % tmp)

def fun_TestInt():
    fun_SplitLine('int')

def fun_TestListTuple():
    fun_SplitLine('list and tuple')
    x=1
    y=2
    list_a = [1,2,3,4]
    tuple_a = (1,2,3,[x,y])
    print(tuple_a[-1][-1])
    y=3
    print(tuple_a[-1][-1])

main():
    print('Hello World!')