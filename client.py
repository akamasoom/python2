import socket
host="192.168.107.9"
port=65432
with socket.socket() as s:
    s.connect((host,port))
    with open("hello.ipynb","rb") as f:
        s.sendfile(f)
    print("Sent")
