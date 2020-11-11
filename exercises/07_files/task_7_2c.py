# -*- coding: utf-8 -*-
"""
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ignore = ["duplex", "alias", "Current configuration"]

from sys import argv

file_name_r = argv[1]
file_name_w = argv[2]

f = open(file_name_r)
f2 = open(file_name_w, 'w')     

for line in f:
        if line.find(ignore[0]) and line.find(ignore[1]) and line.find(ignore[2]) is -1:
            #print(line.strip())
            f2.writelines(line)
f.close()
f2.close()  
