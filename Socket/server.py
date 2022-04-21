import socket, time

# things to begin with
def tcp_connect(host_ip, port):
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host_ip, port))
    return

def tcp_server_wait(num_of_client_wait, port):
    global s2
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2.bind(('', port))
    s2.listen(num_of_client_wait)

def tcp_server_next():
    global s
    s = s2.accept()[0]

def tcp_write(data):
    s.send(data + '\r')
    return

def tcp_read():
    char = ' '
    recv_str = bytearray(' ')
    while char != '\r':
        char = s.recv(1)
        recv_str.append(char)
    return str(recv_str)

def tcp_close():
    s.close()
    return


tcp_server_wait(5, 17098)
tcp_server_next()
print
tcp_read()
tcp_write('hi')
print
tcp_read()
tcp_write('hi')
tcp_close()