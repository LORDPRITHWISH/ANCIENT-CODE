import tkinter as tk
import asyncio as ass
import pyautogui as gui
import random
import time

STAT = True
txt="SEARCH"
def text():
    st=""
    for _ in range(random.randint(10,20)) :
        st+=chr(random.randint(ord('A'),ord('Z')))
    print(st)
    return st

def search():
    gui.press('/')
    gui.press('backspace')
    gui.write(text())
    gui.press('enter')
    # print("got it")
    # time.sleep(2)

async def run():
    
    global STAT,txt
    if STAT :
        STAT =False
        txt = "||"
        win.update()
    for _ in range(30):
        await ass.sleep(3)
        search()
        if STAT :
            break
    STAT = True
    txt="SEARCH hoo"
    win.update()


    print('asynchronous programming')


win=tk.Tk()

# win.geometry('100x100')
# Create a Button
btn = tk.Button(win, text = txt,font=('Arial Black',50,'bold'), bd = '5',command = lambda: ass.run(run()))
btn.pack(side = 'top')
win.mainloop()

