list1=list(input('请输入奇数个整数:').split())
m=True
while max(list1)!=min(list1):
    if m:
        list1.remove(max(list1))
        m=False
    else:
        list1.remove(min(list1))
        m=True
print('中数是',list1[0])