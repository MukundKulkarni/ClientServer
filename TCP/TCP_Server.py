import socket
s_port = 10001
s_address = '127.0.0.1'
s_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s_socket.bind((s_address,s_port))
s_socket.listen(1)
con_socket, c_address = s_socket.accept()
msg = con_socket.recv(1024)
u_msg = msg.upper()
con_socket.send(u_msg)
con_socket.close()
