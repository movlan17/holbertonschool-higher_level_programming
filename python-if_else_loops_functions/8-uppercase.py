#!/usr/bin/python3
def uppercase(str):
    result = ""
    for c in str:
        if 'a' <= c <= 'z':
            result += chr(ord(c) - 32)  # Kiçik hərfi böyük hərfə çevir
        else:
            result += c  # Digər xarakterləri olduğu kimi əlavə et
    print("{}".format(result))
