#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pyfmi.common.io import ResultDymolaBinary

mat=ResultDymolaBinary(r'TestValues.mat')


# In[2]:


mat.name


# In[3]:


mat.description


# In[4]:


mat.dataInfo


# In[5]:


data=mat.get_variable_data('Coal').x
data


# In[6]:


mat.get_variable_data('Natural_Gas').t


# In[7]:


mat.get_variable_data('Natural_Gas').x


# In[8]:


mat.get_variable_data('Transportation').t


# In[9]:


mat.get_variable_data('Petroleum').x


# In[10]:


mat.get_variable_data('Transportation').x


# In[11]:


mat.get_variable_data('Nuclear').x


# In[12]:


mat.get_variable_data('Renewable').x


# In[13]:


mat.get_variable_data('Conversion_Losse').x


# In[14]:


mat.get_variable_data('Residential').x


# In[15]:


mat.get_variable_data('Commercial').x


# In[16]:


mat.get_variable_data('Industrial').x


# In[23]:


from  plotly.offline import plot
from plotly.graph_objs import *

trace1 = {
  "link": {
    "color": ["#262C46","#ff3344", "#ffbbcc", "#776647", "#446677", "#336677", "#448899", "#556677", "#337788", "#113366","#668899"],
    "value": [6157,6157,6157,6157,960,960,960,387,387,2383,2383,1240,1240,1240,-7942,-7942,-7942,-1418,-1266,-1017,-541], 
    "source": [0,0,0,0,1,1,1,2,2,3,3,9,9,4,4,4,8,8,8,7,7,7], 
    "target": [2,3,9,5,3,9,2,6,5,6,5,5,6,9,3,5,6,2,3,9,3,5]
  }, 
  "node": {
    "pad": 10, 
    "line": {
      "color": "Black", 
      "width": 0.5
    }, 
    "color": ["#262C46","#ff3344", "#ffbbcc", "#776647", "#446677", "#336677", "#448899", "#556677", "#337788", "#113366","#668899"], 
    "label": ["Coal", "Natural_Gas", "Petroleum", "Renewable", "Conversion_Loose", "Residential", "Commerical", "Industrial", "Transportion"], 
    "thickness": 30
  }, 
  "type": "sankey", 
  "domain": {
    "x": [0, 1], 
    "y": [0, 1]
  }, 
  "orientation": "h", 
  "valueformat": ".0f"
}
data = Data([trace1])

fig = Figure(data=data)
plot(fig)


# In[ ]:




