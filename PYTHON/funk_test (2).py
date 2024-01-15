def outer() :
    a=10
    print('outer :',a)
    def inner() :
        print('inner :',a)
    
outer()
# inner()