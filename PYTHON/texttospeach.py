from tkinter import *
import pyttsx3
e=pyttsx3.init()
def say(x):
    e.say(x)
    e.runAndWait()

w=Tk()
