import os 
li=os.listdir("recognition\\taken\\")
print(*li,end="\n",sep="\n")
dirna="recognition\\taken"
dirna=os.path.join(dirna,"apple")
print(dirna)
dirna=os.path.join(dirna,"banana")
print(dirna)