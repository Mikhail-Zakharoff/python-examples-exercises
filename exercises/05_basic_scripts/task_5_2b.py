# -*- coding: utf-8 -*-
"""
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
from sys import argv

ip_adr = argv[1]

#ip_adr = input('Введите IP-сети в формате 1.2.3.0/24: ')

ip = ip_adr.split('/')[0] 
mask = ip_adr.split('/')[1]
maskds = int(mask)

ip_spl = ip.split('.')

# делим Ip-адрес на октеты
ip_oc1 = ip_spl[0]
ip_oc2 = ip_spl[1]
ip_oc3 = ip_spl[2]
ip_oc4 = ip_spl[3]

# преобразуем октеты IP-адреса в числа
ip_oc1d = int(ip_oc1)
ip_oc2d = int(ip_oc2)
ip_oc3d = int(ip_oc3)
ip_oc4d = int(ip_oc4)
sp = ' '

# преобразуем IP-адрес в двоичный вид
ip_oc1b = bin(ip_oc1d)[2:]
len_ip_oc1b = len(str(ip_oc1b))
len_0_ip_oc1b = 8 - len_ip_oc1b
ip_oc1b_full = "0" * len_0_ip_oc1b + ip_oc1b

ip_oc2b = bin(ip_oc2d)[2:]
len_ip_oc2b = len(str(ip_oc2b))
len_0_ip_oc2b = 8 - len_ip_oc2b
ip_oc2b_full = "0" * len_0_ip_oc2b + ip_oc2b

ip_oc3b = bin(ip_oc3d)[2:]
len_ip_oc3b = len(str(ip_oc3b))
len_0_ip_oc3b = 8 - len_ip_oc3b
ip_oc3b_full = "0" * len_0_ip_oc3b + ip_oc3b

ip_oc4b = bin(ip_oc4d)[2:]
len_ip_oc4b = len(str(ip_oc4b))
len_0_ip_oc4b = 8 - len_ip_oc4b
ip_oc4b_full = "0" * len_0_ip_oc4b + ip_oc4b

ip_b = ip_oc1b_full + ip_oc2b_full + ip_oc3b_full + ip_oc4b_full

ip_b_net = ip_b[:maskds] # отрезаем адрес сети
ip_b_net_full = ip_b_net + "0" * (32 - 24)

ip_oc1b = ip_b_net_full[0:8]
ip_oc2b = ip_b_net_full[8:16]
ip_oc3b = ip_b_net_full[16:24]
ip_oc4b = ip_b_net_full[24:32]

ip_oc1d_net = int(ip_oc1b, 2) 
ip_oc2d_net = int(ip_oc2b, 2)
ip_oc3d_net = int(ip_oc3b, 2)
ip_oc4d_net = int(ip_oc4b, 2)

print('Network:')
print("{:<10} {:<10} {:<10} {:<10}".format(ip_oc1d_net, ip_oc2d_net, ip_oc3d_net, ip_oc4d_net))  
print("{} {} {} {} {} {} {}".format(ip_oc1b, sp, ip_oc2b, sp, ip_oc3b, sp, ip_oc4b))


maskb = "1" * maskds + "0" * (32 - maskds) # создаем двоичную маску 
mask_oc1b = maskb[0:8]
mask_oc2b = maskb[8:16]
mask_oc3b = maskb[16:24]
mask_oc4b = maskb[24:32]

mask_oc1d = int(maskb[0:8], 2)
mask_oc2d = int(maskb[8:16], 2)
mask_oc3d = int(maskb[16:24], 2)
mask_oc4d = int(maskb[24:32], 2)

print('\nMask:')
print('/' + mask)
print("{:<10} {:<10} {:<10} {:<10}".format(mask_oc1d, mask_oc2d, mask_oc3d, mask_oc4d))
print("{:<10} {:<10} {:<10} {:<10}".format(mask_oc1b, mask_oc2b, mask_oc3b, mask_oc4b))
