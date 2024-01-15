import time 
t = time.localtime(time.time()) 
localtime = time.asctime(t) 
str = "current time:" + time.asctime(t) 
print(str)