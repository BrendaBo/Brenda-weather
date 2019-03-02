addresses = [] 
while True:
    cmd = input('请输入你的命令（n:新建，l:列出，v:详细，d:删除，q:退出）:')
    if cmd == 'n':
        #新建联系人
        name = input('你的名字：')
        age = input('你的年龄：')
        gender = input('你的性别：')
        ####################################################
        tels = []
        while True:
            tel = input('请输入你的电话（输入\'end\'结束）:')
            if tel == 'end':
                break
            tels.append(tel)
        ###################################################
        addrs = []
        while True:
            addr = input('请输入你的地址（输入\'end\'结束）:')
            if addr == 'end':
                break
            addrs.append(addr)
        ###################################################
        addresses.append({'name':name,'age':age,'gender':gender,'tels':tels,'addrs':addrs})
        print('******%s的信息录入完成******' % name)
    elif cmd == 'l':
        # print(addresses)
        i = 0
        for person in addresses:
            print(i,person['name'])
            i += 1
        print('******信息列出完成******')
        #列出所有联系人
    elif cmd == 'v':
        indexstr = input('请输入要查询的联系人序号：')
        if indexstr.isdigit():
            index = int(indexstr)
            if index >= 0 and index < len(addresses):
                person = addresses[index]
                print(person['name']+':')
                print('---------------------')
                print('年龄:'+person['age'])
                print('性别:'+person['gender'])
                print('电话:')
                for tel in person['tels']:
                    print('\t'+tel)
                print('地址:')
                for addr in person['addrs']:
                    print('\t'+addr)
                print('---------------------')
                print('******信息显示完成******')
        else:
            print('请输入一个正确的序号')
        #查看联系人
    elif cmd == 'd':
        indexstr = input('请输入要删除的联系人序号：')
        if indexstr.isdigit():
            index = int(indexstr)
            if index >= 0 and index < len(addresses):
                p = addresses.pop(index)
                print('******%s的信息删除完成******' % p['name'])
        #删除联系人
    elif cmd == 'q':
        break
        #退出程序
    else:
        print('***请输入正确的命令***')