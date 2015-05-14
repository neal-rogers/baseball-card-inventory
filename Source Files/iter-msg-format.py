#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This program loops through a list of tuples, gets values, and creates a new
list."""


def prepare_email(appointments):
    """This function loops through and inserts values into a string.

    Args:
        appointment(list): List of tuples.

    Returns:
        message(list): List with formatted strings of referenced values.

    Example:
        >>> prepare_email([('Jen', '2015'), ('Max', 'March 3')])
        ['Dear Jen,\nI look forward to meeting with you on /2015.\nBest,\nMe',
        'Dear Max,\nI look forward to meeting with you on /March 3.\nBest,\nMe']
    """

    record = 0
    message = []
    template = 'Dear {},\nI look forward to meeting with you on {}.\nBest,\nMe'
    for member in appointments:
        member = appointments[record]
        name = member[0]
        date = member[1]
        record += 1
        message.append(template.format(name, date))

    return message
