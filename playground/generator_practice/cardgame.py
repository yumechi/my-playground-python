#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
refer: http://www.shuwasystem.co.jp/products/7980html/2655.html
Python入門(2&3) 第9章のTIPSを写経して、コードを追加して分析
"""

def get_player(name: str, cards: list):
    turn = 0
    while True:
        if turn == 0:
            card = yield
        else:
            card = (yield cards.pop(0))
        cards.append(card)
        print("{name} got {card}: {cards}".format(name=name, card=card, cards=cards))
        turn += 1

def run(command: str):
    player1 = get_player('p1', [1, 2, 3])
    player2 = get_player('p2', [4, 5, 6])
    
    if command == "1":
        # 書式の掲載例がPython2であるため、Python3対応
        next(player1)
        next(player2)

    print(player1, player2)
    
    card = 7
    for turn in range(5):
        if command == "1":
            card = player1.send(card)
            card = player2.send(card)
        else:
            # send しなかったらどうなるのか？
            next(player1)
            next(player2)

def hoge_func(n:  int):
    """ 
    ganaratorの動作検証。
    yieldあるとganaratorと認識されるっぽい
    """ 
    i = 0
    for i in range(n):
        yield i
        return 1

def run2():
    f1 = hoge_func(3)
    print(f1)

    try:
        # returnで即値が帰る場合でもnextできてるっぽいけど
        # 進んでいるだけで意味がなさそう
        # よくわからないので、yieldとreturnを両方書かないほうが
        # 良さそうだなあという直感が働く
        next(f1)
        next(f1)
        print(f1)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    # トランプゲーム呼び出し
    run(command=input('1を入力すると普通に動作します -> '))
    # generatorの動作検証
    run2()
