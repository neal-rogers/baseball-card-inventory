#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This program creates player matches from a table."""


def get_matches(players):
    """This function takes a list of names and generates a list of matches.

    Args:
        players(list): List of player names.

    Returns:
        matches(list): List of player matches.

    Examples:
        >>> task_01.get_matches(['Harry', 'Howard', 'Hugh'])
        [('Harry', 'Howard'), ('Harry', 'Hugh'), ('Howard', 'Hugh')]
    """

    matches = []
    for index_1, name_1 in enumerate(players):
        for index_2, name_2 in enumerate(players):
            if name_1 is not name_2 and index_1 < index_2:
                matches.append((name_1, name_2))
            else:
                continue

    return matches
