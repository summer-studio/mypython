#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 装饰器模式
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now():
    print("2020-01-01")


f = now
print(f())

print(f.__name__)
