#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    a = {'b', 'f', 'g', 'm', 'o'}
    b = {'b', 'g', 'h', 'l', 'u'}
    c = {'e', 'f', 'm'}
    d = {'e', 'g', 'l', 'p', 'q', 'u', 'v'}
    all_ = a.union(b).union(c).union(d)
    x = ((a.difference(b))).union(c.intersection(d))
    y = (all_.difference(a).intersection(all_.difference(b))).difference(c.union(d))

    if x:
        print(f'x = {x}')
    else: print("x - пустое множество")
    if y:
        print(f'y = {y}')
    else: print("y - пустое множество")
