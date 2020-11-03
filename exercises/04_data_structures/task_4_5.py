# -*- coding: utf-8 -*-
"""
Задание 4.5

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2 (пересечение).

Результатом должен быть такой список: ['1', '3', '8']

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"
vlans1 = command1.split()[-1] # Разделяем строку на блоки (разделитель пробел) и берем последний блок
vlans2 = command2.split()[-1]
vlans1 = vlans1.split(',') # Разделяем на отдельные символы (разделитель запятая)
vlans2 = vlans2.split(',') 
vlans = set(vlans1) & set(vlans2) # Преобразуем в множества и делаем пресечение множеств
vlans = list(vlans)  # Преобразуем в список
vlans = sorted(vlans)
print(vlans) 
