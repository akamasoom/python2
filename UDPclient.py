from socket import *
host="localhost"
port=7000
addr=(host,port)
client=socket(type=SOCK_DGRAM)
while True:
    data=input('->')
    if not data:
        break
    client.sendto(data.encode(),addr)
    print('receive')
    data,addr=client.recvfrom(1028)
    if not data:
        break
    print(data.decode())
client.close()
