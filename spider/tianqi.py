import requests

url='https://www.sojson.com/open/api/weather/json.shtml?city='

def tq(city='上海'):
    try:
        res=requests.get(url+city).json().get('data')
        info=res.get('forecast')
        for i in info:
            for key in i.keys():
                print(i[key])
    except requests.ConnectionError as e:
        print('Error', e.args)

if __name__ == '__main__':
    tq('阜阳')
    