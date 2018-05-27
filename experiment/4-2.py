a='abcdefg123456789'
def right(str):
    c=str[-1]
    i=1
    while i<len(str):
        c+=str[i-1]
        i+=1
    print(c)
def r2(str):
    c=str[-1]
    c+=''.join(str[i-1] for i in range(1,len(str)))
    print(c)
right(a)
r2(a)