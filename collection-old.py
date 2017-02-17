#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is a simple baseball card inventory system."""


import graphx, csv, json, os


def check_file(self):
    """Args:
        None.
    Returns:
        something() = stuff.

    Examples:
        >>> 
    """
    
    if os.path.isfile('data\cards.json'):
        print 'Loading database.'
        jsoncards = open('data\cards.json', 'a')
    else:
        print 'No file found, importing from CSV...'
        csvcards = open('data\cards.csv', 'r')
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

        csv_rdr = csv.DictReader(csvcards, fields)
        jsoncards = open('data\cards.json', 'a')

        with jsoncards:
            for row in csv_rdr:
                json.dump(row, jsoncards)
                jsoncards.write('\n')

        csvcards.close()
        print 'Import complete.'        
#csvfile = open('cards.csv', 'r')
#jsonfile = open('cards.json', 'w')

ask_1 = raw_input('What would you like to do?, Update, Search, or Report?: ').title()

if ask_1 == 'Update':
    reply_1 = 'Add'
elif ask_1 == 'Search' or 'Report':
    reply_1 = 'Search By'

ask_2 = raw_input('{A}? '.format(A=reply_1)).title()

if ask_2 == 'Yes' or 'Add':
    raw_input('Enter player name, position, team: ')
elif ask_2 == 'Search' or 'Report':
    reply_2 = 'Search By'

    uid += len() 
#    new_card = {'uid': , 'player': , 'position': , 'cid': , 'year': , 'condition':}
    sreply = 'Add'
elif fask == 'Search' or 'Report':
    sreply = 'Search By'

nask = raw_input('{A}? '.format(A=freply)).title()
"""
"""
              
if ask_3 == 'Report':
    pass

# def c_sold ():


def main():
    print graphx.BANNER


if __name__ == '__main__':
    main()