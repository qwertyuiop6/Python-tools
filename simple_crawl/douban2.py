import requests

url='https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start=0'

def geturl(mvtype='科幻'):
    mvurl=[]
    web_data = requests.get(url+'&genres='+mvtype).json()
    data=web_data.get('data')
    print(data)

    for item in data:
        mvurl.append(item.get('url'))
    print(mvurl)
    return mvurl
    

if __name__ == '__main__':
    geturl()
    