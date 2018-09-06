import os
def tras(ini):
	a=1
	b=''
	res=''
	for i in ini:
		if a%2:
			b+=i
		else:
			b+=i
			if tras2(b)=='**':
				print(b,end='')
				res+=b
			else:
				print(tras2(b),end='')
				res+=tras2(b)
			b=''
		a+=1
	return res

def tras2(twochar):
	return{
		'00':'y','01':'x','03':'z','08':'q','09':'p','0A':'s','0B':'r','0C':'u','0D':'t','0E':'w',
		'0F':'v','10':'i','11':'h','12':'k','13':'j','14':'m','15':'l','16':'o','17':'n','57':'.',
		'18':'a','1A':'c','1B':'b','1C':'e','1D':'d','1E':'g','1F':'f','20':'Y','21':'X','23':'Z','28':'Q','29':'P','2A':'S',
		'2B':'R','2C':'U','2D':'T','2E':'W','2F':'V','30':'I','31':'H','32':'K','33':'J','34':'M','35':'L','36':'O','37':'N',
		'38':'A','3A':'C','3B':'B','3C':'E','3D':'D','3E':'G','3F':'F','40':'9','41':'8','44':'=','48':'1','49':'0','4A':'3',
		'4B':'2','4C':'5','4D':'4','4E':'7','4F':'6'
	}.get(twochar,'**')

u1='%s/UserCustom.ini'%(os.path.abspath('ini'))
u2='%s/UserCustom2.ini'%(os.path.abspath('ini'))
with open(u1,'r') as f:
	with open(u2,'w') as r:
		r.write(tras(f.read()))

	
