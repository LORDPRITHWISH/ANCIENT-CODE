s=0
c=1_000_000_000
# c=1_000_000_00

for  i in range(c) :
    s+=i
    if i%(c//100)==0 :
        print(i//(c//100))
print("\n\nTHE REASULT IS ", s)