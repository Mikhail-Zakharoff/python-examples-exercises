# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
ospf_route_templete = '''
    Prefix {:>25}
    AD/Metric {:>16}
    Next-Hop {:>20}
    Last update {:>13}
    Outbound Intrface {:>17}
    '''
ospf_route_str = ospf_route.split()
prefix = ospf_route_str[0] 
metric = ospf_route_str[1][1:-1]
nh = ospf_route_str[3][:-1]
update = ospf_route_str[4][:-1]
interface = ospf_route_str[5]
print(ospf_route_templete.format(prefix, metric, nh, update, interface))
