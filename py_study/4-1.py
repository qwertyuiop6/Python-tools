a=input('输入字符串')
b=''.join(a[i] for i in range(len(a)) if i%2==0)
print('偶数项:'+b)
c=''.join(a[i] for i in range(len(a)) if i%2==1)
print('奇数项:'+c)
print('连接奇数 偶数项：'+b+c)


    