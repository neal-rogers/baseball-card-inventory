#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Simple color picker program."""

BASE = raw_input('Which base color, "Seattle Gray" or "Manatee"?: ').title()

if BASE == 'Seattle Gray':
    ACCENT_1 = 'Ceramic Glaze'
    ACCENT_2 = 'Cumulus Nimbus'
elif BASE == 'Manatee':
    ACCENT_1 = 'Platinum Mist'
    ACCENT_2 = 'Spartan Sage'

ACCENT = raw_input('Which accent color, "{A1}" or "{A2}"?: '.format(
     A1=ACCENT_1, A2=ACCENT_2)).title()

if ACCENT == 'Ceramic Glaze':
    HIGHLIGHT_1 = 'Basically White'
    HIGHLIGHT_2 = 'White'
elif ACCENT == 'Cumulus Nimbus':
    HIGHLIGHT_1 = 'Off-White'
    HIGHLIGHT_2 = 'Paper White'
elif ACCENT == 'Platinum Mist':
    HIGHLIGHT_1 = 'Bone White'
    HIGHLIGHT_2 = 'Just White'
elif ACCENT == 'Spartan Sage':
    HIGHLIGHT_1 = 'Fractal White'
    HIGHLIGHT_2 = 'Not White'

HIGHLIGHT = raw_input('Which highlight color, "{H1}" or "{H2}"?: '.format(
    H1=HIGHLIGHT_1, H2=HIGHLIGHT_2)).title()

print 'Your selected colors are, {B_CLR}, {A_CLR}, and {H_CLR}.'.format(
    B_CLR=BASE, A_CLR=ACCENT, H_CLR=HIGHLIGHT)
