def fibo(x):
    a=0
    b=1
    sum=0
    for _ in range(x):
        # print(a,end='  ')
        b,a=a+b,b
        
        # print(a)
    print("\nlast :  ",b)

fibo(3)    