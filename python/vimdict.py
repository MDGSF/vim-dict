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


def getRange():
    buf = vim.current.buffer
    if buf is None:
        print("vim.current.buffer is None.")
        return
    return vim.eval("@*")


def getWordUnderCursor():
    wordUnderCursor = vim.eval("expand('<cword>')")
    trimdWord = ''.join(list(filter(str.isalnum, wordUnderCursor)))
    return trimdWord


def Python_QueryWord(word):
    sqlitename = os.path.join(os.path.dirname(__file__), 'stardict.db')
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


def Normal_Python_QueryWord():
    word = getWordUnderCursor()
    Python_QueryWord(word)


def Visual_Python_QueryWord():
    txt = getRange()
    Python_QueryWord(txt)


def Python_input(message='input'):
    vim.command('call inputsave()')
    vim.command("let user_input = input('" + message + ": ')")
    vim.command('call inputrestore()')
    return vim.eval('user_input')


def CEnter_Python_QueryWord():
    word = Python_input("Please enter the word")
    Python_QueryWord(word)
