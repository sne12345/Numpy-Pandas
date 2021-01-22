#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[57]:


df = pd.read_csv('./PatientInfo.csv')
df


# In[136]:


df_part = df[["patient_id", "sex", "birth_year", "age", "province", "city", "infection_case", "contact_number"]]
df_part


# .

# # null값이 몇 개인지

# In[137]:


df_part.isnull().sum()


# # 1. null값이 있는 row 제거

# In[138]:


df_no_missing = df_part.dropna()
df_no_missing


# # 2. 모든 데이터가 비어있으면 해당 row 제거

# In[139]:


df_cleaned = df_part.dropna(how='all')
df_cleaned


# ### 데이터가 n개 이상 있지 않으면 드롭

# In[140]:


df_thresh = df_part.dropna(thresh=6)
df_thresh


# In[141]:


df_thresh.isnull().sum()


# # 3. null 자리에 대체값을 채우기

# ### 0값으로 대체

# In[142]:


df_part["city"].fillna(0, inplace=True)
#df_part["contact_number"].fillna(0, inplace=True)
df_part


# In[143]:


df_part.isnull().sum()


# ### 평균값, 최빈값으로 대체

# In[146]:


df_part["birth_year"].fillna(df["birth_year"].mean(), inplace=True)
df_part["contact_number"].fillna(df["contact_number"].mean(), inplace=True)


# In[147]:


df_part.isnull().sum()


# In[129]:


df_part


# ### groupby로 transform

# In[148]:


df_part.groupby("infection_case")["contact_number"].transform("mean")


# In[149]:


df_part["contact_number"].fillna(
    df_part.groupby("infection_case")["contact_number"].transform("mean"), inplace=True
)


# In[150]:


df_part.isnull().sum()


# ### null값이 없는 값 뽑아내기

# In[151]:


df_part[df_part['sex'].notnull() & df_part['age'].notnull()]


# ### One-hot-Encoding

# In[152]:


df_part.dtypes


# In[153]:


pd.get_dummies(df_part)


# In[ ]:




