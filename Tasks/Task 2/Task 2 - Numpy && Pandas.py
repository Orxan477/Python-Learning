#region Task 1
a= [9,4,12,35,22];
from cmath import nan
from operator import index
import numpy as np 
b=np.array(a);
# print(b);
# print(b*2);

c=np.arange(3,28).reshape(5,5);
# print(c);
# print(c.mean());
# c[3,4]=c.mean();
# print(c);
#endregion

#region Task 2
import pandas as pd
a=pd.read_csv(r"C:\Users\Orxan477\Desktop\Task2.csv");
print(a);
df=pd.DataFrame(a,index=[1,2,3,4,5]);
# print(df);
# print(df.loc[4,'Acer']);
# print(df.loc[5,'Apple']);
# print(df.iloc[3,4]);
# print(df.isnull());
# print(df.isnull().sum());

df.insert(3,"Samsung",[33,56,43,None,79]);
# print(df);
print(df.isnull());

df.dropna(axis=0)
# print(df);
# print(df.drop("Samsung",axis=1));
#endregion