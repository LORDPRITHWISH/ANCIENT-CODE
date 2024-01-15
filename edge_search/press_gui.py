import pyautogui as gui
# gui.press('/')
# print("//")

pos=gui.locateOnScreen("edge_search\\edge.png",confidence=0.9)
# gui.moveTo(600,750)
gui.moveTo(pos[0:2])
gui.moveRel(20,20)
gui.sleep(.5)
gui.click() 


gui.moveTo(20,400)
gui.click() 


