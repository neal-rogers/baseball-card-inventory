#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is a simple baseball card inventory system."""

import graphx, csv, json, os


print graphx.BANNER

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

        

        jsoncards = open('cards.json', 'a')

        with jsoncards:
            for row in csv_rdr:
                json.dump(row, jsoncards)
#                jsoncards.write('\n')

#        csvcards.close()
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

def cardssold (filename):
    """Opens File using json and stores data in dict.
    Args:
        m_file = Opens file.
        m_read = Loads json file.
        m_data(dict) = Placeholder for data.

    Returns:
        m_data(dict) = Market density dictionary.

    Examples:
        >>> 
    """

    m_file = open(filename, 'r')
    m_read = json.load(cards)
    m_data = {}

    for values in m_read['data']:
        boro = values[8].strip()

        if boro in m_data:
            m_data[boro] += 1
        else:
            m_data[boro] = 1
    return m_data


def correlate_data(restaurants, markets, outputfile):
    """Combines Data for Boroughs and returns a Dict AVG Score, markets/restaur.
    Args:
        restaurants(dict) = Restaurant Score summary file.
        markets(dict) = Market Density summary file.

    Returns:
        None

    Examples:
    """

    restaurants = get_score_summary(restaurants)
    markets = get_market_density(markets)
    data_dict = {}

    for key, value in markets.iteritems():
        boro = key.upper()
        m_val = float(value)
        r_val = float(restaurants[boro][0])

        if boro in restaurants:
            data_dict[boro] = restaurants[boro][1], m_val/r_val

    with open(outputfile, 'w') as outfile:
        json.dump(data_dict, outfile)
