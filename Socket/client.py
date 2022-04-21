import socket, time

def tcp_connect(host_ip, port):
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host_ip, port))
    return

def tcp_write(data):
    b_array = bytearray(data)
    b_array.append('\r')
    s.send(b_array)
    return

def tcp_read():
    char = ' '
    recv_str = bytearray('')
    while char != '\r':
        char = s.recv(1)
        recv_str.append(char)
    return str(recv_str)

def tcp_close():
    s.close()
    return

tcp_connect('127.0.0.1', 17098)
tcp_write('Hello World.')
print
tcp_read()
tcp_write('Python')
print
tcp_read()
tcp_close()