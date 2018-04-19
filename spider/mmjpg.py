import requests
import bs4
import time
import os

header={

    # 'X-Requested-With':'XMLHttpRequest',
    # 'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8',
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
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}

def set_header(referer):
    headers = {
        'Pragma': 'no-cache',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'Referer': '{}'.format(referer),
    }
    return headers

def get_page_links(number):
    try:
        x=1
        y=1
        while number>15:
            x=int(number/15)+1
            url='http://www.mmjpg.com/home/'+str(x)
            r = requests.get(url,headers=header)
            print('开始爬取第',x,'页')
            if y==0:
                make(r.content,15,x)
            elif y==1:
                make(r.content,number%15,x)
                y=0
            number-=15
        url='http://www.mmjpg.com/'
        r = requests.get(url,headers=header)
        print('开始爬取第1页')
        if y==0:
                make(r.content,15,1)
        else:
            make(r.content,number,1)
    except:
        return '出现异常，未执行爬取！'

def make(text,number,x):
    soup = bs4.BeautifulSoup(text, 'lxml') #查询首页内容
    #print(soup)
    list1=soup.find_all('ul')[0].find_all(class_='title')
    print(list1)
    if list1!=[]:
        print('找到啦(๑＞ڡ＜)✿ ~')
    else:
        print('???')
    
    m=0
    while m<number:    #循环处理列表各项
        page_src=list1[m].a['href']
        page_alt=list1[m].a.string
        print('第',m+1,'组,找到链接:',page_src,',','标题：',page_alt)
        go_page(page_src,m+1,x,page_alt)
        print('第',m+1,'组下载成功~')
        m+=1    

def go_page(page_src,n,x,title):
    r = requests.get(page_src,headers=header)
    soup = bs4.BeautifulSoup(r.content, 'lxml')
    # print(soup)
    img_number=soup.select('#page')[0].find_all('a')[-2].string
    print('第',n,'组发现',img_number,'张图')
    dirName = '%s (%s张)' % (title, img_number)
    os.mkdir('./mmjpg/'+dirName)
    m=0
    while m<int(img_number):
        img_src=soup.select('#content')[0].a.img['data-img']
        print('开始下载第',m+1,'张图:',img_src)
        save_img(img_src,m+1,dirName)
        print('下载',img_src,'完毕~')
        page_src2=page_src+'/'+str(m+2)
        r2 = requests.get(page_src2,headers=header)
        soup = bs4.BeautifulSoup(r2.text, 'lxml')
        m+=1


def save_img(src,m,dirname):
    img=requests.get(src,headers=set_header(src)).content
    t = int(round(time.time() * 1000))
    filename = '%s/%s/%s.jpg' % (os.path.abspath('mmjpg'), dirname, m)
    with open(filename, 'wb') as f:
        f.write(img)
    #time.sleep(0.5)


if __name__ == '__main__':
    number = int(input('请输入需要爬取的人物数：'))
    get_page_links(number)
        