import pyautogui as gui
import random

tags=["caption"]

def teleopen():
    pos=gui.locateOnScreen("Telegram bot\\telegram_logo.png",confidence=0.9)
    # gui.moveTo(650,750)
    gui.moveTo(pos[0:2])
    gui.moveRel(20,20)
    gui.click()
    
def run() :
    for _ in range(10) :
        gui.write(random.choice(tags))
        gui.press('enter')
        gui.sleep(.1)
    
def home() :
    pos=gui.locateOnScreen("whatsapp\\vs code.png",confidence=0.9)
    # gui.moveTo(600,750)
    gui.moveTo(pos[0:2])
    gui.moveRel(20,20)
    gui.sleep(.5)
    gui.click()