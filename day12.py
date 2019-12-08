#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 09:45:07 2019

@author: owner
"""

from tkinter import *

root = Tk()


def ohh():
    print('Hello from here..')
    
    
def addEm():
    print('Hello from here..')
    new = Toplevel(root)
    Label(new, text='Name').grid()
    Label(new, text='Id').grid()
    Label(new, text='Name').grid()
    Label(new, text='Name').grid()

    

men = Menu(root)
root.config(menu=men)

file = Menu(men, tearoff=0)
file.add_command(label='Report', command=ohh)
file.add_separator()
file.add_command(label='Exit', command=root.destroy)

em = Menu(men, tearoff=0)
em.add_command(label='Add', command=addEm)
em.add_command(label='View', command=ohh)
em.add_command(label='Delete', command=root.destroy)

st = Menu(men, tearoff=0)
st.add_command(label='Add', command=ohh)
st.add_command(label='View', command=ohh)
st.add_command(label='Delete', command=root.destroy)

hel = Menu(men, tearoff=0)
hel.add_command(label='About', command=ohh)



men.add_cascade(label='File', menu=file)
men.add_cascade(label='Employees', menu=em)
men.add_cascade(label='Students', menu=st)
men.add_cascade(label='Help', menu=hel)


root.mainloop()












