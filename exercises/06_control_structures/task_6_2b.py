# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
while True:
    ip = input('Ввведите IP адрес в формате 1.2.3.4: ')
    try:
        octet1 = int(ip.split('.')[0])
        octet2 = int(ip.split('.')[1])
        octet3 = int(ip.split('.')[2])
        octet4 = int(ip.split('.')[3])
    except ValueError:
        print ('Неправильный IP-адрес')
    else:
        if ip == '255.255.255.255':
            print('local broadcast')
        elif ip == '0.0.0.0':
            print('unassigned')
        elif octet1 > 255 or octet2 > 255 or octet3 > 255 or octet4 > 255:
            print ('Не правильный IP-адрес')
        elif octet1 >= 1 and octet1 <=223:
            print('unicast')
        elif octet1 >= 224 and octet1 <=239:
            print('multicast')
        else:
            print('unused')
        break
