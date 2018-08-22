#!/usr/bin/python3
print("Start upgrage all packeges installed by pip")
import os
os.system("pip3 list > ~tmp.txt")
with open("~tmp.txt", 'r') as file:
    strings = file.readlines()
for i in strings[2:]:
    os.system("pip3 install --upgrade "+i.strip().split(' ')[0])

os.system("echo 0 > ~tmp.txt")
print("Update was successfully done")
