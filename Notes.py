# import numpy as np

# print("Hello World!")

# print(10*"K T")


# mil =[1,2,3,4,5]        #lists
# print(len(mil))

# mak =(1,2,3,4,5)        #tuples
# print(len(mak))

# sak = {1,2,3,4,5,5,6,3}     #Set
# print(sak)

# keys1 = ["aak", "pak", "tamal"] #dictionaries
# values1 = [1,5,8]
# data = dict(zip(keys1,values1))
# print(data)
# data["moni"] = 4   #adding values
# del data["moni"]   #deleting values
# prog ={'deam':4}   #general initialization

# a = 10
# print(id(a))       #finding the address

# l = list(range(0,10))      #Initiating a list using range() datatype
# m = list(range(2,10,2))   #(start,upto,interval)

# nums =[2,13,14,12,19]

# for num in nums:            #for-else lOOP 
#     if num % 5 == 0 :
#         print(num)
#         break
# else:
#     print("not found")


# import numpy as np              #numpy intro

# # val = np.array([12,12,133,212])
# # print(val)

# arr1 = np.array([1,2,3,4,5])
# arr2 = np.array([5,6,1,2,3]) 
# #print(arr1+arr2)

# m = np.matrix('1 2 3; 1 4 5; 2 3 4')
# print(m)
# print(np.diagonal(m))


# def person(name, **data):
#     print(name)
#     for i,j in data.items():        #To retrieve the info from data
#         print(i,j)              


# import sys

# print(sys.getrecursionlimit())

'''
nums = [3,4,5,6,7,9]            #filter() func usage
#evens = list(filter(lambda n: n%2==0, nums))

evens = list(map(lambda n:2*n, nums))   #using map()
print(evens)

import functools as ft          #using reduce()
sum = ft.reduce(lambda x,y:x+y , evens) 
print(sum)

'''


'''
#Decorators example:

def div(a,b):
    print(a/b)
                #To manipulate the functionality of def() such that the numerator is always greater than the denominator no matter how the args are passed
def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner 

div = smart_div(div) 
div(2,4)     



# def square(x):                  #Here is our function which gives out the squares
#     return x*x

# def my_map(func,lst):           #Here is our map func which applies square func() to all individual elements of a given list 
#     sqrs = []
#     for i in lst:
#         sqrs.append(func(i))
#     return sqrs

# f = square
# print(f)

# #creating my_map() function
# lst = [1,2,3,4,5]
# print(my_map(square,lst))



#-----------------------------------------------------------------------------------------------------------------------------------


# def outer_function(func):
#     def inner_func():
#         print('inner execcuted before: {}'.format(func.__name__))
#         return func()
#     return inner_func

# def display():
#     print("Hello, this is DISPLAY")


# f = outer_function(display)
# f()
#------------------------------- A better way to using decorators------------------------------
# def outer_function(func):
#     def inner_func():
#         print('inner execcuted before: {}'.format(func.__name__))
#         return func()
#     return inner_func

# @outer_function                         #This line is similar to : f = outer_function(display)
# def display():
#     print("Hello, this is DISPLAY")


# display()                               #This has enabled us to use our original function directly without a variable which is just awesome    


'''



'''
#Classes and object
--------------------------
class Computer:
    generation = "Gen:5"      #Class variable or static varible

    def __init__(self, cpu, ram):  
        self.cpu = cpu
        self.ram = ram

    def config(self):           #it is mandatory to pass self
        print("Hello there!")
        print("Confg is ",self.cpu,self.ram)

    def compare(self,other_obj):                # method to compare the features of two objects
        return True if self.cpu == other_obj.cpu else False

    @classmethod                                # Class method
    def design_info(cls):
        return print(cls.generation)

    @staticmethod    
    def info():
        return print("This is a computer factory")

com = Computer('i6',16)     #here 3 args are being passed of which the object itsef is one of them
boom = Computer('i5',8)

#com.config()
Computer.config(com)    # we can use the method in both ways

if(com.compare(boom)):          
    print("They are same!")

Computer.design_info()
Computer.info()
'''


                            #Nested Classes
'''
class Student:
    def __init__(self):
        self.name = "Kiran"
        self.lap = self.Laptop()            #using the whole laptop class as an object itself 

    class Laptop:
        def __init__(self):
            self.brand = "HP"
            self.cpu = "Intel"

stu = Student()
lap2 = Student.Laptop()                     #  Another way to declare the object of a subclass
print(stu.name)
print(stu.lap.brand)
print(lap2.brand)
'''

                                #Inheritance
'''
class A:
    def __init__(self):
        print("Reporting from A")
        
    def feature1(self):
        return "feature1 from A working!"

class B(A):
    def __init__(self):
        super().__init__()
        print("Reporting from B")
        
    def feature2(self):
        return  "feature2 from B working!"

class C(B,A):                               # multiple inheritance - C(A,B) isn't possible for method resolution because the fields in A can be manipulated by B. So its difficult to decide who the boss is if we say A is the boss
    def __init__(self):
        super().__init__()
        print("Reporting from C")
        
    def feature3(self):
        return  "feature3 from C working!"

#a = A()
#b = B()
# c = C()
#print(c.feature1())
'''

                                #Polymorphism

#DuckTyping:
'''
class Laptop:
    def code(self, ide):
        ide.execute()

class VsCode:
    def execute(self):
        print("VsCode:")
        print("Editing")
        print("Awesome plugins and fonts")

class Notepad:
    def execute(self):
        print("Notepad")
        print("Editing")

ide = VsCode()
lap1 = Laptop()
lap1.code(ide)
ide = Notepad()
lap1.code(ide)          #Here type(ide) doesnt matter unless the execute() function is present in both its implementations

'''

'''
#Operator overloading

class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self,other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        return Student(m1,m2)

    def __gt__(self, other):               #overloading the greaterthan operator
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2

        return True if r1>r2 else False 

    def __str__(self):                      #This is generally a method called for displaying when we use print()
        return self.m1, self.m2

s1 = Student(5,6)     
s2 = Student(12,13) 

#print(s1>s2)
#print((s1+s2).m1,(s1+s2).m2)

print(s1.__str__())                         #__str__() generally returns module_name.Classname.Address. Here we are overriding its functionality
'''

#Abstract methods
'''
from abc import ABC, abstractmethod

class Computer(ABC):                    #inheriting ABC
    @abstractmethod                     #using decorator
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print("Hi, here I'm")

com1 = Laptop()
com1.process()
'''


#Iteration
'''
nums = [1,2,3,4,5]
lst = iter(nums)

#for i in range(len(nums)):
#    print(lst.__next__())                   #automatically saves the state without the help of index

class Topten:                               #creating my own iterator    
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
        else:
            raise StopIteration

        return val    

values = Topten()
for i in values:
    print(i)

#Generator
def topTen():
    yield 5             #instead of return, using yield to covert the function into a generator
                        #yield returns a generator object
    
print(topTen().__next__())


def topTen2():
    n=1
    while n<=10:
        yield n*n
        n+=1

val2 = topTen2()
for i in val2:
    print(i)

'''

'''
#Eception handling
a=1
b=0
try:
    print(a/b)
except Exception as e:
    print("Hey, you have an error:",e)

finally:
    print("Closing all resources")

'''


'''
#Threads
from threading import Thread
import time

class Hello(Thread):
    def run(self):
        for i in range(5):
            print(i,"Hello")
            time.sleep(1)               # in python, sleep() takes arguments in seconds unlike in Java

class Hi(Thread):
    def run(self):
        for i in range(5):
            print(i,"Hi")
            time.sleep(1)
t1 = Hello()
t2 = Hi() 

t1.start()
time.sleep(0.5) #to avoid collisions
t2.start()

t1.join()
t2.join()                           # making the main thread wait for the two threads to join the branch

print("End")

'''



#FileHandling
r'''
f = open('MyData','r')          #opening file in write mode      

f1=open('MyData2','w')          #opening file in read mode
f1.write("Something")

f1=open('MyData2','a')          #opening file in append mode
f1.write("Something")

for data in f:
    f1.write(data)

f.close()
f1.close()

f3 = open(r"C:\Users\ktaak\Desktop\Untitled.png",'rb')
f1=open('MyData2','wb')
for data in f3:
    f1.write(data)

f3.close()
f1.close() 

'''

#Database connection
'''
#---------------first
#               pip install mysql-connector
import mysql.connector
try:
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="SeekAndYehShallFind#2020")

    print(mydb)
    cus = mydb.cursor()
    cus.execute("show databases")

    for i in cus:
        print(i)
except :
    print("Exception!")
    
finally:
    cus.close()

'''        