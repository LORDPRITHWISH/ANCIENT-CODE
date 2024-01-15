def fibo(x):
    if x==0 or x==1:
        return x
    return (fibo(x-2)+fibo(x-1))

print(fibo(50))

