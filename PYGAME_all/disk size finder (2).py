import os
import shutil
import string

# x=string.ascii_uppercase
# print(x)
# a=shutil.disk_usage('H:')
# b=list(a)[0]
# print(a)
# print(b/2**30)
# print((os.path.getsize('H:\\test\\DARKNIGHT-0\\LORD\\PRITHWISH 0.txt')))
# print((os.path.getsize('H:\\test\\DARKNIGHT-3\\LORD\\PRITHWISH 0.txt')/2**10))
# way='H:\\test\\DARKNIGHT-0\\sector\\LORD\\PRITHWISH.txt'
# print(os.stat(way).st_size /2**10)
# print((os.path.getsize(way)/2**10))

# path1='H:\\test\\dad.txt'


# a=shutil.disk_usage('H:')[2]
# b1=list(a)[2]
# print(a)
# print(b1/2**30)

# with open(path1,'a') as fi :
#     fi.write("dol "*100000000)
        
# a=shutil.disk_usage('H:')
# b2=list(a)[2]
# print(b2/2**30)

# print((b2-b1)/2**30)


# path = 'H:\\test\\DAYNIGHT\\boy\\reborn'

# os.mkdir(path)

ini=list(string.ascii_uppercase)
ini.remove('C')
disks=[]
for i in ini :
    
    try :
        b=shutil.disk_usage(f'{i}:')
        # print(b)
        disks.append((i,(b[0]//2**30,b[1]//2**30,b[2]//2**30)))
    except FileNotFoundError : pass
    
print(disks)
        
            