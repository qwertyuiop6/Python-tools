def reversal(data):
	y=1	
	for i in data:
		if i==',':
			y+=1
	print('this file have',y,'key-value')
	m=1
	a=''
	b=''
	res=''
	while m<=y:
		n=9*m-8
		a=data[n:n+2]
		#data[m:3*m]=data[6*m:7*m]
		b=data[n+5:n+6]
		if m!=64:
			res+='\''+b+'\':\''+a+'\','
		else:
			res+='\''+b+'\':\''+a+'\''
		m+=1
	print(res)
	return res


with open('D:/my-python/Tools/xxcode.txt','r') as x:
	with open('D:/my-python/Tools/yycode.txt','w') as y:
		y.write(reversal(x.read()))