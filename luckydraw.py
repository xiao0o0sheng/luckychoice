# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/1/10 13:28
# @Author : Xiaosheng Jin
# @Email : xiao0o0sheng@126.com
# @File : 超级大乐透2_大数据概率.py
# @Software: PyCharm


import random

a = [362, 335, 341, 305, 341, 320, 345, 300, 305, 326, 341, 304, 314, 326, 302, 273, 320, 321, 352, 334, 311, 367, 336,
     305, 331, 321, 327, 319, 417, 392, 358, 386, 414, 369, 415]
b = [364, 391, 391, 393, 403, 384, 419, 362, 390, 425, 399, 413]

i = 1
j = 1
drop1 = []
drop2 = []
for k in a:
    for ki in range(k):
        drop1.append(i)
    i += 1
for l in b:
    for li in range(l):
        drop2.append(j)
    j += 1

for lucky in range(5):
    r1 = []
    r2 = []
    res = []
    for m in range(5):
        v = random.choice(drop1)
        r1.append(v)
        while v in drop1:
            drop1.remove(v)
    for n in range(2):
        p = random.choice(drop2)
        r2.append(p)
        while p in drop2:
            drop2.remove(p)
    r1 = sorted(r1)
    r2 = sorted(r2)
    for ans1 in r1:
        ans1 = '{0:0>2s}'.format(str(ans1))
        res.append(ans1)
    for ans2 in r2:
        ans2 = '{0:0>2s}'.format(str(ans2))
        res.append(ans2)
    print(res)
