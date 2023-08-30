#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# In[2]:


import pandas as pd


# In[3]:


def create_dataset(json_url):
    
    response = requests.get(json_url)
    
    if response.status_code == 200:
        
        json_data = response.json()
        
        df = pd.DataFrame(json_data)
        
        newDF = df.loc[:,"results"]
        
        finalDict = dict()
        
        for indx, value in newDF.items():
            first_value = next(iter(value.values())) 
            finalDict[indx] = first_value[0], first_value

        print(finalDict)
    
    else:
        print("Failed to retrieve data from the JSON URL")
    


# In[4]:


json_url = "https://pokeapi.co/api/v2/pokemon/?offset=0&limit=20"
create_dataset(json_url)


# In[ ]:




