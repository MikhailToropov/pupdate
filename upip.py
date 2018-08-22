#!/usr/bin/python3
print("Hello")
import os
moduls_list = []
os.system("pip3 list > ~tmp.txt")
with open("~tmp.txt", 'r') as file:
    strings = file.readlines()
for i in strings[2:]:
    moduls_list.append(i.strip().split(' ')[0])

for i in moduls_list:
    os.system("pip3 install --upgrade "+i)
    
print("Update was successfully done")