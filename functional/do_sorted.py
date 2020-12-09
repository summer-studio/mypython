#!/usr/bin/env python3
# -*- coding: utf-8 -*-

arr = sorted([9, 1, 876])
print(arr)

arr = sorted([-2, 1, 3], key=abs)
print(arr)

char = sorted(['jack', 'Atom', 'tom'])
print(char)

char = sorted(['jack', 'Atom', 'tom'], key=str.lower, reverse=True)
print(char)
