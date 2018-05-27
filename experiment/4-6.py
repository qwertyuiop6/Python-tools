str=input('输入字符串:').lower()
dic={}
for i in str:
    dic[i]=str.count(i)
print(dic)
