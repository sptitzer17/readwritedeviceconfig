import sys
import subprocess
#Checking IP reachability

def ip_reach(list):
    for ip in list:
        ip = ip.rstrip('\n')
        pring_reply = subprocess.call('ping %s /n 2' % (ip), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        if pring_reply == 0:
            print('\n* {} is reachable :)\n'.format(ip))
            continue

        else:
            print('\n* {} not reachable :( Check connectivity and try again.'.format(ip))
            sys.exit()
