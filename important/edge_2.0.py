import tkinter as tk
import threading as th
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

def looper():
        global STAT,txt
        if STAT :
            STAT =False
            txt = "||"
            win.update()
        for _ in range(30):
            time.sleep(3)
            search()
            if STAT :
                break
        STAT = True
        txt="SEARCH hoo"
        win.update()
        print("done")

def run():
    print('test')
    th.Thread(target=looper,daemon=True).start()




win=tk.Tk()

# win.geometry('100x100')
# Create a Button
btn = tk.Button(win, text = txt,font=('Arial Black',50,'bold'), bd = '5',command = lambda: run())
btn.pack(side = 'top')
win.mainloop()

JOUGTXLGNSW
HXOIVXZAYQMOIB
FNQIGENXCN
COHIYHEGIFLGXN
TYQWXOXT/OZSROVJMMPFHEVQOXIM
VLPMRBGLTZVBN
WCEBHZPEVHIN
QBFZRMXKMF
GXNUWHYPSWJICHRS
RWWVTCEWNNMYZRQAXCZ
KWUAMCDEFDMQYHA
VUFRGZKJZTWOXPWE
QTUPOGXNBCZPGLXLTXZ
NNGMHNWKKNH
YGXSGDEGUKDIQRFF
