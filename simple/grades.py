#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import reduce

data = [
    {
        "name": "Rothcold",
        "gender": "male",
        "grade": 30,
    },
    {
        "name": "John",
        "gender": "male",
        "grade": 60,
    },
    {
        "name": "Tim",
        "gender": "male",
        "grade": 80,
    },
    {
        "name": "Lily",
        "gender": "female",
        "grade": 80,
    },
    {
        "name": "Lucy",
        "gender": "female",
        "grade": 95,
    },
    {
        "name": "Jane",
        "gender": "female",
        "grade": 93,
    },
    {
        "name": "Stacy",
        "gender": "female",
        "grade": 100,
    },
]


def main():
    boys = [
        x
        for x in map(lambda item: item if item["gender"] == "male" else None, data)
        if x is not None
    ]
    girls = [
        x
        for x in map(lambda item: item if item["gender"] == "female" else None, data)
        if x is not None
    ]
    passedBoys = [
        x
        for x in map(lambda item: item if item["grade"] >= 60 else None, boys)
        if x is not None
    ]
    passedGirls = [
        x
        for x in map(lambda item: item if item["grade"] >= 60 else None, girls)
        if x is not None
    ]

    print("%d boys passed, total %d" % (len(passedBoys), len(boys)))
    print("%d girls passed, total %d" % (len(passedGirls), len(girls)))

    def reducer(a, b):
        if b["grade"] > a["grade"]:
            return b
        else:
            return a

    topBoy = reduce(reducer, boys)
    topGirl = reduce(reducer, girls)
    print("Top Boy is", topBoy["name"], ", his grade is", topBoy["grade"])
    print("Top Girl is", topGirl["name"], ", her grade is", topGirl["grade"])


if __name__ == "__main__":
    main()
