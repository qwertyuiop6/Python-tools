#-*— coding:UTF-8 -*-
from bs4 import BeautifulSoup #导入BeautifulSoup模块
import requests  #导入requests网页请求模块
initUrl = 'https://movie.douban.com'   #豆瓣网网址
urls = 'https://movie.douban.com/tag/#!/i!/ckDefault'  #豆瓣网所有电影的分类网址
#获得电影的分类信息，以便下一步从分类信息中分类的爬取网页
requests.adapters.DEFAULT_RETRIES = 5
url2='https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start=0'
header={
    # 'Connection': 'close',
    # 'X-Requested-With':'XMLHttpRequest',
    'Host': 'movie.douban.com',
    'Referer': 'https://movie.douban.com/tag',
    'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8',
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}
def requreMovieLable(url = urls):
    data = []
    web_data = requests.get(url,headers=header) #根据网页链接获取网页源代码
    soup = BeautifulSoup(web_data.text,'lxml') #网页预处理
    print(soup)
    cataLog = soup.tbody.find_all('a')  #获取html源代码中含有<a><\a>标签中的内容
    for item in cataLog:
        data.append(initUrl + item.get('href'))     #提取<a><\a>标签中的网页链接
        # print data
    print(data)
    return data #以列表形式返回各个电影标签的网页链接，例如data[0]中包含‘爱情’分类的电影，data[1]中包含‘喜剧’分类的电影，等等
#爬取该网页的电影名称、评分、评论人数等信息

def requreMovieLable2(url = urls):
    mvurl = []
    web_data = requests.get(url2+'&genres=科幻').json() #根据网页链接获取网页源代码
    data=web_data.get('data')
    
    for item in data:
        mvurl.append(item.get('url'))     #提取<a><\a>标签中的网页链接
        # print data
    print(mvurl)
    return data

def parsMovie(url = urls):
    web_data = requests.get(url,headers=header)     #根据网页链接获取网页源代码
    soup = BeautifulSoup(web_data.text,'lxml') #网页预处理
    movieNamePre = soup.find_all(class_="nbg") #寻找网页源代码中含有属性值为‘class_="nbg"’的特定标签
    movieValueAndNumPre = soup.find_all(class_='star clearfix')  #寻找网页源代码中含有属性值为‘class_='star clearfix'’的特定标签
    movieValue = []     #存储电影的评分值
    movieNum = []       #存储特定电影的评论人数
    for item in movieValueAndNumPre:
        movieValue.append(item.span.next_sibling.next_sibling.text)  #存储电影的评分
        movieNum.append(item.span.next_sibling.next_sibling.next_sibling.next_sibling.text)    #存储电影的评论数
    # print movieValueAndNum
    movieName = []   #存储电影的名字信息
    for item in movieNamePre:
        movieName.append(item.get('title'))   #解析获取源代码中的电影名称
    u = zip(movieName,movieValue,movieNum)    #将电影名、电影评分、评论人数zip成一个元组
    #输出解析出的结果信息
    for name ,val ,num in u:
        print (name)
        print (val)
        print (num)
        print ('----' * 10)
ul = requreMovieLable2(urls)     #获取主页面各个电影分类的url地址存取在列表中
page = 3        #设置下载网页列表的个数
firstUl = ul[0]  #爬取‘爱情’分类下的所有电影
for i in range(0,page):
    print (*'----------------第%d页的电影---------------' % i)
    parsMovie(firstUl + '?start={}&type=T'.format(str(i*20)))
