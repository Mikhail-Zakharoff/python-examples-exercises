# -*- coding: utf-8 -*-
"""
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "Current configuration"]

from sys import argv

file_name = argv[1]

f = open(file_name)
f2 = open('config_sw1_cleared.txt', 'w')     

for line in f:
        if line.find(ignore[0]) and line.find(ignore[1]) and line.find(ignore[2]) is -1:
            #print(line.strip())
            f2.writelines(line)
f.close()
f2.close()  
