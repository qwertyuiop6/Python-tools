#coding:utf-8
import requests
import bs4
#import selenium
header={

    'X-Requested-With':'XMLHttpRequest',
    'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8',
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}
host='https://my.jacklul.com'
url='https://my.jacklul.com/dstservers/'
def search(word,what):
    try:
        pre={
            'search':word
        }
        #browser = webdriver.PhantomJS()
        r = requests.post(url,headers=header,data=pre)
        x=make(r.text,what)
        print(x)
        return x
    except:
        return '出BUG啦,什么都没找到??!Σ(っ°Д°;)っ'

def make(text,what):
    soup = bs4.BeautifulSoup(text, 'lxml') #查询首页内容
    #print(soup)
    list=soup.tbody   #找到列表
    tr=list.find_all('tr')  #将列表存为list
    if tr!=[]:
        dic='找到啦(๑＞ڡ＜)✿ ~ \n\n'
    else:
        dic='没有找到该服务器!Σ(っ°Д°;)っ'
    
    m=0
    while m<len(tr):    #循环处理列表各项
        fancybox=tr[m]['href']
        r2= requests.get(host+fancybox,headers=header)  #ajax请求列表各服务器详情
        soup2=bs4.BeautifulSoup(r2.text, 'lxml')
        #print(soup2)
        if what=='info':
            dic+=get_info(m,tr,soup2)
        # elif what=='people':
        #     dic+=s_people(m,tr,soup2)
        else:
            pass
        m+=1
    return dic

def get_info(m,tr,soup2):
    td=tr[m].find_all('td')
    server=td[1].string #服务器名称
    #season=td[5].string #季节
    #print(server)
    tr3=soup2.table.find_all('tr')
    day=tr3[5].td.h2.string   #天数
    day=day[4:]+'天' 
    #print(day)
    number=tr3[2].td.h2.string    #人员
    number=number[:-7]+'人' 
    #print(number)
    season=tr3[4].td.h2.string    #季节

    tr2=soup2.find_all('table')[2].find_all('tr') #玩家列表
    people=''
    if len(tr2)== 1 and tr2[0].find('td')==None:
        people='没人快来玩啊~( • ̀ω•́ )✧`\n'
    else:
        a=0
        while a<len(tr2):
            td2=tr2[a].find_all('td')
            b=0
            while b<len(td2):
                if b%2:
                    pass
                else:
                    player=td2[b].a.string
                    jiaose=td2[b].span.a.string
                    people+=player+':'+jiaose+'\n'
                b+=1
            a+=1
    All=server+':'+day+' '+season+','+number+'\n'+people
    return All   

search('哲学','info')
#con_server('查询服务器哲学')



if __name__ == '__main__':
   print('程序运行中')
else:
   print('另一模块')