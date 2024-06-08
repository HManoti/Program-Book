#Common Errors in Exception Handling
#IOerror( Input Output error)
#Importerror
#Value error
#Keyboard intrupt error
#eof error (end of file)

#1 combination- try and except  2combination-one try and many except  3combination- try, except and finally
#4 combination- try, except, else and finally
#5- except , try   6 combination- try and finally

while(True):
    try:
        x=int(input("Enter a Number:"))
        break
    except ValueError:
        print ("Enter Valid Value:")

while(True):
    try:
        x=int(input("Enter a Number:"))
        break
    except ValueError as a:
        print (a)

import sys
try:
    f= open('myfile.txt')
    s= f.readline()
    i= int(s.strip())
except IOError:
    print("I/O error({0}):{1}")
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:")

#Division Error
try:
    x=5/0
    print(x)
except ZeroDivisionError as a:
    print(a)

try:
    x5/2
except ZeroDivisionError as a:
    print(a)
else:
    print(x)
finally:
    print("Python")

#Assert Statement( Assertion Error)- single line statement,  used to debug any statement
def divide(num1, num2):
    assert num2!=0,"Division cannot be zero"
    return num1/num2

a1= divide(12,2)
print(a1)

#Ignore Errors- keyword: pass
try:
    x=5/0
    print(x)
except:
    pass

