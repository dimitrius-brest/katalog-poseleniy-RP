# -*- coding: utf-8 -*-
try:
    f1 = open("input.txt","r",encoding="utf-8")
except IOError:
    print("Не удалось найти входной файл input.txt")

try:
    f2 = open("output.txt","w",encoding="utf-8")
except IOError:
    print("Не удалось открыть выходной файл output.txt")

import re           # импортируем модуль работы с регулярными выражениями

str = "* '''Грушка''': [[id70486672|Радимир Ясько-Колтаков]]---[[public123|asdf]]---"
print(str)

# ---- Замена внутренних ссылок (id, club, public) ----

#ssylka_inner_tpl = re.compile("\[\[.*?\|.*?\]\]")         # [[ | ]] - нежадный: .*?
ssylka_inner_id = re.compile("\[\[id.*?\|.*?\]\]")         # id      
ssylka_inner_club = re.compile("\[\[club.*?\|.*?\]\]")     # club
ssylka_inner_public = re.compile("\[\[public.*?\|.*?\]\]") # public
 
iskomoe = (re.findall(ssylka_inner_id,str) +
           re.findall(ssylka_inner_club,str) +
           re.findall(ssylka_inner_public,str))  # находит все id,club,public
if iskomoe:
    for ssylka in iskomoe:        
        ssylka_id=ssylka.split("|")[0].replace('[[','')    #выделяем id ссылки
        ssylka_name=ssylka.split("|")[1].replace(']]','')  #выделяем имя ссылки
        ssylka_new=('['+ssylka_name+']('+'http://vk.com/'+ssylka_id+')')        
        str=str.replace(ssylka, ssylka_new)     #заменяем старую ссылку на новую
    print(str)    
else:
    print('did not find')

# --------    
    
f1.close()
f2.close()
