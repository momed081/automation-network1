# script check ACL configuration on a router with config file ACL.txt with napalm
import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver('192.168.122.62', 'cisco', 'cisco')
iosvl2.open()


print ('Accessing 192.168.122.72')
iosvl2.load_merge_candidate(filename='ACL1.txt')

diffs = iosvl2.compare_config()
if len(diffs) > 0:
    print(diffs)
    iosvl2.commit_config()
else:
    print('No changes required.')
    iosvl2.discard_config()
iosvl2.close()


