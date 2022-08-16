import numpy as np

a=np.arange(5);
# print(a.mean())
 
# c=np.arange(12).reshape(3,4)
# print(c)






import pandas as pd
# dt= {'Samsung':[0,1,2,3, None],
#     'Apple':[5,6,None,8,9]};
dt=pd.read_csv(r"C:\Users\Orxan477\Desktop\testing.csv")
print(pd.read_html(r"E:\Documents\Code Academy\FinallProject\Front\index.html"))
df=pd.DataFrame(dt)

# df.insert(0,"yeni",[2])
# df.iloc[0,0]="jssj"
# print(df)
# print(df.loc[4,'Samsung'])
# print(df.iloc[1,1])
# print(df.isnull().sum())

# df.dropna()
# df.dropna(axis=1)
# df.dropna(axis=1,how='all')
# df.fillna(96)

# df[df>10]

# df.insert(0,"yeni",[2,2,2,2,2])
# df.drop("Orxan",axis=1,inplace=True)
# print(df)
# print(df)
