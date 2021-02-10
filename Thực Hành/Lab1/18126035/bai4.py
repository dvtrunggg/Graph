import os

def Check(file_path):
    check = os.path.exists(file_path)
    if check == False:
        print('File is not exist, please check again')
'''     
def Content():
    str = file.read()
    print('file content:', str)   # xuất nội dung file
'''

def Count(str):
    countw = len(str.split())   # đếm số chuỗi con, ( cách nhau khoảng trắng or somethings like it:))))
    print('file has ',countw,'words')
    print('The word you want to check how many time does it appear: ')
    name = input()
    count = str.count(name)
    print('This word appears',count,'times')

def Replace(str):
    print('======Replace word===== ')
    print('Old word: ')
    old = input()
    print('New Old: ')
    new = input()
    str = str.replace(old,new)
    print('Replaced')
    print(str)
    
def newFile( str):
    print('Enter link to access new file: ')
    link = input()
    file = open(link,'w+')
    file.write(str)
    
def fivecharWords(filein, fileout):
    w = open(fileout, "a+")

    f = open (filein,"r")
    line = f.read()
    line = line.replace("\n", " ")
    line = line.split(" ")

    for x in line:
        if len(x) >= 5:
            w.write(x)
            w.write(' ')

        
    

file = ('test.txt')
Check(file)
file = open(file,'r')
str = file.read()
print('file content:', str)   # xuất nội dung file
Count(str)
Replace(str)
newFile(str)
fivecharWords('test.txt','123.txt')
file.close()