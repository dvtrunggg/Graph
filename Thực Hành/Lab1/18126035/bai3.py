
import re       # Regular Expression - dùng cho các bài toán so khớp chuỗi hay tập chuỗi 

def InputStr(str):
    flag = 0    
    while True:
        if len(str) <9 and len(str)>20:
            flag = -1
            break           #break khỏi loop khi gặp dk
        elif not re.search("[a-z]", str):        #use not in if ( phủ định) - check nếu ko có chữ in thường -> break
            flag = -1
            break
        elif not re.search("[A-Z]", str):    # check chữ in hoa
            flag = -1
            break
        elif not re.search("[0-9]", str):          #check number
            flag = -1
            break
        elif not re.search("[_@$!#%^&*|\~, ./+-=]", str):    #check ký tự đặc biệt
            flag = -1
            break 
        else:
            flag = 0    
            break
    return flag

def encodePass(str, k):
    encodePass = []
    p = 0
    for i in range(len(str)):
        if ord(str[i]) + k > 126:
            p = ord(str[i]) + k -126 +20
        else:
            p = ord(str[i]) + k
        encodePass.append(chr(p))
    return encodePass
def decodePass(str, k):
    decodePass = []
    p = 0
    for i in range(len(str)):
        if ord(str[i]) - k <21:
            p = ord(str[i]) - k + 106
        else:
            p = ord(str[i]) - k
        decodePass.append(chr(p))
    return decodePass
        

'''
str = "HaHa@12345 "
if InputStr(str) == 0:
    print("your password is strong")
    encodePass(str,0)
    decodePass(str,0)
else:
    print("your password is not strong")
'''