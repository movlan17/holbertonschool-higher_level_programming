#!/usr/bin/python3
def uppercase(str):
    for c in str:
        # Əgər xarakter kiçik hərfdirsə
        if 'a' <= c <= 'z':
            # Kiçik hərfi böyük hərfə çevir
            print("{:c}".format(chr(ord(c) - 32)), end="")
        else:
            # Digər xarakterləri olduğu kimi çap et
            print("{:c}".format(c), end="")
    # Yeni sətr əlavə et
    print()
