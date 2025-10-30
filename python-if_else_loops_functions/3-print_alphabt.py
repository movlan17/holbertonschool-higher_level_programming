#!/usr/bin/python3
for i in range(97, 123):           # 97 = 'a', 122 = 'z'
    if i != 101 and i != 113:      # 101 = 'e', 113 = 'q'
        print("{:c}".format(i), end="")
