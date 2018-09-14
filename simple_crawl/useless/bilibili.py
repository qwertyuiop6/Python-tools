import requests
from lxml import etree

header1={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
    ,'Connection':'keep-alive'
    ,'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
    ,'Cookie':'sid=jcmcca8h; buvid3=EAC52A7D-83F7-4C30-95F4-59D9909FF91342414infoc; UM_distinctid=160726f6685d7-0d6c56f0f2f65b-e323462-1fa400-160726f668629e; pgv_pvi=6255271936; fts=1513748393; rpdid=kspliqqmxidosokmmmiww; LIVE_BUVID=dc59e95acc7b54da7f53319fd5b4f34f; LIVE_BUVID__ckMd5=d0018701445aa5e7; im_notify_type_26236093=0; finger=edc6ecda; CURRENT_QUALITY=80; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1523790693; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; CNZZDATA2724999=cnzz_eid%3D2115956354-1522332512-https%253A%252F%252Fwww.bilibili.com%252F%26ntime%3D1524489258'
    ,'Host': 'space.bilibili.com'
}
header2={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'http://space.bilibili.com/45388',
    'Origin': 'http://space.bilibili.com',
    'Host': 'space.bilibili.com',
    'AlexaToolbar-ALX_NS_PH': 'AlexaToolbar/alx-4.0',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4',
    'Accept': 'application/json, text/javascript, */*; q=0.01'
}
url='https://space.bilibili.com/'

def get_user(s):
    res=requests.get(url+str(s),headers=header1).text
    print(res)
    


if __name__=='__main__':
    start,howmany=map(int,input('输入起始用户UID和抓取个数:').split())
    while howmany:
        get_user(start)
        start+=1
        howmany-=1
    print('完毕!')