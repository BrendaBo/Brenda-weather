a = b = 1

numstr = input( '请输入数列个数:')
if numstr.isdigit():
    num = int(numstr)
    #for i in range(num):
    #    print(a)
    #    a,b = b,a + b
    
    t = a + b
    a = b
    b = a + b
    print(t)        
      
