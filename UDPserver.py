from socket import *
host="localhost"
port=7000
add=(host,port)
server=socket(type=SOCK_DGRAM)
server.bind(add)
while True:
    print("waiting")
    data,addr=server.recvfrom(1024)
    print(data.decode(),addr)
    msg=input("respond")
    server.sendto(msg.encode(),addr)
server.close()
