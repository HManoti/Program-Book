x=[12,34,67,89,90] #to find the length of list
print(len(x))

x=[12,34,67,89,90] #append
x.append("Java")
print(x)

x=[12,34,67,89,90] #extend
y=["Java"]
x.extend(y)
print(x)

x=[12,34,67,89,90] #insert
x.insert(1,"Java")
print(x)

x=[12,34,67,89,90] #remove
x.pop(1)
print(x)

x=[12,34,67,89,90] 
x[2]="Java"
print(x)

x=[3,7,9,7]
y=[2,6,9]
sum=(x+y)

list=[1,5,8]
list.clear()
print(list)

#count function
list=[1,5,5,4,5,3]
print(list.count(5))

#sort function
list=[2,64,24,89]
list.sort(reverse=2)
print(list)

# copy Function
list=[1,4,3,6]
y=list.copy()
y.append("Java")
print(list)
print(y)

#sort on the basis of length of words
x=["ram","alina","owesh","hitiksha","divisha"]
x.sort(key=len)
print(x)


#zip function
x=["m","na","i","hi"]
y=["y","me","s","na"]
z=[i+j for i,j in zip(x,y)]
print(z)

x=[1,2,3,4]
y=[]
for i in x:
    y.append(i*2)
print(y)          

#list comprehension
x=[1,2,3,4]
y=[]
for i in range(20):
    if(i%2==0):
        print(i)
lis=[i for i in range(20) if i%2==0]
print(lis)

