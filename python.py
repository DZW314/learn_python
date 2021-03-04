#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def fun_SplitLine(tmp):
    print()
    print('//////////////////////////////////////////////')
    print("Test for %s" % tmp)

def fun_TestInt():
    fun_SplitLine('int')
    a = 1
    b = 10_000_000
    c = 0xff
    print(f'''整数a的值：{a}
带下划线的整数b的值：{b}
十六进制c的值：{c}
    ''')

def fun_TestListTuple():
    fun_SplitLine('list and tuple')
    x=1
    y=2
    list_a = [1,2,3,4,5,6,7,8,9,10]
    tuple_a = (1,2,3,[x,y])
    print(tuple_a[-1][-1])
    y=3
    print(tuple_a[-1][-1])

def fun_TestFloat():
    fun_SplitLine('float')
    a=3.4e10
    b=10/3
    print('The float formate about 10/3 is')
    print(f'{b}, the type is {type(b)}.')


if __name__ == "__main__":
    print('''Hello World!
Test content:
1. int
2. list and tuple
3. float
4. string
5. boolean
    ''')
    num = int(input('Type the test number:'))
    if num == 1:
        fun_TestInt()
    elif num ==2:
        fun_TestListTuple()
    elif num == 3:
        fun_TestFloat()
    elif num == 4:
        print('string')
    elif num == 5:
        print('boolean')
    else:
        print('end')