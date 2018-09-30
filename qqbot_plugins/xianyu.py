import requests
from lxml import etree

def search(item, p1, p2):
    url="https://s.2.taobao.com/list/list.htm?start="+str(p1)+"&end="+str(p2)+\
    "&cpp=true&st_trust=1&ist=1&userId=0&q="+item
    web_data=requests.get(url).text
    html=etree.HTML(web_data)
    
    price_l=list(set(html.xpath('//span[@class="price"]/em/text()')))
    title_l=list(set(html.xpath('//div[@class="item-brief-desc"]/text()')))
    nick_l=list(set(html.xpath('//div[@class="seller-nick"]/a/text()')))
    vip_l=list(set(html.xpath('//div[@class="seller-icons"]/span/@title')))
    link_l=list(set(html.xpath('//div[@class="item-pic"]/a/@href')))

    res=''
    limit=6
    for i in range(limit-1):
        res+='★ '+nick_l[i]+'('+vip_l[i]+')'+':'+title_l[i]+'\n'+'¥'+\
        price_l[i]+','+'链接:https:'+link_l[i]+'\n'
    print(res)
    return res

    

if __name__ == '__main__':
    search("ipad",1500,2500)