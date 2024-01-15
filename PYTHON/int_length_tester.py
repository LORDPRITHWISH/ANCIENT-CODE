bit=4

a=2**bit-1

b=0
for i in range(bit):
    print(i,2**i)
    b+=2**i

print(f"\n\n\na= {a}\nb= {b}\nres= {a-b}")