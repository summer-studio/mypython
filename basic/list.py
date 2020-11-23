#!/usr/bin/env python3
# -*- coding: utf-8 -*-

classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(len(classmates))

first = classmates[0]
print(first)

second = classmates[1]
print(second)

last = classmates[-1]
print(last)

lastButOne = classmates[-2]
print(lastButOne)

classmates.append("Adam")
print(classmates)

classmates.insert(1, 'jack')
print(classmates)

classmates.pop()
print(classmates)

classmates.pop(1)
print(classmates)

classmates[1] = 'Sarah'
print(classmates)

L = ['Apple', 123, True]
print(L)

s = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(s))
print(s)

classmatesTuple = ('Michael', 'Bob', 'Tracy')
print(classmatesTuple)
print(classmatesTuple[0])
