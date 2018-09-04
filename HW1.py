
# coding: utf-8

# In[93]:


import pandas as pd
df= pd.read_csv('OriginalData.csv')
df1=pd.melt(df, id_vars=["State"], var_name='year')
cols1=list(df1.year)
cols1 = [str(x)[:4] for x in cols1]
cols2=list(df1.year)
cols2=[str(x)[5:len(cols2)] for x in cols2]
df1.year=cols1
cols3=list(df1.value.iloc[765:1530])
df1=df1.iloc[:765]
df1['Marriage rate']=cols3
df1['Marriage rate']=df1['Marriage rate'].apply( lambda x : str(x) + '%')
df1.rename(columns= {'value':'Divorce rate'}, inplace=True)
df1['Divorce rate']=df1['Divorce rate'].apply( lambda x : str(x) + '%')
df1.to_csv('outputdata.csv')
