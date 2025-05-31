import socket
host='localhost'
port=65432
with socket.socket() as s:
    s.bind((host,port))
    s.listen()
    conn,addr=s.accept()
    with conn:
        print(f"connection by {addr}")
        with open("new.ipynb","wb") as f:
            while True:
                data=conn.recv(4096)
                if not data:
                    break
                f.write(data)
        print("recieved file")
