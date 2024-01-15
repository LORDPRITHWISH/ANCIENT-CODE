def deco(a) :
    print('lol')
    def innert(*args,**kwargs) :
        return a(*args,**kwargs)
    return innert

@deco
def caller(x,y) :
    print('LOL',x+y)

print(caller(10,20))
