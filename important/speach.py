import pyttsx3 as tts

en=tts.init()
# en.say('lol')
with open('C:\\Users\\PRITHWISH\\Desktop\\tale.txt',"r") as txt :
    speach=txt.read()
    en.save_to_file(speach,'speach.mp3')
#     en.runAndWait()
# en.endLoop()
