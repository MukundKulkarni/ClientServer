import socket
s_address= "127.0.0.1"
s1_port = 10000
s1_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s2_port = 10001
s2_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s1_socket.bind((s_address,s1_port))
s2_socket.bind((s_address,s2_port))
print("...connecting")
while True:
    print("...receving")
    (msg1,c1_address) = s1_socket.recvfrom(2048)
    print(msg1)
    msg1 = msg1.upper()
    (msg2,c2_address) = s2_socket.recvfrom(2048)
    print(msg2)
    msg2 = msg2.upper()
    s1_socket.sendto(msg1,(c2_address))
    s2_socket.sendto(msg2,(c1_address))
