#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random


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

def fun_TestString():
    fun_SplitLine('string')
    s='Hello' + 'World' + ' !'
    print(s)

def fun_TestSetDict():
    fun_SplitLine(set and dict)
    set_a = set([1,2,3,4])
    dict_b = {'Cable': 630, 'Cyborg': 650, 'Electron': 850}
    set_c = set([2,3,4,5])
    print('set show:')
    print(set_a)
    print(dict_b['Cyborg'])

def fun_TestLogic():
    fun_SplitLine('if')
    num = input('Type a number between 1 and 10:')
    num = int(num)
    if num == 1:
        print('You are the No.1')
    elif 2<= num <= 4:
        print('加油')
    elif 5<= num <=10:
        print('ありがとう')
    else:
        print('This is a job. Do you?')

    fun_SplitLine('for')
    dict_team = {'Lily':0,'Leo':0,'Nancy':0,'Conan':0,'Tom':0}
    str_winner = ''
    int_winscore = 0

    print('As below the team members, there is a winner.')
    print('They are Lily, Leo, Nancy, Conan, and Tom.')
    tmp = input('Do you know who is the winner?')
    for n in dict_team:
        i = random.randint(0,100)
        print("%s's test scores is %d." %(n,i))
        dict_team[n] = i
        if i > int_winscore:
            int_winscore = i
            str_winner = n
    print('The winner is %s, the score is %d' % (str_winner,int_winscore))
    if tmp == str_winner:
        print('Congratulation!')
    else:
        print('Game over.')
    


if __name__ == "__main__":
    print('''Hello World!
Test content:
1. int
2. list and tuple
3. float
4. string
5. boolean
6. set and dict
7. logic 'for and if'
    ''')
    num = int(input('Type the test number:'))
    if num == 1:
        fun_TestInt()
    elif num ==2:
        fun_TestListTuple()
    elif num == 3:
        fun_TestFloat()
    elif num == 4:
        fun_TestString()
    elif num == 5:
        pass
    elif num == 6:
        fun_TestSetDict()
    elif num == 7:
        fun_TestLogic()
    else:
        print('END.')