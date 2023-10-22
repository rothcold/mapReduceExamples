#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas
import pathlib
import math
import os
from map import custom_map
from reduce import custom_reduce

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


def rating_reducer(val, item):
    try:
        rating = float(item["ratings"])
        if math.isnan(rating):
            return val
        val["sum_ratings"] += rating
        val["count"] += 1
        return val
    except:
        return val


def main():
    data = load_data()
    mapOutput = custom_map(category_mapper, data)
    categories = mapOutput.keys()
    for category in categories:
        ratings = custom_reduce(rating_reducer, mapOutput.read(
            category), {"sum_ratings": 0, "count": 0})
        print("Avarage Rating for %s: %f" %
                (category, ratings["sum_ratings"]/ratings["count"]))


if __name__ == "__main__":
    main()
