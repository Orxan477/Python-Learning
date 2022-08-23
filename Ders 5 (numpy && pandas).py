#region numpy
a=[1,2,3,4]
# print(a*3)


import numpy as np

b=np.array(a);
# print(b*3)
# print(b.mean()) #ortada duran

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
    'MI':[15,16,17,18,None],
    'Xiaomi':[655,8787,3354,5578,448]};

df=pd.DataFrame(dt,index=[3,85,97,41,22]);
# print(df)
# print(df.loc[22,'Apple'])
# print(df.iloc[3,0])
# print(df.isnull().sum())
# print(df)
# print(df.dropna(axis=1,how="all")) #butun sutun nulldusa onu sil
# print(df.fillna(99))
# print(df[df>=10])
df.insert(1,"HP",[None,None,None,None,None])
# print(df)
print(df.dropna(axis=1,how="all")) 
# print(df)
# df.drop("Samsung",axis=1,inplace=True)
# print(df)
# print(df.mean()) #ortalama
#endregion 