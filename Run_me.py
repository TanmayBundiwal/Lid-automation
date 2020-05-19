#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tkinter as tk
import os

root= tk.Tk() 
   
canvas1 = tk.Canvas(root, width = 350, height = 250) 
canvas1.pack()

def start_off(): 
       os.system('"C:\Windows\System32\lid.cmd off"')

def start_on(): 
       os.system('"C:\Windows\System32\lid.cmd on"')

button1 = tk.Button (root, text='Turn Screen off',command=start_off,bg='black',fg='white')
canvas1.create_window(170, 80, window=button1)

button2 = tk.Button (root, text='Do nothing',command=start_on,bg='black',fg='white')
canvas1.create_window(170, 180, window=button2)

root.mainloop()


# In[ ]:




