#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
from hanoi import hanoi
from baserole import *
from advancedfeture import fun_TestListTuple

def fun_TestInt():
    fun_SplitLine('int')
    a = 1
    b = 10_000_000
    c = 0xff
    print(f'''整数a的值：{a}
带下划线的整数b的值：{b}
十六进制c的值：{c}
    ''')

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
    fun_helloworld('D')
    print('''Test or Game:
    1. Test
    2. Game
    ''')
    numl1 = int(input('Type the number:'))
    if numl1 == 1:
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
        numl2 = int(input('Type the test number:'))
        if numl2 == 1:
            fun_TestInt()
        elif numl2 ==2:
            fun_TestListTuple()
        elif numl2 == 3:
            fun_TestFloat()
        elif numl2 == 4:
            fun_TestString()
        elif numl2 == 5:
            pass
        elif numl2 == 6:
            fun_TestSetDict()
        elif numl2 == 7:
            fun_TestLogic()
        else:
            print('END.')
    elif numl1 == 2:
        hanoi()
    else:
        print('END.')