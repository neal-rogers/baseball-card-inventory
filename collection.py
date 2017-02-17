#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is a simple baseball card inventory system."""


import csv, json, graphx


csvfile = open('data\cards.csv', 'r')
jsonfile = open('data\cards.json', 'w')
fields = (
            "UID",
            "PLAYER",
            "POSITION",
            "BRAND",
            "CID",
            "YEAR",
            "CONDITION",
            "SOLD",
            "VALUE"
            )

reader = csv.DictReader(csvfile, fields)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')

def main():
    print graphx.BANNER


if __name__ == '__main__':
    main()