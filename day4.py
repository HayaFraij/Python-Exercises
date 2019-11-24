#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 14:04:15 2019

@author: owner
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
def func_name(name):
    print("Hello " + name)
    
func_name("Haya")
func_name("Omemeh")
#func_name()

def food(food1, *foood):
    print("1: " + food1)
    for t in foood:
        print(t)

fruit = ("apple", "orange", "another fruit", "another fruit2")

food("apple", "orange", "another fruit", "another fruit2")


def dic(**diction):
    for key, value in diction.items():
        print("%s => %s" %(key, value))


dic(name= "Haya", age= "24", edu= "industrial eng")


x = "awesome"

def myfunc():
    
    #x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

factorial(10)

sum = lambda x, y, z = 22 : x + y + z
print ( sum(56,7) )


my_pets = ['alfred', 'tabitha', 'william', 'arla']
uppered_pets = map(str.upper, my_pets)

print(uppered_pets)
print(my_pets)

circle_areas = [3.56773, 5.57668, 4.00914, 56.24241,
9.01344, 32.00013]

result = list(map(round, circle_areas, range(1,7)))

print(result)

def ff(n):
    return n*2

MyList = [0,1,2,3,4,10,13,22,25,100,120]

print("squared List:", list(map(ff, MyList)) )

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = (1,2,3,4,5, 10)
my_minus_numbers = [-1,-2,-3,-4,-5]

results = list(zip(my_strings, my_numbers, my_minus_numbers))
print(results)


from functools import reduce
x= reduce(lambda a,b: a+b,[23,21,45,98])
print(x)


print("End of Practicing and start of Exercises")
"""



#Q1

o = lambda x=1, y=2, z=3 : x + y + z

#print(o()) >>> 6
#print(o(10)) >>> 15
#print(o(10, 20)) >>> 33


#Q2

lis = [1, 2, 3, 4, 5, 6]
from functools import reduce

multiplication = reduce(lambda x, y: x * y, lis)
print(multiplication)
#Q3

multi = (lambda x, y: x * y) (2, 4)
print(multi)
#Q4
lis = range(-5, 5)
negatives = list(filter(lambda x: x < 0, lis))
print(negatives)
#Q5

x = lambda a, b, c: a + b + c
print(x(5, 6, 2))
#>>> 13


#Q6

x = ("H", "A", "Y")
y = ("h", "a", "y")
z = (1, 2, 3)
result = list(zip(x, y, z))
print(result)

#>>> [('H', 'h', 1), ('A', 'a', 2), ('Y', 'y', 3)]

#Q7

x = ("H", "A", "Y")
y = ("h", "a", "y")

result = dict(zip(x, y))
print(result)

#>>> {'H': 'h', 'A': 'a', 'Y': 'y'}

#Q8

def fun(var):
    letters = ['a', 'e', 'o', 'i', 'u']
    if (var in letters):
        return True
    else:
        return False

seq = ['g', 'j', 'e', 'j', 'k', 'o', 'p', 'r']

fill = list(filter(fun, seq))

print(fill)

#>>> ['e', 'o']

#Q9

v = list(map(int, input("Enter multi values: ").split()))

print("List: ", v)
#Q10

def func(a):
    return a * a
a = list(map(func, [1, 2, 4, 5]))

print(a)

#>>> [1, 4, 16, 25]

#Q11

def func(a, b):
    return a + b
a = list(map(func, [2, 4, 5], [1, 2, 3, 2, 4]))

print(a)

#>>> [3, 6, 8]

#Q12

result = list(map(lambda x: x + x, filter(lambda x: (x>=3), [1, 2, 3, 4])))

print(result)

#>>> [6, 8]

#Q13

result = list(filter(lambda x:(x>=3), map(lambda x: x + x, [1, 2, 3, 4])))

print(result)

#>>> [4, 6, 8]

#Q14

result = reduce(lambda x, y: x if x < y else y, [10, 24, 3, 7])

print(result)

#>>> 3

#Q15

numbers = [1, 2, 3]
letters = ['a', 'b', 'c']

result = list(zip(numbers, letters))
print(result)
#>>> [(1, 'a'), (2, 'b'), (3, 'c')]
