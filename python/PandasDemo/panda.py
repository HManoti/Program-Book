import pandas as pd
x=[12,34,45.56,"python"]
se=pd.Series(x)
print(se)
print(type(se))


import pandas as pd
#x=[12,34,45,56,78,90]
se=pd.Series([12,34,56,78])
print(se)


import pandas as pd
#x=[12,34,45,56,78,90]
se=pd.Series([12,34,56,78],index=['a','b','c','d'],dtype=float)
print(se)


import pandas as pd
#x=[12,34,45,56,78,90]
se=pd.Series(0.5,index=[1,2,3,4])
print(se)


import pandas as pd
#x=[12,34,45,56,78,90]
se=pd.Series({'a':12,'b':34,'c':56})
print(se)

import pandas as pd
se=pd.Series([1,2,3,4,5,6,7,8,])
print(max(se))
print(min(se))
print(se[se>3])