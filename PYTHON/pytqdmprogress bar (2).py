from tqdm import *
import time
s=0
# for i in trange(5) :
for i in tqdm(range(100000000)) :
    s+=i
    # time.sleep(.1)
print(s)