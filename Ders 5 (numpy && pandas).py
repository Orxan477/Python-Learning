#region numpy
a=[1,2,3,4]
# print(a*3)

from tracemalloc import start
import numpy as np

b=np.array(a);
# print(b*3)
# print(b.mean())

c=np.arange(1,16).reshape(3,5)
# print(c)
c[1,1]=16
# print(c)

# print(np.abs(-151651));
#endregion

#region pandas
import pandas as pd
# print(pd.read_csv("C:\\Users\\Orxan477\\Desktop\\testing.csv"))
# print(pd.read_csv(r"C:\Users\Orxan477\Desktop\testing.csv"));
dt= {'Samsung':[0,1,2,3, None],
    'Apple':[5,6,None,8,9],
    'Huawei':[10,12,13,None,14],
    'MI':[15,16,17,18,None]};

df=pd.DataFrame(dt,index=[3,85,97,41,22]);
# print(df)
print(df.loc[3,'Samsung'])
#endregion 