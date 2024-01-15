import pyttsx3
# e = pyttsx3.init()

# engine = pyttsx3.init()
# # volume = engine.getProperty('volume')
# # engine.setProperty('volume', volume-0.25)
# engine.say('hi what the hell is goind on ova here')
# # engine.runAndWait()

# # engine = pyttsx3.init()
# rate = e.getProperty('rate')
# print(rate)
# e.setProperty('rate', rate+150)
# e.setProperty('rate', 300)
# print(e.connect)

# rate = engine.getProperty('rate')

# print(rate)
# engine.say('hi what the hell is goind on ova here')
# engine.runAndWait()

# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# for voice in voices:
#    engine.setProperty('voice', voice.id)
#    engine.say('The quick brown fox jumped over the lazy dog.')
# engine.runAndWait()


# def onWord(name, location, length):
#    print ('word'), name, location, length
#    if location > 10:
#       engine.stop()
# engine = pyttsx3.init()
# engine.connect('started-word', onWord)
# engine.say('The quick brown fox jumped over the lazy dog.')
# engine.runAndWait()

# volume = e.getProperty('volume')
# e.say('hi what the hell is goind on ova here')
# print(e.getProperty('volume'))

# e.setProperty('volume', volume-0.25)
# print(e.getProperty('volume'))

# e.say('hi what the hell is goind on ova here')
# e.setProperty('volume', volume-0.25)
# print(e.getProperty('volume'))

# e.say('hi what the hell is goind on ova here')
# e.setProperty('volume', volume-0.25)
# print(e.getProperty('volume'))

# e.say('hi what the hell is goind on ova here')
# e.setProperty('volume', volume-0.25)
# print(e.getProperty('volume'))

# e.say('hi what the hell is goind on ova here')

# e.setProperty('volume', 1)
# e.say("or")
# print("or")
# volume = e.getProperty('volume')
# e.say('hi what the hell is goind on ova here')
# print(e.getProperty('volume'))

# e.setProperty('volume',1)
# print(e.getProperty('volume'))

# e.say('hi what the hell is goind on ova here')
# e.setProperty('volume',.8)
# print(e.getProperty('volume'))

# e.say('hi what the hell is goind on ova here')
# e.setProperty('volume', .6)
# print(e.getProperty('volume'))

# e.say('hi what the hell is goind on ova here')
# e.setProperty('volume', .4)
# print(e.getProperty('volume'))

# e.say('hi what the hell is goind on ova here')

# e.setProperty('volume', 1)
# e.say("or")
# print("or")

# volume = e.getProperty('volume')
# e.say('hi what the hell is goind on ova here')
# print(e.getProperty('volume'))
# volume-=.2
# e.setProperty('volume', volume)
# print(e.getProperty('volume'))
# volume-=.2

# e.say('hi what the hell is goind on ova here')
# e.setProperty('volume', volume)
# print(e.getProperty('volume'))
# volume-=.2

# e.say('hi what the hell is goind on ova here')
# e.setProperty('volume', volume)
# print(e.getProperty('volume'))
# volume-=.2

# e.say('hi what the hell is goind on ova here')
# e.setProperty('volume', volume)
# print(e.getProperty('volume'))
# volume-=.2

# e.say('hi what the hell is goind on ova here')

# e.runAndWait()
# def externalLoop():
#     engine.say('The quick brown fox jumped over the lazy dog.', 'fox')


# engine = pyttsx3.init()
# engine.say('The quick brown fox jumped over the lazy dog.', 'fox')
# engine.startLoop(True)
# # engine.iterate() must be called inside externalLoop()
# externalLoop()
# engine.endLoop()
# e.runAndWait()




# engine = pyttsx3.init()


# def onStart(name):
#    print ('starting', name)
   
# def onWord(name, location, length):
#    print ('word', name, location, length)
   
# def onEnd(name, completed):
#    print ('finishing', name, completed)
#    if name == 'fox':
#       engine.say('What a lazy dog!', 'dog')
#    elif name == 'dog':
#       engine.endLoop()
      
# engine = pyttsx3.init()
# engine.connect('started-utterance', onStart)
# engine.connect('started-word', onWord)
# engine.connect('finished-utterance', onEnd)
# engine.say('The quick brown fox jumped over the lazy dog.', 'fox')
# engine.startLoop()




# def goa(name):
#     print ('goa', name)
#     e.say("hell fire is upon us","kum")

# def go(name, completed):
#     print("go", name , completed)
#     if name == 'rum':
#         e.say("hi what is happning","dum")
#     elif name == 'dum':
#         e.endLoop()
        


# e=pyttsx3.init()
# print("hi")
# e.connect('started-utterance',goa)
# e.connect('finished-utterance',go)
# e.say("who is that","rum")
# e.startLoop()




# def onStart(name):
#    print ('starting', name)
#    engine.say('a human watched it happen','human')
   
# def onWord(name, location, length):
#    print ('word', name, location, length)
   
# def onEnd(name, completed):
#    print ('finishing', name, completed)
   
#    if name=='human':
#        engine.say('he was a bad human', 'hu')
#    elif name == 'fox':
#       engine.say('What a lazy dog!', 'dog')
#    elif name == 'dog':
#       engine.endLoop()
      
# engine = pyttsx3.init()
# engine.connect('started-utterance', onStart)
# engine.connect('started-word', onWord)
# engine.connect('finished-utterance', onEnd)
# engine.say('The quick brown fox jumped over the lazy dog.', 'fox')
# engine.startLoop()




e=pyttsx3.init()

# t=input("ENTER TEXT :\t")
# e.say(t)
e.say('hell no man, hell no')
e.say('good good go on')
# e.runAndWait()

e.startLoop()
e.say('hell no man, hell no')
e.say('good good go on')
# e.runAndWait()

e.endLoop()
# e.runAndWait()
