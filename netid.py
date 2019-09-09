import socket
import uuid

hostname = socket.gethostname()
IPaddress = socket.gethostbyname(hostname)
hexIP = socket.inet_aton(IPaddress).hex()
macaddress=  (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
for ele in range(0,8*6,8)][::-1]))

print("The Computer name is: " +hostname)
print("The Computer IP is: " +IPaddress)
print("The Computer hexIP is: " +hexIP)
print("The Computer MAC is: " +macaddress)