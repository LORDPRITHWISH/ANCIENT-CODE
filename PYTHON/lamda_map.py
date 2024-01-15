a=list(range(10))
y=lambda a : a**2
# print(y(7))
c=list(map(y,a))
print(*c)
