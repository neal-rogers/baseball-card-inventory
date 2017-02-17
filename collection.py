#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is a simple baseball card inventory system."""


import csv, json, graphx



def csvimport(csvdata):
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
    reader = csv.DictReader(csvdata, fields)
    for row in reader:
        json.dump(row, jsonfile)
        jsonfile.write('\n')

    jsonfile.close()

def main():
    #print graphx.BANNER
    csvfile = open('data\cards.csv', 'r')
    csvimport(csvfile)

if __name__ == '__main__':
    main()