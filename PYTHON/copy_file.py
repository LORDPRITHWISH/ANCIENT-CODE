import shutil
import tqdm 

path1='H:\\test\\bob\\dad.txt'
path2='H:\\test\\mam\\well.txt'
for _ in tqdm.tqdm(range(100000000)) :
    with open(path1,'a') as fi :
        fi.write("dol ")


# shutil.copy(path1,path2)


print('done')
