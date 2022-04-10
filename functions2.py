#!/usr/bin/env python3

import ipaddress

tet_nets = ['91.105.0.0/17', '46.109.0.0/16', '194.8.16.0/21', '194.8.24.0/22', '194.8.40.0/23', '194.8.43.0/24', '195.122.0.0/19', '195.13.128.0/17', '80.232.128.0/17',
'81.198.0.0/16', '84.237.128.0/17', '87.110.0.0/16', '194.8.9.0/24', '195.114.32.0/19', '195.2.96.0/19', '62.85.0.0/17', '87.246.144.0/20', '87.246.160.0/19', '78.84.0.0/16',
'193.200.224.0/24', '95.68.0.0/17', '195.2.111.0/24','62.85.0.0/18','81.198.170.0/24']
tet_address = []

lmt_nets = ['80.89.72.0/21', '212.3.192.0/19', '185.65.160.0/22', '212.93.96.0/19', '213.175.79.0/24', '185.147.56.0/22', '193.108.29.0/24', '194.125.240.0/24']
lmt_address = []

bite_nets = ['84.15.0.0/16', '213.226.128.0/18', '213.252.192.0/18', '159.148.8.0/23']
bite_address = []

tele2_nets = ['90.130.96.0/19', '90.130.104.0/22', '213.100.164.0/22', '213.100.176.0/21', '213.100.184.0/22', '213.100.168.0/21', '90.142.32.0/19', '91.128.32.0/19',
'213.102.108.0/22', '83.178.136.0/22', '83.176.128.0/23', '83.178.226.0/23', '83.178.225.0/24', '83.176.150.0/23', '83.176.152.0/21', '83.177.168.0/21', '83.177.176.0/20', '83.187.156.0/22',
'90.129.224.0/19', '213.100.6.0/23', '213.100.8.0/23', '213.100.112.0/21', '213.101.224.0/19', '213.102.92.0/22', '213.102.96.0/21', '213.102.105.0/24', '213.102.106.0/23', '213.100.132.0/23',
'90.128.0.0/18', '90.128.64.0/18', '213.100.0.0/22', '213.100.28.0/22', '213.100.4.0/23', '213.101.208.0/22', '83.177.128.0/19', '83.177.192.0/19', '83.178.200.0/22',
'83.178.204.0/23', '90.141.73.0/24', '90.141.74.0/23', '90.141.76.0/22', '213.100.16.0/21', '94.186.40.0/21', '94.186.64.0/18', '213.100.160.0/22', '213.101.130.128/25',
'213.101.190.0/23', '213.101.216.0/23', '90.139.64.0/19', '90.139.0.0/18', '90.133.0.0/17', '90.133.128.0/20', '90.133.144.0/20', '90.133.160.0/20', '90.133.176.0/20',
'90.133.192.0/19', '213.101.160.0/22', '213.102.24.0/21', '90.131.128.0/18', '90.141.64.0/21', '90.141.96.0/19', '91.131.128.0/20', '94.186.48.0/20', '91.131.128.0/18',
'91.131.144.0/21', '213.121.216.0/23', '83.178.128.0/21', '83.178.206.0/23', '83.177.240.0/20', '213.100.130.0/23', '77.219.0.0/19', '83.176.130.0/23', '83.176.132.0/22',
'83.176.136.0/21', '83.176.144.0/22', '83.176.148.0/23', '83.177.224.0/20', '83.178.72.0/22', '83.178.76.0/22', '83.178.140.0/22', '83.178.144.0/22', '83.178.160.0/21',
'83.178.168.0/21', '83.178.188.0/24', '83.178.189.0/24', '83.178.208.0/21', '83.178.216.0/21', '83.178.228.0/23', '83.183.80.0/20', '83.183.144.0/20', '83.183.224.0/20',
'83.187.152.0/23', '83.187.154.0/23', '83.188.176.0/23', '83.188.178.0/23', '83.189.192.0/18', '90.130.160.0/21', '90.130.168.0/21', '90.130.176.0/21','90.130.188.0/22',
'90.130.190.0/24', '90.130.191.0/24', '90.134.128.0/21', '90.137.134.0/24', '90.137.135.0/24', '213.100.10.0/23', '213.100.12.0/22', '213.100.16.0/22', '213.100.20.0/22',
'213.100.24.0/24', '213.100.25.0/24', '213.100.26.0/23', '213.100.48.0/20', '213.100.120.0/21', '213.100.128.0/23', '213.101.128.0/23', '213.101.184.0/22', '213.101.188.0/24',
'213.101.189.0/24', '213.101.212.0/22', '213.102.1.0/24', '213.102.2.0/24', '213.102.20.0/24', '213.102.21.0/24', '213.102.22.0/24', '213.102.24.0/23', '213.102.30.0/24',
'213.102.31.0/24', '213.102.88.0/22', '213.102.104.0/24', '213.102.144.0/20']
tele2_address = []

cloud_nets = ['185.129.151.0/24', '92.63.91.0/24', '185.176.220.0/22', '185.176.220.0/24', '185.176.221.0/24', '185.176.222.0/24', '185.176.223.0/24']
cloud_address = []

latnet_nets = ['94.101.224.0/20', '217.69.112.0/20', '46.19.200.0/21', '80.81.32.0/19', '83.223.128.0/19','91.190.32.0/19','159.148.0.0/16','85.254.0.0/17', '85.254.128.0/18',
'176.67.32.0/20','185.62.196.0/22', '185.176.60.0/22','185.176.116.0/22']
latnet_address = []

telia_nets = ['185.87.204.0/22', '194.19.224.0/19', '213.175.64.0/18', '80.233.128.0/17', '62.63.128.0/18', '78.154.128.0/19', '78.28.192.0/18', '94.100.0.0/20']
telia_address = []

decta_nets = ['185.178.48.0/24']
decta_address = []

itservices_nets = ['185.129.148.0/24', '92.63.87.0/24']
itservices_address = []

baltcom_nets = ['109.110.0.0/19', '136.169.0.0/17', '185.211.96.0/22', '185.7.236.0/22', '188.112.128.0/18', '195.244.128.0/20', '195.62.128.0/19', '213.180.96.0/19',
'217.198.224.0/20', '217.199.96.0/19', '217.24.64.0/20', '37.148.168.0/21', '62.84.0.0/19', '77.38.128.0/17', '79.132.64.0/19', '80.254.208.0/20', '80.255.224.0/20',
 '85.115.96.0/19', '85.234.160.0/19', '85.254.120.0/23', '87.226.0.0/17', '89.18.192.0/19', '89.191.96.0/19', '89.201.0.0/17', '91.123.64.0/20', '91.142.0.0/20', '91.188.32.0/19',
 '93.177.192.0/18', '94.30.128.0/17']
baltcom_address = []

telenet_nets = ['109.197.208.0/21', '109.197.208.0/24', '109.229.192.0/19', '171.25.218.0/23', '176.103.176.0/20', '176.103.192.0/21', '176.106.160.0/20', '176.106.176.0/21',
'176.106.48.0/20', '176.106.96.0/21', '185.47.10.0/24', '185.47.11.0/24', '193.0.239.0/24', '193.111.244.0/22', '193.238.212.0/22', '193.238.216.0/21', '194.9.212.0/22',
'194.9.212.0/24', '195.69.88.0/22', '213.110.64.0/19', '31.42.80.0/20', '83.243.88.0/21', '84.38.136.0/21', '87.99.64.0/19', '87.99.64.0/24', '87.99.65.0/24', '87.99.66.0/24',
'87.99.67.0/24', '87.99.95.0/24', '88.135.128.0/19', '91.224.0.0/23', '91.233.214.0/23', '91.90.224.0/19', '91.90.230.0/24', '91.90.231.0/24', '91.90.236.0/24', '91.90.238.0/24',
'91.90.255.0/24' ]
telent_address = []

jsc_nets = ['109.73.100.0/24' ,'109.73.102.0/23', '109.73.107.0/24', '109.73.96.0/20', '109.73.97.0/24', '185.141.52.0/22', '185.141.52.0/24', '185.141.55.0/24', '185.31.44.0/22',
'185.31.44.0/24', '185.31.45.0/24', '185.57.77.0/24', '185.75.236.0/22', '185.75.236.0/24', '185.75.238.0/24', '185.75.239.0/24', '188.92.16.0/21', '194.8.6.0/24', '212.142.64.0/18',
'217.195.48.0/20', '46.23.32.0/20', '46.23.32.0/24', '77.93.0.0/19', '77.93.0.0/20', '77.93.12.0/24', '77.93.13.0/24', '77.93.14.0/24', '77.93.16.0/20', '77.93.29.0/24', '82.193.64.0/19',
'82.193.76.0/24', '82.193.80.0/24', '82.193.95.0/24', '83.99.128.0/17', '83.99.128.0/23', '83.99.134.0/23', '83.99.137.0/24', '83.99.144.0/24', '83.99.149.0/24', '83.99.158.0/24',
'83.99.166.0/24', '83.99.174.0/24', '83.99.180.0/24', '83.99.182.0/24', '83.99.187.0/24', '83.99.189.0/24', '83.99.190.0/24', '83.99.199.0/24', '83.99.201.0/24', '83.99.202.0/24',
'83.99.206.0/24', '83.99.208.0/24', '83.99.215.0/24', '83.99.220.0/24', '83.99.224.0/24', '83.99.234.0/24', '83.99.241.0/24', '83.99.242.0/24']
jsc_address = []


lumii_nets = ['185.23.160.0/22', '194.0.8.0/24', '85.254.192.0/18', '194.8.1.0/24', '194.8.2.0/23', '91.198.156.0/24', '92.240.64.0/19', '194.0.48.0/24', '194.0.49.0/24',
'194.0.50.0/24', '91.240.246.0/23', '5.152.224.0/21']
lumii_address = []

skatvis_nets = ['85.158.72.0/21', '89.221.112.0/23', '89.221.114.0/23', '89.221.116.0/23', '89.221.118.0/23', '89.221.120.0/23', '89.221.122.0/23', '89.221.124.0/23', '89.221.126.0/23']
skatvis_address = []

mikronet_nets = ['85.255.64.0/20']
mikronet_address = []

altnet_nets = ['195.3.144.0/22', '195.3.147.0/24']
altnet_address = []

singularity_nets = ['176.118.37.0/24', '178.171.0.0/20', '185.100.156.0/23', '185.101.200.0/23', '185.101.202.0/24', '185.103.60.0/23', '185.103.62.0/24', '185.104.148.0/23',
'185.104.150.0/24', '185.111.24.0/24', '178.171.20.0/23']
singularity_address = []

ostkom_nets = ['185.182.92.0/22', '89.254.128.0/18']
ostkom_address = []

mikronet_nets = ['85.255.64.0/20']
mikronet_address = []

nanoit_nets = ['141.136.0.0/21', '159.148.102.0/24', '159.148.198.0/23', '159.148.200.0/24', '178.249.32.0/21', '185.61.148.0/22', '185.61.148.0/23', '185.61.150.0/24',
'185.71.128.0/22', '185.72.204.0/22', '185.72.84.0/22', '185.80.236.0/22', '185.81.128.0/23', '185.81.48.0/22', '185.81.49.0/24', '185.82.124.0/22', '185.86.151.0/24',
'188.92.72.0/21', '193.46.236.0/24', '195.43.82.0/23', '31.170.16.0/21', '46.19.144.0/21', '5.44.216.0/21', '80.246.31.0/24', '80.250.48.0/20', '83.241.0.0/17',
'85.254.142.0/23', '85.254.145.0/24', '85.254.16.0/22', '85.254.24.0/22', '85.254.32.0/21', '85.254.5.0/24', '85.31.96.0/21', '86.63.160.0/19', '86.63.184.0/22',
'87.246.128.0/20', '89.248.80.0/20', '91.135.80.0/20', '91.135.86.0/24', '91.203.68.0/22', '91.224.12.0/23', '91.237.98.0/23', '94.140.111.0/24', '94.140.112.0/23',
'94.140.114.0/23', '94.140.116.0/22', '94.140.120.0/22', '94.140.120.0/23', '94.140.123.0/24', '94.140.96.0/19', '95.215.45.0/24']
nanoit_address = []

cloudhosting_nets = ['185.8.60.0/22', '87.246.183.0/24', '91.220.43.0/24', '94.30.181.0/24']
cloudhosting_address = []

good_nets = ['146.185.239.0/24', '159.148.38.0/24', '159.148.88.0/24','91.247.38.0/24']
good_address = []

manual_check = []

def check_lmt(address):
    for lmt in lmt_nets:
        if address in ipaddress.IPv4Network(lmt):
            return True

def check_tet(address):
    for tet in tet_nets:
        if address in ipaddress.IPv4Network(tet):
            return True

def check_tele2(address):
    for tele2 in tele2_nets:
        if address in ipaddress.IPv4Network(tele2):
            return True

def check_bite(address):
    for bite in bite_nets:
        if address in ipaddress.IPv4Network(bite):
            return True

def check_cloud (address):
    for cloud in cloud_nets:
        if address in ipaddress.IPv4Network(cloud):
            return True

def check_latnet (address):
    for latnet in latnet_nets:
        if address in ipaddress.IPv4Network(latnet):

            return True
def check_telia (address):
    for telia in telia_nets:
        if address in ipaddress.IPv4Network(telia):
            return True

def check_decta (address):
    for decta in decta_nets:
        if address in ipaddress.IPv4Network(decta):
            return True

def check_itservices (address):
    for itservices in itservices_nets:
        if address in ipaddress.IPv4Network(itservices):
            return True

def check_baltcom (address):
    for baltcom in baltcom_nets:
        if address in ipaddress.IPv4Network(baltcom):
            return True
def check_telenet (address):
    for telenet in telenet_nets:
        if address in ipaddress.IPv4Network(telenet):
            return True

def check_jsc (address):
    for jsc in jsc_nets:
        if address in ipaddress.IPv4Network(jsc):
            return True

def check_lumii (address):
    for lumii in lumii_nets:
        if address in ipaddress.IPv4Network(lumii):
            return True

def check_skatvis (address):
    for skatvis in skatvis_nets:
        if address in ipaddress.IPv4Network(skatvis):
            return True

def check_mikronet (address):
    for mikronet in mikronet_nets:
        if address in ipaddress.IPv4Network(mikronet):
            return True

def check_altnet (address):
    for altnet in altnet_nets:
        if address in ipaddress.IPv4Network(altnet):
            return True

def check_singularity (address):
    for singularity in singularity_nets:
        if address in ipaddress.IPv4Network(singularity):
            return True

def check_ostkom (address):
    for ostkom in ostkom_nets:
        if address in ipaddress.IPv4Network(ostkom):
            return True

def check_nanoit (address):
    for nanoit in nanoit_nets:
        if address in ipaddress.IPv4Network(nanoit):
            return True

def check_cloudhosting (address):
    for cloudhosting in cloudhosting_nets:
        if address in ipaddress.IPv4Network(cloudhosting):
            return True

def check_good (address):
    for good in good_nets:
        if address in ipaddress.IPv4Network(good):
            return True


with open('/home/kali/Desktop/cert/lv.list.ip') as topo_file:
    for line in topo_file:
        net4 = line.rstrip()
        address = ipaddress.ip_address(net4)
        if check_lmt(address):
            lmt_address.append(net4)

        elif check_tet(address):
            tet_address.append(net4)

        elif check_tele2(address):
            tele2_address.append(net4)

        elif check_bite(address):
            bite_address.append(net4)

        elif check_cloud(address):
            cloud_address.append(net4)

        elif check_latnet(address):
            latnet_address.append(net4)

        elif check_telia(address):
            telia_address.append(net4)

        elif check_decta(address):
            decta_address.append(net4)

        elif check_itservices(address):
            itservices_address.append(net4)

        elif check_baltcom(address):
            baltcom_address.append(net4)

        elif check_telenet(address):
            telent_address.append(net4)

        elif check_jsc(address):
            jsc_address.append(net4)

        elif check_lumii(address):
            lumii_address.append(net4)

        elif check_skatvis(address):
            skatvis_address.append(net4)

        elif check_mikronet(address):
            mikronet_address.append(net4)

        elif check_altnet(address):
            altnet_address.append(net4)

        elif check_singularity(address):
            singularity_address.append(net4)

        elif check_ostkom(address):
            ostkom_address.append(net4)

        elif check_nanoit(address):
            nanoit_address.append(net4)

        elif check_cloudhosting(address):
            cloudhosting_address.append(net4)

        elif check_good(address):
            good_address.append(net4)

        else:
            manual_check.append(net4)


print(f"TET tet@tet.lv ")
print(*tet_address, sep = ", ")

print(f"LMT info@lmt.lv ")
print(*lmt_address, sep = ", ")

print(f"Bite info@bite.lv ")
print(*bite_address, sep = ", ")

print(f"Tele2 info@tele2.lv ")
print(*tele2_address, sep = ", ")

print(f"LATNET abuse@latnet.eu ")
print(*latnet_address, sep = ", ")

print(f"2cloud abuse@2cloud.eu ")
print(*cloud_address, sep = ", ")

print(f"2cloud abuse@2cloud.eu ")
print(*cloud_address, sep = ", ")

print(f"telia abuse@telia.lv ")
print(*telia_address, sep = ", ")

print(f"Decta network@decta.com ")
print(*decta_address, sep = ", ")

print(f"itservices.ws info@itservices.ws ")
print(*itservices_address, sep = ", ")

print(f"Baltcom core@baltcom.lv ")
print(*baltcom_address, sep = ", ")

print(f"Telenet noc@telenet.lv ")
print(*telent_address, sep = ", ")

print(f"JSC BALTICOM abuse@balticom.lv ")
print(*jsc_address, sep = ", ")

print(f"LUMII noc@lumii.lv ")
print(*lumii_address, sep = ", ")

print(f"SkaTVis abuse@skatvis.net ")
print(*skatvis_address, sep = ", ")

print(f"Mikronet info@mikronet.lv ")
print(*mikronet_address, sep = ", ")

print(f"altnet admin@altnet.lv ")
print(*altnet_address, sep = ", ")

print(f"Singularity Telecom ceo@ws.network ")
print(*singularity_address, sep = ", ")

print(f"OSTKOM info@ostkom.lv ")
print(*ostkom_address, sep = ", ")

print(f"Nano IT abuse@nano.lv ")
print(*nanoit_address, sep = ", ")

print(f"CloudHosting vh@cloudhosting.lv ")
print(*nanoit_address, sep = ", ")

print(f"GOOD abuse@goodtec.lv ")
print(*good_address, sep = ", ")

print(f"Needs Manual Check ")
print(*manual_check, sep = ", ")
