#!/usr/bin/env python
# -*- coding: utf-8 -*-

def custom_reduce(reducer, iter, initializer):
    val = initializer
    for item in iter:
        val = reducer(val, item)
    return val