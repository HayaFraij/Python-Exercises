#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 16:43:46 2019

@author: owner
"""

import pandas as pd
import numpy as np

#data = pd.Series([2, 4, 6, 8, 10])
#print(data)
#
#d1 = pd.Series({'a': 100, 'b': 200, 'c':300, 'd':400, 'e':800})
#print(d1)
#
#data = pd.Series([20, 10, 150, 110, 100, 50])
#data.plot(kind="bar", color=["red", "black", "green", "blue", "yellow", "red"])



#Data = {'d1':[100,200,5,400,700,100,200,50,400,700],
#'d2':[140,0,300,400,200,140,0,700,400,200]}
#frame = pd.DataFrame(Data)
#print(frame)
#frame.plot()



#data = {'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}
#frame = pd.DataFrame(data)
#print(frame)



#names = ['Bob','Jessica','Mary','John','Mel']
#births = [968, 155, 77, 578, 973]
#frame = pd.Series(births,
#index=names, name='Birthes')
#print(frame)
#frame.plot.pie(y='births', figsize=(5, 5))




#df = pd.read_csv('input.csv',sep='\t',index_col=0)
#print(df)
#df.to_csv('myDataFrame.csv', sep=',')



#dates = pd.date_range('20000101', periods=4)
#data = pd.DataFrame(np.random.randn(4, 2), index=dates, columns=['A', 'B'])
#print(data)
#print(data.head(2))
#print(data[['A']])
#print(data[0:1])
#print(data['20000102':'20000104'])
#print(data.loc['20000102':'20000104', ['A']])
#print(data.iloc[:, 1:2])
#print(data[data>0])
#print(data[data.B>0])
#data['A']=[100, 200, 300, 100]
#print(data)
#print(data[data['A'].isin([200, 300])])













