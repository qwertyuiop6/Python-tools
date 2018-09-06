import bs4
import requests
import base64
import re

from fontTools import ttLib, unicode

header={

    # 'X-Requested-With':'XMLHttpRequest',
    # 'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8'
    # ,
    # "Connection": "keep-alive",
    'Cookie':'UM_distinctid=1622ea820465b3-07c78d5cae8b82-b353461-1fa400-1622ea8204a846; CNZZDATA3866066=cnzz_eid%3D1659038682-1494676185-https%253A%252F%252Fwww.google.com%252F%26ntime%3D1494676185; bdshare_firstime=1521201193282; G_WPT_TO=zh; SL_GWPT_Show_Hide_tmp=1; Hm_lvt_9a737a8572f89206db6e9c301695b55a=1521201193,1522681903,1522681936; Hm_lpvt_9a737a8572f89206db6e9c301695b55a=1522685327'
    ,
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
}

url='https://piaofang.maoyan.com/?ver=normal'

r = requests.get(url,headers=header)

# 找寻加密base64字符串,并解密存为ttf
font = re.findall("url\(data:application/font-woff;charset=utf-8;base64,(.*?)\) format",r.text)[0]
# font="d09GRgABAAAAAAggAAsAAAAAC7gAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAABHU1VCAAABCAAAADMAAABCsP6z7U9TLzIAAAE8AAAARAAAAFZW7lTNY21hcAAAAYAAAAC8AAACTDXKnytnbHlmAAACPAAAA5EAAAQ0l9+jTWhlYWQAAAXQAAAALwAAADYR8c2oaGhlYQAABgAAAAAcAAAAJAeKAzlobXR4AAAGHAAAABIAAAAwGhwAAGxvY2EAAAYwAAAAGgAAABoGbgVSbWF4cAAABkwAAAAfAAAAIAEZADxuYW1lAAAGbAAAAVcAAAKFkAhoC3Bvc3QAAAfEAAAAWgAAAI/KSOKXeJxjYGRgYOBikGPQYWB0cfMJYeBgYGGAAJAMY05meiJQDMoDyrGAaQ4gZoOIAgCKIwNPAHicY2Bk0mWcwMDKwMHUyXSGgYGhH0IzvmYwYuRgYGBiYGVmwAoC0lxTGBwYKr6GMev812GIYdZhuAIUZgTJAQDdjgtdeJzFkr0NgzAQhZ/DTxKcImVGQCgFK9AyACMwAxNkggyCUmUSFnDjAuhck2cfTSRok7M+S/d8ujvdGUACICJ3EgPqDQVvL6oq6BGyoMd40L/hSuWEzmhT2srWdhiLqZ9bl7tmWRix/7Jlihm3jn/JkEKzbsJ6Rxxw9p2qdCfTD0z9r/S3XcL9XD1NuhW2aLTg92ZKgZOErQQfb2vB79wOgv8LYyFw4ph6gbPH3ArcAlwucB9wjYDoA1IaPZh4nD2Sz2/aZhyH39dUkBJCyLBxIS1gTGwDSXD8M4ADFAfa/GQkmBDS0hC1lGZrm0VNl7bR1tJtUjvtD+gulXrYpdqh906a1tPWacthf8CkXXdbpV4istdOUh9e+X2lV+/zeT5fAAE4/BcIAAcYAKpI4EGcA+gzz/+Dh9ifIIHOg1AUFIll6IhDJQVFltCf3cEqqiIKZBDidkcQEridjjBsd/CCkjXYmBaIOt2p1ZwiTjvrnlS6mhYmZGEid+FJ58re6V/nCrU9lnMuwMwUn8sWBhvJicCZ+vqcb/BS6fLjrYbJgIgO38EeYgiDUYTEWAB2hxsSWQTkI3A3RE/KkoXhIyFucSK6iB1+7yKiUjwcJ10D4TVxZS99tXDr6bz+maHIrt4ztsgolfLdKuaTyBEylDq3rEyMd9v6nannr/ebS/x4tfd21Eg0FmZWapaLd9gp7BcQ+uDiSICXIijHMYsDxWcZ9hvnjJKv1/SEji8X4dXeP2x4mm4+ShU/35jK9r0pFjae1ZiQE25Vf/aRj66vX1xRJhuWb7QcYm+AFwCvTBFuG0pKZ6GqqGhJwn1anxa9/r41OOQJZYJ5CrtlFKOtew/yjU/ibW33duoS88HZAXKGm7ReSTXxkBxEaJozGVXcJygelkEu4/5AZ3E7c9bjcbmHr5Wva6VG5f5ynHsQHYOt7uxidS2e127m2uzi8mz97as7O3A9kxYLJ7w76B0XABQ95IYO2SIV4U493OFmJoe5/hTGBzWPERH8PHnEhu4cYL8DJxhAt2RKhuKQSNAEO2SDeu83WLrYatX/flmB+z2+8vIAnf2Ertgs/+A40xhKhTpXLOfW2KFIaI9SiYKqmOXbcJQXtXS0e/Xp1uvtzUKx+9f5fIkvSDxN6e3zZyMjkVhYJGLVLyrwK27z4xu35zuc70rh8l5Wa5WaP0i5cKip53tP2CLuJXD24VIFnOR+j1iiAIwQFPJrM2OfTEQWCsemHahB+L7H9juHuRSTLhOxOS03Dxund//YpRK4znMC+VFftRoK+pNJOczPnpu8NjNbcrZvbBtjCwKZ46ixM+TASadWfhokjycQPZmFU1Bi7ebcmflFwZRx1DALLRwCJ1HT3/ZrfDzDuu0O6E+Oqqv3v9yY3tEyd8uGpDhhZ2kyU4vF75V/1OSRrBxQhvtO2eOBwMPNm1/Pfdd9+sIYTxowM7/aXCzFEisI53+i0+DCAAAAeJxjYGRgYADiDlODx/H8Nl8ZuFkYQOB6pssPBP3/DQsD03kgl4OBCSQKADRdC0MAeJxjYGRgYNb5r8MQw8IAAkCSkQEV8AAAM2IBzXicY2EAghQGBiYd4jAAN4wCNQAAAAAAAAAMAE4AkgDEAOgBHAE2AVIBmAHSAhoAAHicY2BkYGDgYTBgYGYAASYg5gJCBob/YD4DAA6DAVYAeJxlkbtuwkAURMc88gApQomUJoq0TdIQzEOpUDokKCNR0BuzBiO/tF6QSJcPyHflE9Klyyekz2CuG8cr7547M3d9JQO4xjccnJ57vid2cMHqxDWc40G4Tv1JuEF+Fm6ijRfhM+oz4Ra6eBVu4wZvvMFpXLIa40PYQQefwjVc4Uu4Tv1HuEH+FW7i1mkKn6Hj3Am3sHC6wm08Ou8tpSZGe1av1PKggjSxPd8zJtSGTuinyVGa6/Uu8kxZludCmzxMEzV0B6U004k25W35fj2yNlCBSWM1paujKFWZSbfat+7G2mzc7weiu34aczzFNYGBhgfLfcV6iQP3ACkSaj349AxXSN9IT0j16JepOb01doiKbNWt1ovippz6sVYYwsXgX2rGVFIkq7Pl2PNrI6qW6eOshj0xaSq9mpNEZIWs8LZUfOouNkVXxp/d5woqebeYIf4D2J1ywQB4nG3LOw6AIBAE0B1/KOJdEIXQguBdbOxMPL6RtXSal8nuUEUcSf9RqFCjQYsOAj0GSIxQmAi3uM4jZ+ded2uL2a+BTdyXRRdTZDcT+N94vuv47WaiBxwQF30AAA=="
fontdata=base64.b64decode(font)
# print(fontdata)  
file=open('1.ttf','wb')  
file.write(fontdata)  
file.close() 

# 处理字体文件字符集unicode映射关系
tt = ttLib.TTFont("1.ttf")
print(tt.getGlyphOrder())
glyphs = tt.getGlyphOrder()[2:]
tmp_dic = {}
for num,un_size in enumerate(glyphs): 
    print(un_size,num) 
    font_uni = un_size.replace('uni','0x').lower() 
    tmp_dic[font_uni] = num 
print(tmp_dic)

# 替换原先加密字符为正常数字
s=r.text.replace('&#','0')
for key in tmp_dic:
    key2=key+';'
    s=s.replace(key2,str(tmp_dic[key]))
# print(s)

# 解析解密后的html
soup = bs4.BeautifulSoup(s, 'lxml')
# print(soup.style)


now_piaofang=soup.select('.c2 .cs')
print(now_piaofang)
print(now_piaofang[0])
# now_piaofang[0].replace('&#','0')


