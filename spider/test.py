import requests
import bs4
header={

    # 'X-Requested-With':'XMLHttpRequest',
    # 'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8',
    # "Connection": "keep-alive",
    # 'Cookie':'UM_distinctid=1622ea820465b3-07c78d5cae8b82-b353461-1fa400-1622ea8204a846; CNZZDATA3866066=cnzz_eid%3D1659038682-1494676185-https%253A%252F%252Fwww.google.com%252F%26ntime%3D1494676185; bdshare_firstime=1521201193282; G_WPT_TO=zh; SL_GWPT_Show_Hide_tmp=1; Hm_lvt_9a737a8572f89206db6e9c301695b55a=1521201193,1522681903,1522681936; Hm_lpvt_9a737a8572f89206db6e9c301695b55a=1522685327'
    # ,
    'Connection': 'keep-alive',
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
}
url='http://www.meizitu.com/a/5584.html'
r = requests.get(url,headers=header)
#print(r.text)
soup = bs4.BeautifulSoup(r.text, 'lxml')
print(soup)