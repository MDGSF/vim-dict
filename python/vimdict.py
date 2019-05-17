#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import print_function
import sys
import time
import os
import io
import csv
import sqlite3
import codecs
import stardict
import vim

try:
    import json
except:
    import simplejson as json

def getWordUnderCursor():
    return vim.eval("expand('<cword>')")

def Python_QueryWord(dbpath):
    word = getWordUnderCursor()
    sqlitename = os.path.join(dbpath, 'stardict.db')
    sd = stardict.StarDict(sqlitename, False)
    result = sd.query(word)
    if result is None:
        print("Can't find, %s !!!" % word)
        return
    print(result['word'])
    if len(result['definition']) > 0:
        print(result['definition'])
    if len(result['translation']) > 0:
        print(result['translation'])

