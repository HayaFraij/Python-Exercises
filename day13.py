#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 13:16:13 2019

@author: owner
"""

import sqlite3

conn = sqlite3.connect('stocks.db')

c = conn.cursor()

#c.execute('''CREATE TABLE stocks
#          (date text, trans text, symbol text, gty real, price real)''')

c.execute("INSERT INTO stocks VALUES ('2006-01-05', 'BUY', 'RHAT', 100, 35.14)")

c.execute("INSERT INTO stocks VALUES ('2006-01-05', 'SEL', 'RHAT', 50, 35.25)")

c.execute("INSERT INTO stocks VALUES ('2006-01-05', 'BUY', 'APPLE', 100, 35.25)")

c.execute("INSERT INTO stocks VALUES ('2006-01-05', 'SEL', 'APPLE', 50, 3.23)")

c.execute("INSERT INTO stocks VALUES ('2006-01-05', 'BUY', 'APPLE', 100, 4.49)")

c.execute("INSERT INTO stocks VALUES ('2006-01-05', 'SEL', 'APPLE', 50, 3.23)")

conn.commit()

conn.close()