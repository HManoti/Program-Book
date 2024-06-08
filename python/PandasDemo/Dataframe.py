import pandas as pd
x=[12,34,56,78,90]
#x=[[1,2,3],[4,5,6],[7,8,9]]
df=pd.DataFrame(x)
print(df)


import pandas as pd
#d={'ID':[12,34,56,78],'Name':['Heena','Alina','Hit','Rosy']}
#d={'ID':[12,34,56,78]}
d=[{'a':12,'b':34},{'a':100,'b':200,'c':300}]             #not a number-NaN
df=pd.DataFrame(d)
print(df)