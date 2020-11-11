# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "Current configuration"]

from sys import argv

file_name = argv[1]

f = open(file_name)

for line in f:
        if line.find('!') and line.find(ignore[0]) and line.find(ignore[1]) and line.find(ignore[2]) is -1:
            print(line.strip())
