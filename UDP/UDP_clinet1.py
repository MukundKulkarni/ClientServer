import socket
s_address="127.0.0.1"
s_port = 10000
c1__socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while(True):
    msg = input("sent >>>")
    if input == "exit":
        break
    b_code = msg.encode()
    c1__socket.sendto(b_code,(s_address,s_port))
    (msg,s_address) = c1__socket.recvfrom(2048)
    print("received >>>",msg)
c1__socket.close()
