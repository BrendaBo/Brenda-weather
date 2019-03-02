adresswss = []
while True:
    cmd = input('输入你的命令 （n:新建. l:列出. v:详细. d:删除. q:退出) :')
    if cmd == 'n':
        #新建联系人
        name = input('你的名字')
        age = input('你的年龄')
        gender = input('你的性别')
        tels = []
        while True:
            tel = input('输入你的电话 (输入\'end\'结束):')
            if tel == 'end':
                break
            tels.append(tel)
###############################################################################
        addrs = []
        while True:
            addr = input('请输入你的地址 (输入\'end\'结束 ) :')
            if addr == 'end':
                break
            adress.append(addr)
            
        addresses.append(['name': name, 'age':age, 'gender':gender, 'tels';tels])
    elif cmd == 'l':
        i = 0


        for person in adresses:
            print(person)
        print(addresses)
        for person in adresses:
            print(person['name']=':')
            print('年龄:'+person['age'])
            print('性别:'+person['gender'])
            print('电话:')
            for tel in person ['tels']:
                print(tels)
            print('地址:')
            for addr in person['addrs']:
                print(addr)
        #列出所有联系人
    elif cmd == 'v':
        pass
        #查看联系人
    elif cmd == 'd':
        pass
        #删除联系人
    elif cmd =='q':
        break

