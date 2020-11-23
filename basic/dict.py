#!/usr/bin/env python3
# -*- coding: utf-8 -*-

names = ['Michael', 'Bob', 'Tracy']
scores = [95, 75, 85]

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

d['Adam'] = 67
print(d['Adam'])

bob = d.get('Bob')
print(bob)

nothing = d.get("Jack", -1)
print(nothing)

d.pop('Tracy')
print(d)
