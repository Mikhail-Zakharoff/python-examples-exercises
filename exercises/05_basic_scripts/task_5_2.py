# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip_adr = input('Введите IP-сети в формате 1.2.3.0/24: ')

ip = ip_adr.split('/')[0] 
mask = ip_adr.split('/')[1]
maskds = int(mask)

ip_spl = ip.split('.')

ip_oc1 = ip_spl[0]
ip_oc2 = ip_spl[1]
ip_oc3 = ip_spl[2]
ip_oc4 = ip_spl[3]

ip_oc1d = int(ip_oc1)
ip_oc2d = int(ip_oc2)
ip_oc3d = int(ip_oc3)
ip_oc4d = int(ip_oc4)
sp = ' '

print('Network:')
print("{:<10} {:<10} {:<10} {:<10}".format(ip_oc1, ip_oc2, ip_oc3, ip_oc4))  
print("{:08b} {} {:08b} {} {:08b} {} {:08b}".format(ip_oc1d, sp, ip_oc2d, sp, ip_oc3d, sp, ip_oc4d))

maskb = "1" * maskds + "0" * (32 - maskds)
mask_oc1b = maskb[0:8]
mask_oc2b = maskb[8:16]
mask_oc3b = maskb[16:24]
mask_oc4b = maskb[24:32]

mask_oc1d = int(mask_oc1b, 2)
mask_oc2d = int(mask_oc2b, 2)
mask_oc3d = int(mask_oc3b, 2)
mask_oc4d = int(mask_oc4b, 2)

print('\nMask:')
print('/' + mask)
print("{:<10} {:<10} {:<10} {:<10}".format(mask_oc1d, mask_oc2d, mask_oc3d, mask_oc4d))
print("{:<10} {:<10} {:<10} {:<10}".format(mask_oc1b, mask_oc2b, mask_oc3b, mask_oc4b))

  
