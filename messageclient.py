import socket,time,threading
#对应的客户端程序
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
all_user = []
# 建立连接:
s.connect(('192.168.0.109', 1986))
def recvdata(s):
    buffer = []
    while True:
        d = s.recv(1)
        if not d or d != b'\n' :
            buffer.append(d)
        else:
            break
    return  b''.join(buffer)
def recvmessge(s):
    global all_user
    while True:
        time.sleep(2)
        data = recvdata(s).decode('utf-8')
        if data.find('-') != -1:
            n,mess = data.split('-',2)
            print('\n------------------\n来自%s的消息：%s\n------------------' % (n,mess))
        else:
            all_user = data.split(':')
if recvdata(s).decode('utf-8') == 'this a message server':
    t = threading.Thread(target=recvmessge, args=(s,))
    t.start()
    nickname = input('输入昵称：')
    if nickname != '':
        data = ('0:%s:none\n' % nickname).encode('utf-8')
        s.send(data)
        while True:
            cmd = input('请输入命令（l:查看用户列表,s:发送信息,q:退出,v:读取消息）：')
            if cmd == 'q':
                s.send(b'3:exit:exit\n')
                break
            elif cmd == 'l':
                i = 1
                for name in all_user:
                    print(i,name)
                    i += 1
            elif cmd == 's':
                index = input('请输入收件人序号：')
                message = input('请输入短消息：')
                data = '2:%s:%s\n' % (all_user[int(index)-1],message)
                s.send(data.encode('utf-8'))
            # elif cmd == 'v':
            #     data = recvdata(s).decode('utf-8')
            #     if data.find('-') != -1:
            #         n,mess = data.split('-',2)
            #         print(n,mess)
            else:
                print('请输入正确的命令')
    else:
        print('请连接正确的服务器1')
else:
    print('请连接正确的服务器')
s.close()