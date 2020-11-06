# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Сообщение должно выводиться только один раз.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

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
