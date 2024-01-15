import random
import pyperclip
from tkinter import *

def creator(x):
    li=[]
    for _ in range(x):
        y=random.randint(100,1000000)
        li.append(y)
    return li

a=str(creator(10000))
# print(a)
pyperclip.copy(a)   

[618401]