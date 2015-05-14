#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is a simple baseball card inventory system."""

import graphx

print graphx.BANNER

f-ask = raw_input('What would you like to do?, "Update", "Search" or "Report"?: ').title()

try:
    if f-ask == 'Update':
        f-reply = 'Add'
    elif f-ask == 'Search' OR 'Report':
        f-reply = 'Search by'
except TypeError:
    pass

"""f-reply = raw_input("{f-reply}"?: '.format(f-reply).title()

if ACCENT == 'Ceramic Glaze':
    HIGHLIGHT_1 = 'Basically White'
    HIGHLIGHT_2 = 'White'
elif ACCENT == 'Cumulus Nimbus':
    HIGHLIGHT_1 = 'Off-White'
    HIGHLIGHT_2 = 'Paper White'
"""
