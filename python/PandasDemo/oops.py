#object is a real world entity, instance of class 
#class is a blueprint used to create objects having similar property or attributes.

class A:
    x=45
    def show(self):
        print("Hello")
#create  a object of class 
ob=A()
print(ob.x)
ob.y=50
print(ob.y)
ob.show()

#classname is known as namespace.  Attributes- VAriable in class
class B:
    x=5  #public
    _x=10   #protected
    __x=20   #private
ob=B()
print(ob.x)
print(ob._x)
#print(ob.__x)
print(ob._B__x)    #we can access any private instance by using Protected member.

class A:
    def show(self):
        print("Hello")
    def __put(self):
        print("Java")
ob=A()
ob.show()
ob._A__put()

class A:
    x="GITS"
    def show(self,name,age,mob):
        print(name,age,mob)
ob=A()
print(ob.x)
ob.show("Heena",35,676767)
print(ob.x)
ob.show("Alina",45,12345)

class A:
    def show(self,y):
        print("Hello")
ob=A()
ob.show("y")

#Static Method
class A:
    @staticmethod
    def show():
        print("Hello")
#A.show()  #only applicable when function is static.
ob=A()
ob.show()

#Constructor
class A:
    def __init__(self):       #__init__is used for creating constructor
        print("Hello")
    def __del__(self):        #__del__is used for creating destructor
        print("Python")
ob=A()

class A:
    def show(self):
        print("Hello")
class B(A):
    def put(self):
        print("Java")
class C(B):
    def get(self):
        print("Python")
ob=C()
ob.show()
ob.put()
ob.get()

#To achieve Function Overloading
class sumClass:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b==None or c==None:
            print("Provide more numbers")
        else:
            print("First method:",a+b+c)

obj=sumClass()
obj.sum(19,8,77)#104
obj.sum(18)#Provide more numbers

from abc import ABCMeta,abstractmethod
class A:
    @abstractmethod
    def show(self):
        pass
class B(A):
    def show(self):
        print("Hello")
ob=B()
ob.show()

#re=Regular Expressions
import re
result=re.match(r'AV',"AV Analytics Vidhyaa AV")
print(result.group())

import re
result=re.search(r'AV',"AV Analytics Vidhyaa AV")
print(result.group())

import re
result=re.findall(r'AV',"AV Analytics Vidhyaa AV")
print(result)

import re 
result=re.split(r'y','Analytics')
print(result)


from itertools import permutations
print(list(permutations([3,"Python"],2)))


from itertools import combinations
print(list(combinations(['B',3],2)))
print()

from itertools import combinations_with_replacement
print(list(combinations_with_replacement("XY",3)))
print()

#Terminating Iterator
import itertools
import operator
#initializing list 1
list1=[1,4,5,7,9,11]
print(list(itertools.accumulate(list1)))
print(list(itertools.accumulate(list1,operator.mul)))


import itertools
#declaring list1
list1=[1,2,3,4]
#declaring list2
list2=[1,5,6,8]
#declaring list3
list3=[9,10,11,12]

print(list(itertools.chain(list1,list2,list3)))


import itertools
list1=[2,4,5,7,8]
print(list(itertools.dropwhile(lambda x:x%2==0,list1)))

import itertools
list1=[12,14,15,27,28]
print(list(itertools.filterfalse(lambda x:x%2==0,list1)))

import itertools
list1=[12,34,65,73,80,19,20]
print(list(itertools.islice(list1,2,8,2)))

