# print('hi')
# a=10
# print(a)
# print(-a)
# a=170
# k=a%90
# print(k)
# k=[]
# for i in range (10):
#         for j in range (5):
#             k.append([i,j])
# print(k)
# x=['aa','zz','abc']
# y=max(x)
# z=y+x[1]

# x=0

# match x :
#     case 0:
#         print('zero')
#     case 1:
#         print('one')
#     case 2:
#         print('two')
#     case 3:
#         print('three')
#     case default :
#         print('no')
# from math import *
# print(pi)
# from time import *
# print('ko')
# sleep(1)
# print('ko')
# print() pi

# K=lambda: print('XPRITHWISH')
# K()
# x=range(100)
# ch=lambda y:y%2==0
# P= list(filter(ch,x))
# print(P)
# x=300
# # i=list(range(x,-1,-1))
# # print(i)
# c=0
# for i in range(x-1,-1,-1):
#         for j in range(i,-1,-1):
#             print(j)
#             # c+=1
#             # print(i,' ',j)
#         print()
# print('\n'*3,c)

# print(list(range(1,21)))
x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for i in range(len(x)-1) :
    print(x[i])
    print(x,i)
    # x.pop(-1)
    x.remove(x[i])
