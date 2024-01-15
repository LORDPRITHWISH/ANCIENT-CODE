import pyautogui as gui
import random
import time

colo="edge_search\\vs code.png"
edg="edge_search\\edge.png"
mark="edge_search\\mark.png"


def home() :
    pos=gui.locateOnScreen(colo,confidence=0.9)
    # gui.moveTo(600,750)
    gui.moveTo(pos[0:2])
    gui.moveRel(20,20)
    gui.sleep(.5)
    gui.click() 


def ready() :
    pos=gui.locateOnScreen(edg,confidence=0.9)
    # gui.moveTo(600,750)
    gui.moveTo(pos[0:2])
    gui.moveRel(20,20)
    gui.sleep(.5)
    gui.click() 
    gui.sleep(1)
    
def clear():
    gui.moveTo(20,400)
    gui.click() 

    
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
    print("got it")
    time.sleep(2)



ready()
search()
clear()

for _ in range(20):
    while 1:
        pos=gui.locateOnScreen(mark,confidence=0.9)
        
        if pos:
            search()
            break
        else:
            # print("yo")
            time.sleep(0.1)
home()