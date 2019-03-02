addresses = []
def save_infor(name,gender,age,tels,addrs,city='天津',des='这个家伙很懒。。。'):
    addresses.append({'name':name,'age':age,'gender':gender,'tels':tels,'addrs':addrs})
def input_int():
    indexstr = input('请输入联系人序号：')
    if indexstr.isdigit() and int(indexstr) >= 0 and int(indexstr) < len(addresses):
        return int(indexstr)
    else:
        return None
def view_address():
    index = input_int()
    if index != None:
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
        print('城市')
        print('---------------------')
        print('******信息显示完成******')
    else:
        print('请输入一个正确的序号')
    #查看联系人
def new_address():
    #新建联系人
    name = input('你的名字：')
    age = input('你的年龄：')
    gender = input('你的性别：')
    city = input('你所在的城市')
    des = input('简介')

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
    if des == ' ' and city == ' ':
        save_infor(name,gender,age,tels,addrs)
    elif city != ' ' and des == ' ':    
        save_infor(name,gender,age,tels,addrs,city) 
    elif des != ' ' and city == ' ':
        save_infor(name,gender,age,tels,addrs,city,des=des)
    else:
        save_infor(name,gender,age,tels,addrs)
    print('******%s的信息录入完成******' % name)
def list_address():
    i = 0
    for person in addresses:
        print(i,person['name'])
        i += 1
    print('******信息列出完成******')
    #列出所有联系人
def delete_address():
    index = input_int()
    if index != None:
        p = addresses.pop(index)
        print('******%s的信息删除完成******' % p['name'])
    else:
        print('请输入一个正确的序号')
    #删除联系人
####################################################################
while True:
    cmd = input('请输入你的命令（n:新建，l:列出，v:详细，d:删除，q:退出）:')
    if cmd == 'n':
        new_address()
    elif cmd == 'l':
        list_address()
    elif cmd == 'v':
        view_address()
    elif cmd == 'd':
        delete_address()
    elif cmd == 'q':
        break
        #退出程序
    else:
        print('***请输入正确的命令***')