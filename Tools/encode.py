def tras(ini):
	res=''
	m=1
	for i in ini:
		if i=='[':
			res=ini
			print(ini,end='')
			break
		elif (m<=7) or (i=='\n'):
			print(i,end='')
			res+=i
		else:
			print(tras2(i),end='')
			res+=tras2(i)
		m+=1	
	return res

def tras2(char):
	return{
		'y':'00','x':'01','z':'03','q':'08','p':'09','s':'0A','r':'0B','u':'0C','t':'0D','w':'0E',
		'v':'0F','i':'10','h':'11','k':'12','j':'13','m':'14','l':'15','o':'16','n':'17','.':'57',
		'a':'18','c':'1A','b':'1B','e':'1C','d':'1D','g':'1E','f':'1F','Y':'20','X':'21','Z':'23',
		'Q':'28','P':'29','S':'2A','R':'2B','U':'2C','T':'2D','W':'2E','V':'2F','I':'30','H':'31',
		'K':'32','J':'33','M':'34','L':'35','O':'36','N':'37','A':'38','C':'3A','B':'3B','E':'3C',
		'D':'3D','G':'3E','F':'3F','9':'40','8':'41','=':'44','1':'48','0':'49','3':'4A','2':'4B',
		'5':'4C','4':'4D','7':'4E','6':'4F'
	}.get(char,'*')


with open('D:/my-python/Tools/UserCustom2.ini','r') as f:
	with open('D:/my-python/Tools/UserCustom.ini','w') as r:
		for line in f.readlines():
			r.write(tras(line))
