# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком виде:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
f = open('ospf.txt')

for line in f:
    list1 = line.split()
    print ('Prefix {:>27}'.format(list1[1]))
    print ('AD/Metric {:>18}'.format((list1[2]).strip('[]')))
    print ('Next-Hop {:>22}'.format((list1[4]).strip(',')))
    print ('Last update {:>15}'.format((list1[5]).strip(',')))
    print ('Outbound Interface {:>18}'.format(list1[6]))
    print ('\n')
