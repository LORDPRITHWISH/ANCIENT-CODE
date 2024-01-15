# print(ord('a'))
# print(ord('1'))
# print(ord('9'))
# print(ord('A'))
# print('\n'*2)


# print(122%16)
# print(chr(97))


def dehex(x):
    hex=''
    while x:
        a=x%16
        x=x//16
        print(x)
        if a>9 :
            hex+=chr(a+87)
        else:
            hex=str(a)+hex
    print('\n'*2)
    print(hex)
    
dehex(255)
# dehex(ord('z'))