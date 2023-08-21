#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas
import pathlib
import math
import os
from map import custom_map

basePath = pathlib.Path(__file__).parent.absolute()


def merge_data():
    dataPath = basePath.joinpath("../data/")
    with open(dataPath.joinpath("all.csv"), mode="w+") as f:
        f.write(
            "name,main_category,sub_category,image,link,ratings,no_of_ratings,discount_price,actual_price\n"
        )
        f.flush()
        for file in dataPath.iterdir():
            print("Processing file:", file)
            dataFile = open(file)
            lines = dataFile.readlines()
            if len(lines) > 1:
                f.writelines(lines[1:])
                f.write("\n")
                f.flush()
            dataFile.close()


def load_data():
    dataPath = basePath.joinpath("../data/all.csv")
    result = []
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
    merge_data()
    data = load_data()
    mapOutput = custom_map(category_mapper, data)
    ratings = mapOutput.keys()
    for rating in ratings:
        print(rating, ":", len(mapOutput.read(rating)))


if __name__ == "__main__":
    main()
