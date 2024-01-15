biori=''
birec=''
def compare():
    with open('zippy\\output.zip', 'rb') as ori_zip_ref:
        biori = ori_zip_ref.read()

    with open("resurected\\recovered_files.zip", 'rb') as rec_zip_ref:
        birec = rec_zip_ref.read()
    lo=len(biori)
    lr=len(birec)
    print(lo)
    print(lr)
    if lo!=lr :
        return

    for i in range(lo):
        if biori[i] != birec[i]:
            print((hex(i))[2:]," -\t",biori[i] , birec[i]," -\t ",i)
    print('done')        
    
    
def splcompare():
    with open('zippy\\output.zip', 'rb') as ori_zip_ref:
        biori = ori_zip_ref.read()

    with open("resurected\\recovered_files.zip", 'rb') as rec_zip_ref:
        birec = rec_zip_ref.read()
    lo=len(biori)
    lr=len(birec)
    print(lo)
    print(lr)
    
    if lo!=lr :    
        if lo>lr :
            r=lo-lr
            for i in range(r):
                if biori[- (i+1)]!=0 :
                    print(biori[- (i+1)])
                    return
        elif lo<lr :
            r=lr-lo
            for i in range(r):
                if birec[- (i+1)]!=0 :
                    print(birec[- (i+1)])
                    return
    for i in range(lr):
        if biori[i] != birec[i]:
            print((hex(i))[2:]," -\t",biori[i] , birec[i]," -\t ",i)
    print('done')               
        

compare()
# splcompare()