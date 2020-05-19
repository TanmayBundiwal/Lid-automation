#!/usr/bin/env python
# coding: utf-8

# In[6]:


import wmi
from shutil import copyfile


# In[2]:


obj = wmi.WMI().Win32_PnPEntity(ConfigManagerErrorCode=0)


# In[3]:


displays = [x for x in obj if 'DISPLAY' in str(x)]


# In[ ]:


for item in displays:
    print (item)


# In[4]:


without_monitor_count = len(displays)


# In[ ]:


File = open("config_data.txt",'w')


# In[ ]:


File.write(str(without_monitor_count))


# In[ ]:


File.close()


# In[ ]:


copyfile('lid.cmd','C:\Windows\System32\lid.cmd')

