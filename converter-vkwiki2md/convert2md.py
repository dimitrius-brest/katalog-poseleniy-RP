# -*- coding: utf-8 -*-
try:
    f1 = open("input.txt","r",encoding="utf-8")
except IOError:
    print("Не удалось найти входной файл input.txt")

try:
    f2 = open("output.txt","w",encoding="utf-8")
except IOError:
    print("Не удалось открыть выходной файл output.txt")

import re  # импортируем модуль работы с регулярными выражениями

# --- регулярное выражение для заголовков вида: == ййй ==
zagolovok_level2 = re.compile("==.*==")    #    жадный квантификатор .*

# --- регулярные выражения для внутренних ссылок вида [[id**|**]], [[club**|**]], [[public**|**]]
#ssylka_inner_tpl = re.compile("\[\[.*?\|.*?\]\]")         # [[ | ]]    нежадный кватнификатор .*?
ssylka_inner_id = re.compile("\[\[id.*?\|.*?\]\]")         # id      
ssylka_inner_club = re.compile("\[\[club.*?\|.*?\]\]")     # club
ssylka_inner_public = re.compile("\[\[public.*?\|.*?\]\]") # public

# --- регулярное выражение для внешних ссылок вида  [http**|**]
ssylka_outer = re.compile("\[http.*?\|.*?\]")

# --- регулярное выражение для вставки переноса на другую строку (если заканчивается на ":" + пробелы)
perenos = re.compile(":\s*$")

# --------

for stroka in f1.readlines():           #читаем входной файл построчно
    # ---- Замена заголовков
    if re.match(zagolovok_level2, stroka):
        stroka = stroka.replace("==","##",1)
        stroka = stroka.replace("==", "")        
    
    # ---- Замена жирного шрифта и курсива ----
    stroka = stroka.replace("'''",'**') # жирный шрифт - переделать в регулярные выражения!
    stroka = stroka.replace("''",'*')   # курсив       - переделать в регулярные выражения!

    # ---- Замена внутренних ссылок (id, club, public) ----
    iskomoe = (re.findall(ssylka_inner_id, stroka) +
               re.findall(ssylka_inner_club, stroka) +
               re.findall(ssylka_inner_public, stroka))  # находим все id,club,public
    if iskomoe:
        for ssylka in iskomoe:        # перебираем найденные ссылки в строке
            ssylka_id = ssylka.split("|")[0].replace('[[','')    #выделяем id ссылки
            ssylka_name = ssylka.split("|")[1].replace(']]','')  #выделяем имя ссылки
            ssylka_new = ('['+ssylka_name+']('+'http://vk.com/'+ssylka_id+')')        
            stroka = stroka.replace(ssylka, ssylka_new)     #заменяем старую ссылку на новую

    # ---- Замена внешних ссылок [http**|**] ----
    iskomoe2 = re.findall(ssylka_outer, stroka)
    if iskomoe2:        
        for ssylka2 in iskomoe2:            
            ssylka2_id = ssylka2.split("|")[0].replace('[http','http')
            ssylka2_name = ssylka2.split("|")[1].replace(']','')
            ssylka2_new = '['+ssylka2_name+']('+ssylka2_id+')'
            stroka = stroka.replace(ssylka2, ssylka2_new)                    

    # ---- Запись преобразованной строки в выходной файл ----    
    if re.search(perenos, stroka):
        f2.write('\n' + stroka)
    else:
        f2.write(stroka)

# --------     

f1.close()
f2.close()
