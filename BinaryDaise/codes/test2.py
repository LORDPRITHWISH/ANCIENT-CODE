import numpy as np
import cv2
# import pandas as pd
# import random as rn
# import math
# # pixels_per_bit=3

# frame=25*np.ones((10,15),dtype=np.uint8)
# # frame[:pixels_per_bit, :3] = 255 - frame[:pixels_per_bit, :3]

# # print(frame)

# # byte=4

# # for bit_position in range(7, -1, -1):
# #     # print(bit_position)
# #     bit = (byte >> bit_position)&1
# #     print(bit)

# i=j=0
# i+=1
# print(i,j)
# i=0
# j=30
# while j :
#     i+=1
#     j-=1
#     # if i>10 :
#     i%=10
#     print(i)
# print('\n'*5)
# i=0
# j=30
# while j :
#     i+=1
#     j-=1
#     if i>10 :
#         i%=10
#     print(i)

# x= np.uint8()
# for i in range(300):
#     print(i,np.uint8(i))

# lis=[1,5,5,3,5,7,1,6,9,8,5,2,1,3,4,5,7,6,2,1,4,8,9,6,3,2,1,4,5,7,8,9,5,4,6,4,5,4]
# lis=[]

# for _ in range(100):
#     lis.append(rn.randint(0,9))
    
# counted=dict(pd.Series(lis).value_counts())

# print(counted)
# print(list(map(counted.keys,counted.items)))
# bibi=list(map(lambda bi: [], counted))
# for i in counted:
#     print(f'{i}-> {counted.get(i)}')
# kfr=frame.copy()
# frame*=2
# print(frame)
# print(kfr)
# # frame.
# ze=[0]*10
# print(ze)
# frame = np.zero((10, 20), dtype=[0,0,0])
# print(frame)
# temp=[1]
# print(bool(temp))
# for i in range(0,100 , 8):
#     byte = 0
#     for j in range(8):
#         print(i + j)
# x=101
# y=((x//8)*8)-x
# print(x+y,'=',x,y)

# a='raananda'
# b='ramnanda'
# # print(a==b)
# di=list(zip(a,b))
# print(di)
# for i,j in di:
#     if i != j:
#         print(i,j)

# lis=[1]*144336
# x=len(lis)
# print(x)

# if x < 8 :
#     r=8-x
# else:
#     # r=(x//8)*8-x+8
#     r=(math.ceil(x/8)*8)-x
# for _ in range(r):
#     lis.append(0)
# print('\n'*3)
# print(len(lis))
# print(len(lis)/8)
# # print(lis)

# compare.compare()
# x=0
# x|= 2<<1
# print(type(x))

# binary_bytes = bytearray()
# for i in range(0, len(binary_data), 8):
#     byte = 0
#     for j in range(8):
#         byte |= (binary_data[i + j] << (7 - j))

# frame=25*np.ones((10,15),dtype=np.uint8)
# imj=cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
# print(imj)

# i=0
# while i<10 :
#     print(i+=1)
# lis1=[1,2,3,4,5,6,7,8,9]
# lis2=lis1
# lis1.append(10)
# lis1=[i*10+i for i in lis1]
# print(lis1)
# print(lis2)

binary_data=[1,1,0,1,1,1,0,0]

binary_bytes = bytearray()
for i in range(0, len(binary_data), 8):
    byte = 0
    for j in range(8):
        byte |= (binary_data[i + j] << (7 - j))
    binary_bytes.append(byte)
    
# for i in [65,236,66] :
#     binary_bytes.append(i)

binary_bytes.extend([25,75,225])


print( binary_bytes)

binary_bytes.clear()

binary_bytes.extend([25,75,225])


print( binary_bytes)