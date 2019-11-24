# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#a,b = 1, 10
"""
a = int(input("insert the first num"))
b = int(input("insert the first num"))

if a > b:
    print("a > b")
elif a < b:
    print("a < b")
else:
    print("a = b")


max = a if (a > b) else b
print("Max = ",max)


if 'a' in ['c', 'b']:
    print (True)
else:
    print(False)
    

if a > b:
    print(a, b)
else:
    print(b, a)


name = input("insert your name")
age = int(input("insert your age"))

if age < 18:
    print("Under Age")
    schoolAvg = int(input("plz insert your school Avg. "))
    if schoolAvg >= 90:
        print("Excellent Avg. ")
    elif schoolAvg >= 50 and age < 90:
        print("Passed")
    else:
        print("Failed")
elif age >= 18:
    print("Adult")
    job = input("plz insert your job title..")
    print(name, "your age is: ", age, "and your job title is: ", job)
    

for a in range (3):
    print (a)
    


for a in range (4,17, 2):
  print (a) 
for items in ['omaima','haya','ahmad']:
  print (items) if items == 'ahmad' else print("hhh")
      #break
      



while True:
    a = input(">")
    if a == 'exit':
        break
    print(a) 
     
for i in range(11):
    print("*")

for i in range(21):
    print("*", end=" ")
    
#for count, i in range(9):
 #   print(*)

i = 1 
while i <= 8:
    print("*" * i)
    i += 1


i = 1 
while i <= 8:
    print(" " * (8 - i),"*" * i)
    i += 1

for i in range(9):
    for j in range(i):
        print("*", end="")
    print("*")


for i in range(9):
    for j in range(i):
        print("*", end="")
    print("*")

while True:
    try :
        a= float (input ("your num"))
        inverse = 1.0/a
    
    except ValueError:
        print("You should have given either an int or a float")
    except ZeroDivisionError:
        print("Infinity")
    finally:
        print("There may or may not have been an exception.")

#Q1:
num1 = int(input("insert the first num"))
num2 = int(input("insert the second num"))

if num1 > num2:
    max = num1
else:
    max = num2
print("max = ", max)

#Q2:
num = int(input("insert your num"))
for i in range(11):
    print(num," * ", i, " = ", num*i)
"""

#Q3
print("hhh\b ")
for i in range(5):
    for j in range(i):
        print("*",end="")   
    print("*")
for i in range(5, -1, -1):
    for j in range(i):
        print("*",end="")   
    print("*")  
"""

#Q4:

letters = ['x', 'y', 'z', 'a', 'b', 'c']
for i in letters:
    if i == 'a':
        continue
    elif i == 'c':
        break
    print(i)
>> x >> y >> z >> b

#Q5:

for x in range(12, 25, 3):
    print(x)
>> 12 >> 15 >> 18 >> 21 >> 24

#Q6:

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
>> 1 >> 2 >> 3


#Q7:

num = int(input("insert your num"))

for i in range(num):
    num += i
print(num)


#Q8:

num = int(input("insert your num"))

if num%2 == 0:
    print("your number is even")
else:
    print("your number is odd")

    print("your number is even")

"""
#Q9:

for i in range(9, 0, -1):
    for j in range(1, i):
        print(" ", j, end="")
    print(" ")
    
   
 #for j in range(i):
  #      print(" ", end="")
for i in range(1, 9, 1):
    for j in range(i, 1, -1):
        print(j, end="")
    print(1)

for i in range(9, 0, -1):
    for j in range(i, 1, -1):
        print(j, end="")
    print(1)



    
    
"""

#Q10:


while True:
    
    try:        
        num = input("insert your num")
        num = int(num)
        break
    except ValueError:
        print("Plz enter just numbers..")


#Q11:

try:
    a = 3
    if a < 4:
        b = a / (a - 3)
    print("Value of b = ", b)
except(ZeroDivisionError, NameError):
    print("\nError Occurred and Handled")
    print(NameError)

#>> Error Occurred and Handled


"""

