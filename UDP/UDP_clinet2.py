import socket
s_address="127.0.0.1"
s_port = 10001
c2__socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while(True):
    msg = input("sent >>>")
    if msg  == "exit":
        break
    b_code = msg.encode()
    c2__socket.sendto(b_code,(s_address,s_port))
    (msg,s_address) = c2__socket.recvfrom(2048)
    print("received >>>",msg)
c2__socket.close()
