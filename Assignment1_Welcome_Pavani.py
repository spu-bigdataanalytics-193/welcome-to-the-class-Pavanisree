#!/usr/bin/env python
# coding: utf-8

# In[4]:


class Name:
    def __init__(self, LastName, FirstName):
        self.LastName=LastName
        self.FirstName=FirstName
    def assign(self):
        return ("Hello, my name is {} {}".format(self.FirstName, self.LastName))


# In[5]:


assignment=Name("Pavanisree", "Relangi")


# In[6]:


assignment.assign()


# In[ ]:




