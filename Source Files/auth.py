#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This program prompts for a password."""

import authentication
import getpass


def login(username, maxattempts=3):
    """This function takes input from a user and checks the password.

       Arg:
           username(str): String input from user.
           maxattempts(int): Max attempts for login.

        Return:
            auth(boolean): True or False if user successfully authenticated
            before hitting maximum no. of failed attempts.

        Examples:
                >>>login('mike', 4)
                    Incorrect username or password. You have 4 attempts.
                    Incorrect username or password. You have 3 attempts.
                    Incorrect username or password. You have 2 attempts.
                    Incorrect username or password. You have 1 attempts.
                    Incorrect username or password. You have 0 attempts.
                    False
    """

    auth = False
    user_login = 'Please enter your password: '
    auth_fail = "Incorrect username or password. You have" ' {} '  "attempts."
    attempt = 1
    while attempt <= maxattempts:
        passwd = getpass.getpass(user_login)
        message = authentication.authenticate(username, passwd)
        if message:
            auth = True
            break
        else:
            print auth_fail.format(maxattempts - attempt)
            attempt += 1

    return auth
