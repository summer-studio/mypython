#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

# 位置参数
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(2, 3))


# 默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(2))


def add_end(L=[]):
    L.append('END')
    return L


print(add_end())
print(add_end())


# 默认参数必须指向不变对象，否则会出现逻辑错误
def add_end2(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


print(add_end2())
print(add_end2())


def calc(numbers):
    sum = 0
    for n in numbers:
        sum += n * n
    return sum


print(calc([1, 2, 3]))


# 可变参数
def calc_variable(*numbers):
    sum = 0
    for n in numbers:
        sum += n * n
    return sum


print(calc_variable(1, 2))


# 关键字参数
def keyword_func(name, age, **kw):
    print('name:', name, ',age:', age, ',kw:', kw)


print(keyword_func('bob', 20, city='hz'))

extra = {'city': 'Beijing', 'job': 'Engineer'}
print(keyword_func('jack', 21, **extra))


# 命名关键字参数
def keyword_func2(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:', name, ',age:', age, ',kw:', kw)


print(keyword_func2('ss', 22, city='sz'))


# 限制关键字参数的名字
def keyword_func3(name, age, *, city, job):
    print(name, age, city, job)


print(keyword_func3('ss', 24, city='hz', job='rd'))
