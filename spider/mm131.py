#coding:utf-8
import requests
import bs4
import time
header={

    # 'X-Requested-With':'XMLHttpRequest',
    # 'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8'
    # ,
    # "Connection": "keep-alive",
    'Cookie':'UM_distinctid=1622ea820465b3-07c78d5cae8b82-b353461-1fa400-1622ea8204a846; CNZZDATA3866066=cnzz_eid%3D1659038682-1494676185-https%253A%252F%252Fwww.google.com%252F%26ntime%3D1494676185; bdshare_firstime=1521201193282; G_WPT_TO=zh; SL_GWPT_Show_Hide_tmp=1; Hm_lvt_9a737a8572f89206db6e9c301695b55a=1521201193,1522681903,1522681936; Hm_lpvt_9a737a8572f89206db6e9c301695b55a=1522685327'
    ,
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
}
header2={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,ja;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': '__jsluid=89194de7a6ae2d48a429812e4ef31596; G_WPT_TO=zh; SL_GWPT_Show_Hide_tmp=1',
    'Host': 'mm.chinasareview.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}

def get_mm(type,number):
    try:
    
        url='http://www.mm131.com/'+type
        r = requests.get(url,headers=header)
        #r.encoding='gb2312'
        make(r.content,number)
    except:
        return '出现异常，未执行爬取！'

def make(text,number):
    soup = bs4.BeautifulSoup(text, 'lxml') #查询首页内容
    #print(soup) 
    list1=soup.find_all('dd')  #将列表存为list
    #print(list1)
    if list1!=[]:
        print('找到啦(๑＞ڡ＜)✿ ~')
    else:
        print('没有?')
    
    m=0
    while m<number:    #循环处理列表各项
        img_src=list1[m].a.img['src']
        img_alt=list1[m].a.img['alt']
        #r2= requests.get(host+fancybox,headers=header)  #ajax请求列表各服务器详情
        #soup2=bs4.BeautifulSoup(r2.text, 'lxml')
        print('第',m,'发现链接',img_src,'!','开始下载：',img_alt)
        save_img(img_src)
        print('下载成功~')
        m+=1

def save_img(src):
    img=requests.get(src,headers=header2)
    t = int(round(time.time() * 1000))
    filename = '%s.jpg' % (t)
    with open('D:/my-python/spider/mm/'+filename, 'wb') as f:
        f.write(img.content)
    
# def get_info(m,tr,soup2):
#     td=tr[m].find_all('td')
#     server=td[1].string #服务器名称
#     #season=td[5].string #季节
#     #print(server)
#     tr3=soup2.table.find_all('tr')
#     day=tr3[5].td.h2.string   #天数
#     day=day[4:]+'天' 
#     #print(day)
#     number=tr3[2].td.h2.string    #人员
#     number=number[:-7]+'人' 
#     #print(number)
#     season=tr3[4].td.h2.string    #季节

#     tr2=soup2.find_all('table')[2].find_all('tr') #玩家列表
#     people=''
#     if len(tr2)== 1 and tr2[0].find('td')==None:
#         people='没人快来玩啊~( • ̀ω•́ )✧`\n'
#     else:
#         a=0
#         while a<len(tr2):
#             td2=tr2[a].find_all('td')
#             b=0
#             while b<len(td2):
#                 if b%2:
#                     pass
#                 else:
#                     player=td2[b].a.string
#                     jiaose=td2[b].span.a.string
#                     people+=player+':'+jiaose+'\n'
#                 b+=1
#             a+=1
#     All=server+':'+day+' '+season+','+number+'\n'+people
#     return All   

get_mm('xinggan',5)



if __name__ == '__main__':
   print('程序运行中')
else:
   print('另一模块')