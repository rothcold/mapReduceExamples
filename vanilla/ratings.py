#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas
import pathlib
import math
import os
from map import custom_map

basePath = pathlib.Path(__file__).parent.absolute()


def load_data():
    result = []
    for dataPath in basePath.joinpath("../data").iterdir():
        # dataPath = basePath.joinpath("../data/Strength Training.csv")
        print("Processing file:", dataPath)
        df = pandas.read_csv(dataPath, low_memory=False)
        for i, row in df.iterrows():
            item = {
                "name": row["name"],
                "main_category": row["main_category"],
                "sub_category": row["sub_category"],
                "image": row["image"],
                "link": row["link"],
                "ratings": row["ratings"],
                "no_of_ratings": row["no_of_ratings"],
                "discount_price": row["discount_price"],
                "actual_price": row["actual_price"],
            }
            result.append(item)
    return result


def category_mapper(item):
    return item["main_category"], item


def main():
    data = load_data()
    mapOutput = custom_map(category_mapper, data)
    ratings = mapOutput.keys()
    for rating in ratings:
        print(rating, ":", len(mapOutput.read(rating)))


if __name__ == "__main__":
    main()
