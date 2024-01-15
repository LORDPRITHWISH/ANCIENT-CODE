def deco(a) :
    print('lol',a)
    
    if type(a)==int :
        a=a**2

    return a
# @deco
def caller(x) :
    print('LOL',x(5))

caller=deco(caller)

caller(deco)
