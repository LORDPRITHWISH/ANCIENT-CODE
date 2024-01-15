a=[1,2,3,4,5,6,7,8,9]
print(*a,sep=', ')


b=['RAM','DAM','PAM','CAM','LAM','BAM','MAM','NAM','ZAM']
c=list(zip(a,b))
print(*c)
d=zip(a,b)
print(d)