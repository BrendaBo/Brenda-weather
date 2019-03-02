import socket,time
#对应的客户端程序
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#建立连接
s.connect(('192.168.0.100',1985))
#接受欢迎信息
print(s.recv(1024).decode('utf-8'))

while True:
    data = input('输入人名：')
    if data == 'exist':
        break
    
    s.send(data.encode('utf-8'))
    print(s.recv(1024).decode('utf-8'))
s.send(b'exsit')
s.close()