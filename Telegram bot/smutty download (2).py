import pyautogui as gui
import threading

DOWN=True
RUN=True
def work() :
    global DOWN
    try :

        pos=gui.locateOnScreen("Telegram bot\\save as.png",confidence=.7)
        print(list(pos))
        if DOWN :
            gui.moveTo(pos[0:2])
            gui.moveRel(30,15)
            gui.click()
            gui.sleep(1)
            gui.press('enter')
            # allign()
            print('in')
            DOWN=False
            gui.vscroll(-500)
        else :
             gui.press('esc')
    except Exception as e :
        gui.press('esc')
        DOWN=True
        print('well ', e)
        pass

def down() :
    gui.vscroll(-150)
    gui.rightClick(550,400)
    gui.sleep(.3)
    work()
    # gui.scroll(300)

def teleopen():
    pos=gui.locateOnScreen("Telegram bot\\telegram_logo.png",confidence=0.9)
    # gui.moveTo(650,750)
    gui.moveTo(pos[0:2])
    gui.moveRel(20,20)
    gui.click()
    gui.sleep(1)
    allign()

def allign() :
    gui.moveTo(550,400)
    
def exiting() :
    global RUN
    while True :
        x=gui.position()[0]
        if x == 0 :
            RUN=False
            
            break
        
        gui.sleep(1)
    home()
    exit(100)

def home() :
    pos=gui.locateOnScreen("whatsapp\\vs code.png",confidence=0.9)
    # gui.moveTo(600,750)
    gui.moveTo(pos[0:2])
    gui.moveRel(30,30)
    gui.sleep(.5)
    gui.click() 
    
threading.Thread(target=exiting,daemon=True).start()

    
teleopen()
while RUN :
    down()
    gui.sleep(.1)

























































