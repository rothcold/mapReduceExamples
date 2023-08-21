#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import reduce


def main():
    numbers = [1, 2, 6, 3, 4, 5]
    result = map(lambda x: x**2, numbers)
    for i in result:
        print(i)

    reduceResult = reduce(reducer, numbers)
    print(reduceResult)


def reducer(a, b):
    print(a, ":", b)
    if b > a:
        return b
    return a


if __name__ == "__main__":
    main()
