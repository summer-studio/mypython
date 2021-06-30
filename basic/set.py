#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s = {1, 2, 3}
print(s)

s = {1, 2, 2, 3, 4}
print(s)

s.add(5)
print(s)

s.remove(5)
print(s)

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 & s2
print(s3)
s4 = s1 | s2
print(s4)