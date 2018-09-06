import requests
import bs4
import time
header={

    # 'X-Requested-With':'XMLHttpRequest',
    # 'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8',
    # "Connection": "keep-alive",
    # 'Cookie':'UM_distinctid=1622ea820465b3-07c78d5cae8b82-b353461-1fa400-1622ea8204a846; CNZZDATA3866066=cnzz_eid%3D1659038682-1494676185-https%253A%252F%252Fwww.google.com%252F%26ntime%3D1494676185; bdshare_firstime=1521201193282; G_WPT_TO=zh; SL_GWPT_Show_Hide_tmp=1; Hm_lvt_9a737a8572f89206db6e9c301695b55a=1521201193,1522681903,1522681936; Hm_lpvt_9a737a8572f89206db6e9c301695b55a=1522685327'
    # ,
    'Connection': 'keep-alive',
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
def get_page_links(number):
    try:
        x=1
        while number>39:
            x=int(number/39)+1
            url='http://www.meizitu.com/a/sexy_'+str(x)+'.html'
            r = requests.get(url,headers=header)
            print('开始爬取第',x,'页')
            make(r.content,number%39,x)
            number-=39
        url='http://www.meizitu.com/a/sexy_'+str(x)+'.html'
        r = requests.get(url,headers=header)
        print('开始爬取第1页')
        make(r.content,number%39,1)
    except:
        return '出现异常，未执行爬取！'

def make(text,number,x):
    soup = bs4.BeautifulSoup(text, 'lxml') #查询首页内容
    #print(soup) 
    ul=soup.find_all('ul')  #将列表存为list
    # print(ul)
    list1=ul[1].find_all('a')
    #print(list1)
    if list1!=[]:
        print('找到啦(๑＞ڡ＜)✿ ~')
    else:
        print('???')
    
    m=0
    while m<(number*2):    #循环处理列表各项
            n=int(m/2+1)
            page_src=list1[m]['href']
            if list1[m+1].find('b')==None:
                page_alt=list1[m+1].string
            else:
                page_alt=list1[m+1].b.string
            print('第',n,'组,发现链接:',page_src,',','标题：',page_alt)
            go_page(page_src,n,x)
            print('下载成功~')
            m+=2

def go_page(page_src,n,x):
    r = requests.get(page_src,headers=header)
    soup = bs4.BeautifulSoup(r.text, 'lxml')
    #print(soup)
    pp=soup.find_all('p')
    img=pp[2].find_all('img')
    m=0
    while m<len(img):
        img_src=img[m]['src']
        print('开始下载',img_src)
        save_img(img_src,m+1,n,x)
        print('下载',img_src,'第',m+1,'张完毕~')
        m+=1

def save_img(src,m,n,x):
    img=requests.get(src,headers=header2).content
    t = int(round(time.time() * 1000))
    filename = '%s-%s-%s.jpg' % (x,n,m)
    with open('/Users/shadow/My-Python/spider/meizitu/'+filename, 'wb') as f:
        f.write(img)


if __name__ == '__main__':
    number = int(input('请输入需要爬取的组数：'))
    get_page_links(number)
        