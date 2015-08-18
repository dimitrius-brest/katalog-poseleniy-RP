# -*- coding: utf-8 -*-
try:
    f1 = open("input1.txt","r",encoding="utf-8")
except IOError:
    print("Не удалось найти входной файл input.txt")

try:
    f2 = open("output.txt","w",encoding="utf-8")
except IOError:
    print("Не удалось открыть выходной файл output.txt")

#

import re
ssylka_inner = re.compile("\[\[id.*?\|.*?\]\]")    # [[ | ]]  - нежадный: .*?
# c = re.compile("id\d*")               # id123455
str = "* '''Грушка''': [[id70486672|Радимир Ясько-Колтаков]]---[[id123|asdf]]---"
#iskomoe = re.search(ssylka_inner,str)  # находит только одну
iskomoe = re.findall(ssylka_inner,str)  # находит все
if iskomoe:
#    print("found", iskomoe.group())
    for name in iskomoe:
        #print("found", iskomoe.index(name), name)
        print(name)
        str.replace(name, "qqq")
    print(str)
else:
    print('did not find')
    
    

f1.close()
f2.close()

