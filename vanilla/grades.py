#!/usr/bin/env python
# -*- coding: utf-8 -*-

from map import custom_map

if __name__ == "__main__":
    arr = [
        {"name": "1", "type": "a"},
        {"name": "2", "type": "a"},
        {"name": "3", "type": "b"},
    ]

    def mapper(item):
        return item["type"], item["name"]

    output = custom_map(mapper, arr)

    print(output.read("a"))
    print(output.read("b"))
