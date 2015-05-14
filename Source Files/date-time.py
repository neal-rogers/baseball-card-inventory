#!/usr/bin/env python
# -*- coding: utf-8 *-*
"""This program imports the datetime module and returns current date & time."""

import datetime

CURDATE = None


def get_current_date():
    """This function should retrieve the current date and time.

    Args:
        none: Value specifying degrees Fahrenheit

    Returns:
        datetime.date.today(): Current system time

    Example:
        >>> get_current_date()
        datetime.date(2015, 3, 8)
    """
    return datetime.date.today()

if __name__ == '__main__':
    CURDATE = get_current_date()
    print CURDATE
