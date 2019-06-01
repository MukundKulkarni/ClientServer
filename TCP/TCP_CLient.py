import socket
s_port = 10001
s_address = '127.0.0.1'
c_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c_socket.connect((s_address,s_port))
msg = input(">>>")
b_msg = msg.encode()
c_socket.send(b_msg)
r_msg = c_socket.recv(1024)
print(r_msg)
c_socket.close()
