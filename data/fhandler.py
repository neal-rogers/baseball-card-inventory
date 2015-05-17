#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Package file for card collection inventory."""


import csv

def fhandler(self):
        """Docstring.
        """
        
        try:
            fhandler = open(self.logfilename, 'r')
        except IOError:
            self.log('Log file not found.'
        for index, entry in enumerate(self.msgs):
            fhandler.write(str(entry) + '\n')
            handled.append(index)

        for index in handled[::-1]:
            del self.msgs[index]

        fhandler.close()
