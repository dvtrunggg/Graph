import re

def read(filein):
    file = open(filein, "r")
    contents = file.read()
    file.close()

    print('Danh bạ: ')
    print(contents)

def name(filein):
    with open (filein, 'r') as f:
        name = sorted (name.rstrip('\n') for name in f)

    print (name)

def search(filein, input):
    with open (filein, 'r') as f:
        name = sorted (name.rstrip('\n') for name in f)

    for i in range(len(name)):
        if input in name[i]:
            print(name[i])

def edit(filein):
    with open (filein, 'r') as f:
        name = sorted (name.rstrip('\n') for name in f)

    print('Nhập liên hệ cần thay đổi')
    contact = input()

    print('Nhập dữ liệu cần thay đổi')
    old = input()

    print('Nhập dữ liệu thay đổi')
    new = input()

    for i in range(len(name)):
        if contact in name[i]:
            name[i] = name[i].replace(old, new)

    print(name)
