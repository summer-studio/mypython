#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools


def int2(x, base=2):
    return int(x, base)


print(int2('1000000'))

int3 = functools.partial(int, base=2)
print(int3('1000000'))
