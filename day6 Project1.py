#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 10:24:42 2019

@author: owner
"""

class Person(object):
    def __init__(self, name, add):
        self._Name = name
        self._Address = add
        
    def getName(self):
        return self._Name
    
    def setName(self, name):
        self._Name = name
        return self._Name
    
    def getAddress(self):
        return self._Address
    
    def setAddress(self, add):
        self._Address = add
        return self._Address
    
    def __del__(self):
        print("I have been deleted")
        
        
from functools import reduce
    
class Employee(Person):
    def __init__(self, num, name, address, salary, title, loans):
        self.Number = int(num)
#        self.__Name = str(name)
        super().__init__(name, address)
#        self.__Address = str(address)
        self.__Salary = float(salary)
        self.__JobTitle = str(title)
        self.__Loans = list(loans)
        
    def getSalary(self):
        return self.__Salary
    
    def setSalary(self, salary):
        self.__Salary = salary
        return self.__Salary
    
    def getJobTitle(self):
        return self.__JobTitle
    
    def setJobTitle(self, title):
        self.__JobTitle = title
        return self.__JobTitle
    
    def getTotal(self):
        if len(self.__Loans) == 0:
            return 0
        else:
            total = reduce(lambda x, y: x + y, self.__Loans)
            return total

    def getLoan(self):
        return self.__Loans
    
    def getMaxLoan(self):
        maxx = reduce(lambda a, b: a if a > b else b, self.__Loans)
        return maxx

    def getMinLoan(self):
        minn = reduce(lambda a, b: a if a < b else b, self.__Loans)
        return minn

    def setLoans(self, loans):
        self.__Loans = loans
        return self.__Lones
    def printInfo(self):
        print("Employee Number", self.Number, ":")
        print("Name :", self._Name)
        print("Address :", self._Address)
        print("Job Title :", self.__JobTitle)
        print("Salary :", self.__Salary)
        print("Loans :", self.__Loans)
        print("Total Loans :", self.getTotal())

    def __del__(self):
        print("I have been deleted")
        
        
        
class Student(Person):
    def __init__(self, num, name, address, subject, marks):
        self.Number = int(num)
        super().__init__(name, address)
        self.__Subject = str(subject)
        self.__Marks = dict(marks)
        
    def getSubject(self):
        return self.__Subject
    
    def setSubject(self, subject):
        self.__Subject = subject
        return self.__Subject
    
    def getMarks(self):
        return self.__Marks
    
    def setMarks(self, marks):
        self.__Marks = marks
        return self.__Marks
    
    def getAvg(self):
        if len(self.__Marks.values()) == 0:
            return 0
        else:
            summ = reduce(lambda x, y: x + y, self.__Marks.values())
            avg = summ/len(self.__Marks.values())
            return avg
    
    def getA(self):
        A = list(filter(lambda x: x >= 90, self.__Marks.values()))
        return A
    
    def printInfo(self):
        print("Student Number", self.Number, ":")
        print("Name :", self._Name)
        print("Address :", self._Address)
        print("Subject :", self.__Subject)
        print("Student's Average:", self.getAvg())
        
        
    def __del__(self):
        print("I have been deleted")
        
#
#Employee1=Employee(1000,"Ahmad Yazaan","Amman Jordan",500,"HR Consultant",[434,200,1020])       
#Employee2= Employee(2000,"Hala rana","Aqaba jordan", 750,"Manager",[150,3000,250])
#Employee3= Employee(3000,"Mariam ali","Mafraq jordan", 600,"HR s",[304,1000,250,300,500,235])
##Employee4= Employee(4000,"Yasmin mohameed","Karak jordan", 865,"Director",[])
#Student1=Student(20191000,"Khalid Ali","Irbid Jordan", "History",{"English":80,"Arabic":90,"Management":75,"Calculus":85, "OS":73,"Priogramming":91})
#Student2=Student(20182000,"Reem Hani","Zarqa Jordan", "Softwere Eng",{"English":80,"Arabic":90,"Management":75,"Calculus":85, "OS":73,"Priogramming":90})
#Student3=Student(20161001,"Nawras Abdallah","Amman Jordan", "Arts",{"English":83,"Arabic":92,"Art":90,"Management":75})
#Student4=Student(20172030,"Amal Raed","Tafelah Jordan", "Computer Eng",{"English":83,"Arabic":92,"Management":70,"Calculus":80, "OS":79,"Priogramming":91})
  
#print(Employee2.printInfo())    
#print(Student1.printInfo())        
       
#print(Student2.getA())        
        
#def employees(employee, *employee2):
#    
#     employee.printInfo()
#
#
#
#employees(Employee1, Employee3)  
#        
EmployeeList = []
EmployeeList.append(Employee1)
EmployeeList.append(Employee2)
EmployeeList.append(Employee3)
#EmployeeList.append(Employee4)
#print(len(EmployeeList))

StudentsList = []
StudentsList.append(Student1)
StudentsList.append(Student2)
StudentsList.append(Student3)
StudentsList.append(Student4)
#print(len(StudentsList)) 


#print(EmployeeList)
#




# Q 5 + 6:
#def printInfo(List):
#    for item in List:
#        print(item.printInfo())

#printInfo(EmployeeList)     
#printInfo(StudentsList)     

#print(Student1.getAvg())   
# Q7:
#def highest(listt):
#    x = reduce(lambda x, y: x if x.getAvg() > y.getAvg() else y, listt)
#    print(x.getAvg())   
#highest(StudentsList)    


# Q 8+9:

def maxx(listt):
    x = reduce(lambda x, y: x if x.getMaxLoan() > y.getMaxLoan() else y, listt)
    print(x.getMaxLoan()) 
    
maxx(EmployeeList)   

def minn(listt):
    x = reduce(lambda x, y: x if x.getMinLoan() < y.getMinLoan() else y, listt)
    print(x.getMinLoan()) 
    
minn(EmployeeList)   


#Q 11:

def LoanDict(listt):
    dictionery = {}
    for x in listt:
        dictionery[x.getName()] = x.getLoan()
    print(dictionery)

LoanDict(EmployeeList)
#print(hhh)
#Q 12:

#def minAndMax(listt):
#    dictionery = {}
#    print(list(listt))
#    for key in listt.values():
#        print(hhh)
#        maxx = reduce(lambda x, y: x if x > y else y, listt)
#        minn = reduce(lambda x, y: x if x < y else y, listt.values())
#        dictionery[key] = {"Max": maxx, "Min": minn}
#    print(dictionery)


#
#def hhhh(lll):
#    for k in lll:
#        print(k)



#hhhh(hhh)
#minAndMax(LoanDict(EmployeeList))    
    
def Dellete(listt):
#    del listt
    for x in listt:
        del x

Dellete(StudentsList)
   