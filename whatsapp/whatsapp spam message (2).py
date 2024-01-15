# import time as ti
import pyautogui as gui
# ti.sleep(2)
# gui.moveTo(650,750)
# gui.click()
# gui.moveTo(600,680)

   
def whatslocate():
    pos=gui.locateOnScreen("whatsapp\\whatsapp logo.png",confidence=0.9)
    # gui.moveTo(650,750)
    gui.moveTo(pos[0:2])
    gui.moveRel(20,20)
    gui.click()

def home() :
    pos=gui.locateOnScreen("whatsapp\\vs code.png",confidence=0.9)
    # gui.moveTo(600,750)
    gui.moveTo(pos[0:2])
    gui.moveRel(20,20)
    gui.sleep(.5)
    gui.click() 

whatslocate()

gui.sleep(1)
for _ in range(500) :
    gui.write("IT IS A MESSAGE FROM NO ONE")
    gui.press('enter')
    gui.sleep(.1)

home()
# gui.moveTo(600,750)
# gui.click()

















