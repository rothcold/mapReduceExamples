#!/usr/bin/env python
# -*- coding: utf-8 -*-


class MapperOutput:
    def __init__(self):
        self.data = {}

    def write(self, key, data):
        if key not in self.data:
            self.data[key] = []
        self.data[key].append(data)

    def read(self, key):
        return self.data[key]

    def keys(self):
        return self.data.keys()


def custom_map(mapper, iter):
    output = MapperOutput()
    for item in iter:
        key, value = mapper(item)
        if key != None:
            output.write(str(key), value)

    return output
