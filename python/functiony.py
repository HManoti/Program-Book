def show():
    print("Hello")
    print("python")
show()

x=5
def show():
    y=10
    print(x)
def put():
    z=30
    print(x)
show()
put()

#positional argument
def show (x,y,z):
    print(x,y,z)
show (2,3,4)

#default argument
def show(x,y=5,z=10):
    print(x,y,z)
show(2,20,30)

def show(x=15,y=20,z=10):
    print(x,y,z)
show(2)

#keyword Argument
def show(x,y,z):
    print(x,y,z)
show(z=1, x=2,y=3)

#Arbitary argument
def show(*ar):     #list form
    for i in ar:
        print(i)
show(2)
show(34,56)
show(56,78,90)

def show(*ar):
    for i in ar:
        print(i)
show(1,2,3,4,5)

def show(**ar):    #dictionary form
    for k in ar.keys():
        print(k,":",ar[k])
show(a="Java",b="Hello")
show(d="python")
show(e="GITS",f="HTML")

def show(x,y):
    return x+y
print(show(4,5))

def show(x,y):
    z=x+y 
    return z
print(show(4,5))

#function inside a function
def show():
    print("Hello")
def put():
    print("python")
    show()
put()

#nested function
def show():
    print("Hello")
    def put():
        print("python")
show()

def show():
    print("Hello")
def put():
    print("Python")
def get():
    print("Java")

def Main():
    while(True):
        print("Enter your choice:\n1. Show\2. Put\n3.Get\n4. Exit")
        x=int(input("Enter your choice"))
        if(x==1):
            show()
        elif(x==2):
            put()
        elif(x==3):
            get()
        else:
            break
Main()
