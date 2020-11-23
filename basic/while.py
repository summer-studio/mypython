#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = 1
while n <= 10:
    if n > 5:
        break
    if n % 2 == 0:
        continue
    print(n)
    n = n + 1
print("end")
