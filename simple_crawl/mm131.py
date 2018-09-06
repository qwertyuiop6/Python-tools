import requests
import bs4
import time
import os
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

def set_header(referer):
    headers = {
        'Pragma': 'no-cache',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,ja;q=0.8,en;q=0.7',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'Referer': '{}'.format(referer),
    }
    return headers

def get_page_links(number,type):
    try:
        last_page=True
        while number>20:
            x=int(number/20)+1
            url='http://www.mm131.com/'+type+'/list_6_'+str(x)+'.html'
            r = requests.get(url,headers=header)
            print('开始爬取第',x,'页')
            if last_page==True:
                make(r.content,number%20,x)
                last_page=False
            else :
                make(r.content,20,x)
            number-=20
        
        url='http://www.mm131.com/'+type
        r = requests.get(url,headers=header)
        print('开始爬取第1页')
        if last_page==False:
            make(r.content,20,1)
        else:
            make(r.content,number,1)
    except:
        return '出现异常，未执行爬取！'


def make(text,number,x):
    soup = bs4.BeautifulSoup(text, 'lxml') #查询首页内容
    #print(soup)
    list1=soup.find_all('dd')
    #print(list1)
    if list1!=[]:
        print('找到啦(๑＞ڡ＜)✿ ~')
    else:
        print('???')
    
    m=0
    while m<number:    #循环处理列表各项
        page_src=list1[m].a['href']
        page_alt=list1[m].a.img['alt']
        print('第',m+1,'组,找到链接:',page_src,',','标题：',page_alt)
        go_page(page_src,m+1,page_alt)
        print('第',m+1,'组 '+page_alt+' 下载完毕~')
        m+=1    

def go_page(page_src,n,title):
    r = requests.get(page_src,headers=header)
    soup = bs4.BeautifulSoup(r.content, 'lxml')
    #print(soup)
    img_number=soup.select('.page-ch')[0].string[1:-1]
    img_dates=soup.select('.content-msg')[0].strings
    date=True
    img_date=''
    for i in img_dates:
        if date==True:
            print(i)
            img_date=i[10:15]
            date=False
    #print(img_date)
    print('第',n,'组发现',img_number,'张图')


    dirName = '[%s]%s (%s张)' % (img_date,title, img_number)
    fulldir='../../Download/mm131/'+dirName
    if os.path.exists(fulldir):
        print('已经下载过啦~')
        return
    else:
        os.mkdir(fulldir)

    m=0
    while m<int(img_number):
        
        img_src=soup.select('.content-pic')[0].a.img['src']
        if os.path.isfile(fulldir+'/'+str(m+1)+'.jpg'):
            print(dirName,'第',m+1,'张已存在')
            pass
        else:
            print('开始下载第',m+1,'张图:',img_src)
            save_img(img_src,m+1,fulldir)
            print('下载完毕~')
        page_src2=page_src[:-5]+'_'+str(m+2)+'.html'
        r2 = requests.get(page_src2,headers=header)
        soup = bs4.BeautifulSoup(r2.text, 'lxml')
        m+=1


def save_img(src,m,dirname):
    img=requests.get(src,headers=set_header(src)).content
    #t = int(round(time.time() * 1000))
    filename = '%s/%s.jpg' % (dirname, m)
    with open(filename, 'wb') as f:
        f.write(img)
    #time.sleep(0.5)




if __name__ == '__main__':
    number = int(input('输入要爬取的人数:'))
    get_page_links(number,'xinggan')