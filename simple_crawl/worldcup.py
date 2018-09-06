import bs4
import requests

header={

    # 'X-Requested-With':'XMLHttpRequest',
    # 'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8'
    # ,
    # "Connection": "keep-alive",
    'Cookie':'UM_distinctid=1622ea820465b3-07c78d5cae8b82-b353461-1fa400-1622ea8204a846; CNZZDATA3866066=cnzz_eid%3D1659038682-1494676185-https%253A%252F%252Fwww.google.com%252F%26ntime%3D1494676185; bdshare_firstime=1521201193282; G_WPT_TO=zh; SL_GWPT_Show_Hide_tmp=1; Hm_lvt_9a737a8572f89206db6e9c301695b55a=1521201193,1522681903,1522681936; Hm_lpvt_9a737a8572f89206db6e9c301695b55a=1522685327'
    ,
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
}

url='http://tiyu.baidu.com/match/世界杯'

def search(se):
    
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.text, 'lxml')

    # 解析
    date=soup.select('.wa-match-schedule-list-title')
    vs=soup.select('.vs-line')
    coutry=soup.select('.wa-tiyu-schedule-item-name')
    time=soup.select('.status-text')
    date_i=[]
    vs_i=[]
    co_i=[]
    time_i=[]
    date2=['yest','tod','tom','tom1','tom2']

    for i in date:
        date_i.append(i.contents[1].rstrip())
    for i in vs:
        vs_i.append(i.string)
    for i in coutry:
        co_i.append(i.string)
    for i in time:
        time_i.append(i.string)

    def whowin(a,b,c):
        b1=int(b[0])
        b2=int(b[-1])
        if b1>b2:
            return a+'赢了!'
        elif b1==b2:
            return '平局'
        return c

    def isout(s,a,b,c):
        if s.find('回放')!=-1:
            return whowin(a,b,c)
        return s

    res={}
    i=0
    while i<5:
        res[date2[i]]=date_i[i]+'\n'+co_i[6*i]+vs_i[3*i]+co_i[6*i+1]+' '+isout(time_i[3*i],co_i[6*i],vs_i[3*i],co_i[6*i+1])+' \n'\
        +co_i[6*i+2]+vs_i[3*i+1]+co_i[6*i+3]+' '+isout(time_i[3*i+1],co_i[6*i+2],vs_i[3*i+1],co_i[6*i+3])+' \n'\
        +co_i[6*i+4]+vs_i[3*i+2]+co_i[6*i+5]+' '+isout(time_i[3*i+2],co_i[6*i+4],vs_i[3*i+2],co_i[6*i+5])+' \n\n'
        i+=1

    res2=''
    for v in sorted(res.values()):
        res2+=v
        
    # print(vs_i)
    # print(date_i)
    # print(co_i)
    # print(time_i)
    if se.startswith('明天'):
        return res['tom']
    elif se.startswith('今天'):
        return res['tod']
    elif se.startswith('昨天'):
        return res['yest']
    return res2

print(search('all'))
