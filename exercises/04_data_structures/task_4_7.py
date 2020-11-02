# -*- coding: utf-8 -*-
"""
Задание 4.7

Преобразовать MAC-адрес в строке mac в двоичную строку такого вида:
'101010101010101010111011101110111100110011001100'

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

mac = "AAAA:BBBB:CCCC"
mac_list = mac.split(':')

oc12h = mac_list[0]
oc34h = mac_list[1]
oc56h = mac_list[2]

oc12d = int(oc12h,16)
oc34d = int(oc34h,16)
oc56d = int(oc56h,16)

oc12b = bin(oc12d)
oc34b = bin(oc34d)
oc56b = bin(oc56d)

oc12bf = oc12b[2:]
oc34bf = oc34b[2:]
oc56bf = oc56b[2:]

result = oc12bf + oc34bf + oc56bf
print(result)
