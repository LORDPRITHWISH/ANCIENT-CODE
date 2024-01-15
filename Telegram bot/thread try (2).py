import sys
import trace
import threading
import time

def func():
    while True:
        # print('thread running')
        time.sleep(.1)

def trying():
    print('do')
    # time.sleep(.5)
    raise SystemExit()

    # print('iy')
    

a=threading.Thread(target=func,daemon=True)
a.start()
time.sleep(1)
print(a)
# b=threading.Thread(target=trying,daemon=True)
# b.start()
# raise SystemExit()
# print('\n'*10)
# a.trying()
a.join()
# b.join()
print('holo')

