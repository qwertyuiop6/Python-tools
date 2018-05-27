students={}
i=1
while i<6:
    num,name=map(str,input('输入学号 姓名:').split())
    students[num]=name
    i+=1
print(sorted(students.keys()))
print(students)