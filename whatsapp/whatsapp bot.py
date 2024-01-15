import pyautogui as gui
import pyperclip as pc
import threading
import AI_CHAT_BOT as reb

RUN=True

def new_message() :
    try :
        pos=gui.locateOnScreen("whatsapp\\green dot.png",confidence=0.8)
        # if pos :
            
        print(pos[0:2])
        gui.moveTo(pos[0:2])
        gui.moveRel(-100,0)
        gui.click()
        gui.sleep(1)
        read()
        writefind()
    except Exception as e :
        print(e)
            
def samechek() :
    read()
    try :
        gui.sleep(1)
        pos=gui.locateOnScreen("whatsapp\\cross.png",confidence=0.7)
        print(pos[0:2])
        gui.moveTo(pos[0:2])
        gui.moveRel(20,10)
        gui.click()
        # gui.sleep(1)
        readpos()
    except Exception as e :
        if copinp:
            # print('message found')
            writefind()
        else :
            print("may be immage")
    
def readpos() :
    try :
        pos=gui.locateOnScreen("whatsapp\\paper clip.png",confidence=0.9)
        print(pos[0:2])
        gui.moveTo(pos[0:2])
        gui.moveRel(-25,-55)
    except Exception as e :
        pass
        # print("readpos ",e)

def read() :
    readpos()
    copy()
    # gui.click()
    gui.sleep(.5)
    
def copy():
    global copinp
    gui.tripleClick()
    gui.keyDown("ctrl")
    gui.press("c")
    gui.keyUp("ctrl")
    copinp=pc.paste()
    # print(copinp)
    

def writefind() :
    try :
        pos=gui.locateOnScreen("whatsapp\\paper clip.png",confidence=0.8)
        print(pos[0:2])
        gui.moveTo(pos[0:2])
        gui.moveRel(100,10)
        gui.click()
        rep=reb.getresponce(copinp)
        # write("good")
        write(rep)
        # RUN=False
        gui.sleep(.5)
    except Exception as e :
        pass
        # print("writefind error ",e)
    
    
def write(x) :
    gui.write(x)
    gui.press('enter')
    gui.sleep(.1)
    
    
def whatslocate():
    pos=gui.locateOnScreen("whatsapp\\whatsapp logo.png",confidence=0.9)
    # gui.moveTo(650,750)
    gui.moveTo(pos[0:2])
    gui.moveRel(20,20)
    gui.click()
    
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
    gui.moveRel(20,20)
    gui.sleep(.5)
    gui.click() 

threading.Thread(target=exiting,daemon=True).start()
gui.sleep(1)
whatslocate()
while RUN :
    samechek()
    
    new_message()
    # samechek()
    
    # read()
    # writefind()
    gui.sleep(5)
    # c=gui.displayMousePosition()




