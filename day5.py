#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 14:12:30 2019

@author: owner
"""
"""
class Person:

    def __init__(self, name):
        self.nameeee = name
    def whoami( self ):
        print("I am " + self.nameeee)
    def __del__(self):
        print ( 'I have been deleted')
        
        
#p1 = Person('tom')
#p1.whoami()
#print(p1.nameeee)

class Encapsulation:
    def __init__(self, a, b, c):
        self.Apublic = a
        self._Bprotected = b
        self.__Cprivate = c
    def getprivate(self):
        return self.__Cprivate
    def setPrivate(self, newName):
         self.__Cprivate = "Roaa"
#         return self.__Cprivate

x = Encapsulation(11,13,17)
print ( x.Apublic )
print ( x._Bprotected )
#print ( x.__Cprivate) #->>>> Error
print ( x.getprivate())
x.setPrivate("Haya")
print ( x.getprivate())


class A:
    def __init__(self):
        print("world")
        
class B(A):
    def __init__(self):
        print("hello")
        super().__init__()
#        A.__init__(self)
        
b1=B()

class Circle:
    def __init__(self, radius):
        self.__radius = radius
    def setRadius(self, radius):
        self.__radius = radius
    def getRadius(self):
        return self.__radius

    def __add__(self, another_circle):
        return Circle( self.__radius + Circle(another_circle))

c1 = Circle(4)
print(c1.getRadius())
c2 = Circle(5)
print(c2.getRadius())
c3 = c1 + 2
print(c3.getRadius())

class Car:
    def start(self):
        self.message = "Engine started"
        return self.message
car_a = Car()
print(car_a.message)

"""

class Employee(object):
    def __init__(self, num, name, add, salary, job_title):
        self.Number = num
        self.__Name = name
        self.__Address = add
        self.__Salary = salary
        self.__JobTitle = job_title
    def getName(self):
        return self.__Name
    def getAddress(self):
        return self.__Address
    def getSalary(self):
        return self.__Salary
    def getJobTitle(self):
        return self.__JobTitle
    def setAddress(self, add):
        self.__Address = add
        return self.__Address
    def print1(self):
        print("Employee", self.Number, "Information:")
        print("Employee Number : ", self.Number)
        print("Name : ", self.__Name)
        print("Address : ", self.__Address)
        print("Salary : ", self.__Salary)
        print("Job Title : ", self.__JobTitle )
    def print2(self):
        print("Employee", self.Number, "Information: Employee Number =", self.Number,  ", Name =", self.__Name, ", Address =", self.__Address, ", Salary =", self.__Salary, ", Job Title \" ", self.__JobTitle, "\" " )

    def __del__(self):
        print(self.__Name, " has been deleted")
        

Employee1 = Employee(1, "Mohd Khalid", "Amman,Jordan", 500, "Consultant")
print(Employee1.getName())
print(Employee1.setAddress("USA"))
print(Employee1.getAddress())
Employee1.print1()
del Employee1
Employee2 = Employee(2, "Haya", "Irbid,Jordan", 750, "Managerة")
print(Employee2.getName())
print(Employee2.getAddress())
Employee2.print2()
del Employee2
