biori=''
birec=''

def compare():
    with open('zippy\\output.zip', 'rb') as ori_zip_ref:
        biori = ori_zip_ref.read()

    with open("resurected\\recovered_files.zip", 'rb') as rec_zip_ref:
        birec = rec_zip_ref.read()
    print(len(biori))
    print(len(birec))
        
    for i in range(len(biori)):
        if biori[i] != birec[i]:
            print((hex(i))[2:]," -\t",biori[i] , birec[i]," -\t ",i)
    print('done')
compare()
# ori = ''.join(format(byte, '08b') for byte in biori)
# rec = ''.join(format(byte, '08b') for byte in birec)

# print(9988633)
# print(ori==rec)
# di=list(zip(ori,rec))
# for i in len(ori):
#     if ori[i] != rec[i]:-
#         print(i," - ",ori[i] , rec[i])

