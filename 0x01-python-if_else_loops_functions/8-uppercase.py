#!/usr/bin/python3
def uppercase(str):
    for i in str:
        tem = i
        if ord(tem) >= 97 and ord(tem) <= 122:
            tem = chr(ord(i) - 32)
        print("{}".format(tem), end='')
    print()
