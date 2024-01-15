a=[1,2,3,4,5,6,7,8,9]
b=[i*10 for i in a]
c=[i*100 for i in a if i%3 == 1]

print(b,'\n',c)