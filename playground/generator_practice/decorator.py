#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import traceback

"""
refer: http://www.shuwasystem.co.jp/products/7980html/2655.html
Python入門(2&3) 第12章のデコレータ
"""

def run():
    def decorate(f):
        f.x = 1
        return f
    
    @decorate
    def func():
        pass
    
    print(func.x)

def fail_run():
    """
    存在しないデコレーターを呼ぶ
    """
    try:
        @nai_decorate
        def func():
            pass
        
        print(func.x)
    except Exception as e:
        # ログ出力はこんな感じでやると良い
        # NameErrorの例外が出る模様
        logging.error(traceback.format_exc())
        logging.exception(e)

def run2():
    def add_two(f):
        def new_f(*args, **kwds):
            result = f(*args, **kwds)
            return result + 2
        return new_f

    def add_three(f):
        def new_f(*args, **kwds):
            result = f(*args, **kwds)
            return result + 3
        return new_f


    @add_two
    def func():
        return 1224
    print(func())

    @add_three
    def func():
        return 1234
    print(func())

if __name__ == '__main__':
    run()
    # fail_run()
    run2()
