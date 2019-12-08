#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 14:05:42 2019

@author: owner
"""

import sqlite3

conn = sqlite3.connect('stocks.db')

c = conn.cursor()

symbol = 'RHAT'
#c.execute('SELECT price FROM stocks WHERE symbol = "%s"' %symbol)
#c.execute('SELECT * FROM stocks')
c.execute('SELECT * FROM sqlite_master')


print(c.fetchall())
#for row in c:
#    print(row)

#for row in c.execute('SELECT symbol, gty, price FROM stocks ORDER by price'):
#    print(row)


conn.close()