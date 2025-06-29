#must be run root##
###I LIED DONT RUN AS ROOT, IT WILL NOT WORK###
###WHY I DONT KNOW FUCK THIS###

import nmap
from WIFIip import get_local_ip

def scan():
    nm = nmap.PortScanner()
    local_ip = get_local_ip()
    subnet = local_ip.rsplit('.', 1)[0] + '.0/24'
    nm.scan(hosts=subnet, arguments='-sn -PR')
    for host in nm.all_hosts():
        status = nm[host]['status']['state']
        mac = nm[host]['addresses'].get('mac', 'N/A')
        vendor = nm[host].get('vendor', {}).get(mac, 'Unknown')
        print(f"{host} is {status}   MAC: {mac}   Vendor: {vendor}")
    return nm.all_hosts()