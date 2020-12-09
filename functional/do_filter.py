#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def is_odd(x):
    return x % 2 == 1


array = list(filter(is_odd, [1, 2, 3, 4, 5]))
print(array)
