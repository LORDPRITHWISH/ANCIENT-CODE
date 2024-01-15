import re
import bot_responce_hub as bore
import random
  
def getresponce(mes) :
    w=re.split(r'\s+|[,;?!.-]\s*',mes.lower())
    # print(w)
    inp=[]
    for i in w :
        if i :
            inp.append(i)
    return getres(inp)

def probab(wl,ms,rw) :
    for i in rw :
        if i not in ms :
            return 0
    p=0
    for i in ms :
        if i in wl :
            p+=1
    return (p*100)//len(ms)

def unknown() :
    return random.choice(bore.unkown)

def getres(mess) :
    chances={}
    
    def res(responce,word_list,required_words=[]) :
        responce=random.choice(responce)
        chances[responce]=probab(word_list,mess,required_words)
    
    def exact(responce,word_list,state='') :
        # print(len(mess),mess)
        if state =='sw' :
            # print('ini in')
            if len(mess)==1 and mess[0] in word_list :
                print('well in')
                return responce
            else :
                return ''
        else :
            for i in word_list :
                if i not in mess :
                    return ''
            return responce

    for i in bore.exacters :
        an=exact(*i)
        if an :
            return (an)
    
    for i in bore.responces :
        res(*i)
        
    # print(chances)
    best=max(chances,key=chances.get)
    # print(best)
    return best if chances[best]>0 else unknown()
           

# getresponce("what are you doing ?")
print(getresponce("how are you"))