import os
import time
import requests

class maoyan():
    def __init__(self):
        self.headers = {
            'Host': 'piaofang.maoyan.com',
            'Referer': 'https://piaofang.maoyan.com/dashboard',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER',
            'X-Requested-With': 'XMLHttpRequest'
        }
    def get_page(self):
        url = 'https://box.maoyan.com/promovie/api/box/second.json'
        try:
            response = requests.get(url, self.headers)
            if response.status_code == 200:
                return response.json()
        except requests.ConnectionError as e:
            print('Error', e.args)
    def parse_page(self, json):
        if json:
            data = json.get('data')
            for index, item in enumerate(data.get('list')):
                self.piaofang = {}
                # 场均上座率
                self.piaofang['avgSeatView'] = item.get('avgSeatView')
                # 场均人次
                self.piaofang['avgShowView'] = item.get('avgShowView')
                # 平均票价
                self.piaofang['avgViewBox'] = item.get('avgViewBox')
                # 票房
                self.piaofang['boxInfo'] = item.get('boxInfo')
                # 票房占比
                self.piaofang['boxRate'] = item.get('boxRate')
                # 电影名称
                self.piaofang['movieName'] = item.get('movieName')
                # 上映天数
                self.piaofang['releaseInfo'] = item.get('releaseInfo')
                # 排片场次
                self.piaofang['showInfo'] = item.get('showInfo')
                # 排片占比
                self.piaofang['showRate'] = item.get('showRate')
                # 总票房
                self.piaofang['sumBoxInfo'] = item.get('sumBoxInfo')
                yield self.piaofang
if __name__ == "__main__":
    def pf(word):
        my = maoyan()
        json = my.get_page()
        results = my.parse_page(json)
        os.system('clear')
        now_time=json.get('data')['updateInfo']
        title='电影名称--综合票房(万)--上映天数--票房占比--排片场次--总票房\n'
        today_all='今日总票房: %s' % json.get('data')['totalBox']+json.get('data')['totalBoxUnit']
        pf=now_time+'\n'+today_all+'\n'+title
        for result in results:
            one=result['movieName'][:7].ljust(8) + '\t'\
            +result['boxInfo'][:8].rjust(8) + '  ' \
            +result['releaseInfo'][:7].ljust(7) +' '\
            +result['boxRate'][:5].ljust(7) + ' ' \
            +result['showInfo'][:6].ljust(6) + '  ' \
            +result['sumBoxInfo'][:7].rjust(7)+'\n'
            
            pf+=one
        print(pf)
        return pf
    pf('xx')
        