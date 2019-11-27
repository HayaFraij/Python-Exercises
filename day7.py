##!/usr/bin/env python3
## -*- coding: utf-8 -*-
#"""
#Created on Wed Nov 27 09:35:19 2019
#
#@author: owner
#"""
#
from numpy import *
#
#arrZeros = zeros(10)
#print(arrZeros)
#
#arrOnes = ones(10)
#print(arrOnes)
#
#arrFives = ones(10)*5
#print(arrFives)
#
#arr = array(range(30, 71))
#print(arr)
#
#
#arr = zeros((3, 3))
#counter = 0
#for x in range(0, 3):
#    if x == counter:
#       arr[x][x] = 1
#    counter += 1
#print(arr)
#print(identity(3))
  
#randomm = random.random(1)
#print(randomm)  

   
#arr = array([[1, 2, 3, 4], [5, 6, 7, 8], [1, 2, 3, 4]])   
#for x in arr:
#    print(x)
#    
#arr = arange(0, 21)
#print(arr)
#
#for x in range(9, 16):
#    arr[x] *= -1
#print(arr)

#x = array([1, 8, 3, 5])
#y = random.randint(0, 11, 4)
#print(x * y)

#def arr(x):
#    print("#rows =", x.shape[0])
#    print("#columns =", x.shape[1])
#    print(x)
#x = array([[1, 8, 3, 5], [1, 2, 4, 3]])
#arr(x)

#arr = random.random((3, 3, 3))
#print(arr)


#a = array([9, -1, 2, 5])
#b = array([6, -1, 0, 10])
#c = array([[1, 8, 2, 5],[3,1,7,9]])
#print("a-b: ",a-b)
#print("a*b: ",a*b)
#print("a.dot(b): ",a.dot(b))
#print("a*2: ",a*2)
#print("np.sin(a): ",sin(a))
#print("a<3: ",a<3)
#print("a.sum(): ",a.sum())
#print("a.sum(axis=0): ",a.sum(axis=0))
#print("c.sum(): ",c.sum())
#print("c.sum(axis=0): ",c.sum(axis=0))
#print("a.min(): ",a.min())
#print("a.max(): ",a.max())
#print("a.mean(): ",a.mean())
#print("a average(): ",average(a))
#print("a median(): ",median(a))
#print("a std(): ",std(a))
#print("a var(): ",var(a))
#print("c.cumsum(): ",c.cumsum())
#print("a[1:2] : ",a[1:2])
#print("a[2:] : ",a[2:])
#print("c[-1] : ",c[-1])


import matplotlib.pyplot as plt

#x = array(range(1, 50))
#y = x * 3
#
#plt.plot(x, y)
#plt.ylabel('Y-axis')
#plt.xlabel('X-axis')
#plt.title("Draw a line..")
#plt.show()

#x1 = [10, 20, 30]
#y1 = [20, 40, 10]
#
#y2 = [40, 10, 30]
#
#plt.plot(x1, y1,"b-",label='line1')
#plt.plot(x1, y2,"y-", label='line2')
#plt.xlabel('X-axis')
#plt.ylabel('Y-axis')
#plt.title('Two or more lines on same plot with suitable legends')
#plt.legend()
#plt.show()

#import numpy as np
#import matplotlib.pyplot as plt
#t = np.arange(0., 5., 0.2)
#plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3,
#'g^')
#plt.show()

x = ('Python', 'Java', 'PHP', 'Javascript', 'C#', 'C++')
y_pos = arange(len(x))
popularity = [22.2,17.6,8.8,8,7.7,6.7]

plt.bar(y_pos, popularity, color=['red','black','green','blue','yellow','blue'], align='center', alpha=0.5)
plt.xticks(y_pos, x)
plt.ylabel('Popularity')
plt.title('Popularity of Programming language')

plt.show()





