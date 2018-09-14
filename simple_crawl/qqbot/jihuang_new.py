
import requests
import bs4

#import selenium

header={
    'Host': 'dstserverlist.appspot.com',
    'Referer': 'https://dstserverlist.appspot.com/',
    # ':scheme:':'https',
    'content-type':'application/json; charset=utf-8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3487.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    # 'Cookie':'_ga=GA1.3.1057087402.1526651393; cookieconsent_status=dismiss; SID=97ae40c3a64a978f6db434846d04778f; _gid=GA1.3.1521506748.1531381891; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1'
}

zhexue=['tvpFav0J1j6whczo1aOiasp4lOLqSZ2xh6rxAvXzifc%3D','Y8d2uZ5L1X5qJJWZRVdW82K0cdhIS%2FK4fyMLb%2BJV3oU%3D','%2FX6G6lBDddZ1NRH7oU8RKAnmZQD2uPzz%2FX414bxAA4ad6CQtJxsO7A%3D%3D']

url1="https://dstserverlist.appspot.com/ajax/query"


def search(server='哲学'):
    
    try:
        if ~server.find('哲学'):
            return s2(zhexue)
        else:
            res1 = requests.get(url1,headers=header).json().get('result')
            print(res1)
            url2="https://dstserverlist.appspot.com/ajax/list?"+str(res1)
            # res2 = requests.get(url2,headers=header).json().get('result').encode('gb2312','ignore').decode('gb2312')
            res2 = requests.get(url2,headers=header).json().get('result')
            # 得到最新服务器列表

            soup=bs4.BeautifulSoup(res2,'lxml')
            #bs处理

            name_list=soup.tbody.select('.name')
            #筛选处服务器名称列表
            
            s_l=[]
            #待查询服务器ID列表

            #循环匹配查找目标Id
            for i in name_list:
                if len(i.contents)==2:
                    x=i.contents[1].encode('gb2312','ignore').decode('gb2312')
                    if ~x.find(server):
                        s_l.append(i.parent['id'])
            
            #查询列表中的服务器
            xxx=s2(s_l)
            return xxx

        # print(name.encode('gb2312','ignore').decode('gb2312'))
        # print(res2.encode('gb2312','ignore').decode('gb2312'))
       
    except requests.ConnectionError as e:
        print('Error', e.args)
        return '查询失败'

def s2(list):
    print(list)
    try:
        res=''
        for i in list:
            url3="https://dstserverlist.appspot.com/ajax/status/"+i
            if requests.get(url3,headers=header).json().get('ok'):
                
                res3 = requests.get(url3,headers=header).json().get('result')
                
                soup3=bs4.BeautifulSoup(res3,'lxml')
                
                s_name=soup3.select('.server-name')[0].string.encode('gb2312','ignore').decode('gb2312')
                
                season_l=soup3.tbody.find_all('tr')
                
                season=season_l[2].td.string.encode('gb2312','ignore').decode('gb2312').lstrip()
                
                nums=soup3.select('a[href="#players"]')[0].string.encode('gb2312','ignore').decode('gb2312')
                # print(soup3.select('.row')[0])
                player='Nobody'
                if soup3.select('.row')[0]!=None:
                    player=''
                    player_l=soup3.select('.row')[0].find_all('a')
                    
                    for i in player_l:
                        x=i.string.encode('gb2312','ignore').decode('gb2312')
                        y=i.next_sibling.lstrip().encode('gb2312','ignore').decode('gb2312')
                        z=x+':'+y+'\n'
                        player+=z
                    
                sss='★ '+s_name+'\n☞ '+nums+'\n# '+season+'\n'+player+'\n'
                
                res+=sss
        return res    
            
    except:
        return '没有找到该服务器!'

if __name__ == '__main__':
    print(search("啦啦啦"))