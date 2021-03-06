# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

interf_type = input('Введите режим работы интерфейса (access/trunk): ')
interf = input('Введите тип и номер интерфейса: ')

show_vlan = { 'access' : 'Ввведите номер VLAN: ', 'trunk' : 'Введите разрешенные VLANы: ' }

vlan = input(show_vlan[interf_type])

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]

show_conf = { 'access': access_template, 'trunk': trunk_template }

print('\ninterface:' + interf)
print('\n'.join(show_conf[interf_type]).format(vlan))
