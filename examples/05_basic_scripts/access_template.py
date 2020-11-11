import sys

vlan = sys.argv[1]
#print(sys.argv)
#print(vlan)


access_template = ['switchport mode access',
                   'switchport access vlan {}',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

print('\n'.join(access_template).format(vlan))

