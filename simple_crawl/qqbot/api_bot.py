import requests

api_url='http://api.qingyunke.com/api.php?key=free&appid=0&msg='

def tq(word):
    try:
        res1=requests.get(api_url+'天气'+word).json().get('content')
        res1=res1.replace('{br}','\n')
        print(res1)
        return res1
    except requests.ConnectionError as e:
        print('Error', e.args)
        return '请求错误'
    except:
        print('查询出现错误啦~')
        return '查询出现错误啦~'
        
def api_search(word):
    try:
        res1=requests.get(api_url+word).json().get('content')
        print(res1)
        return res1
    except requests.ConnectionError as e:
        print('Error', e.args)
        return '请求错误'
    except:
        print('查询出现错误啦~')
        return '查询出现错误啦~'


if __name__ == '__main__':
    api_search('你好')