#tupple is emutable(can't modify)

#enumerate function- returns index and value
x=("hello","Java","Python")
for i,v in enumerate(x):
    print(i,":",v)

#dictionary is a unordered collection of objects
#not use indexing, slicing and stepping. Its mutable.
x={}
print(type(x))  #key always unique pr value can be duplicate.

x={1:"Java",2:"pYTHON",3:"Hello",4:"Java"}
print(x[1])
print(len(x))
print(x.keys())
print(x.values())

#item return key and value
x={1:"Java",2:"pYTHON",3:"Hello",4:"Java"}
for k,v in x.items():
    print(k,":",v)

x={1:"Java", 2:"Python"}
print(x[1])
print(x.get(1))

x={'a':"Java", 'b':"Python"}
x['L']=list(range(5))
x['T']=tuple(sorted(range(9,16),reverse=True))
print(x.keys())
print(x.values())

x={'a':"Java", 'b':"Python"}
x['L']=list(range(5))
x['T']=tuple(sorted(range(9,16),reverse=True))
for k,v in x.items():
    print(k,":",v)

#update 
x={'a':"Java", 'b':"Python","c":"Hello"}
x.update({"d":"HTML"})
print(x)

#delete


a=int(input("Enter a Number:"))
f=1
for i in range(1,a+1):
    f=f*i
print("The factorial of the number is:",f)