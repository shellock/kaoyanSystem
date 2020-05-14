import threading
import random
import requests
from lxml import etree
import csv
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
}

ip =[
'125.87.106.61:21828',
'115.59.246.199:28803',
'49.71.133.191:25101',
'180.123.194.10:20650',
'60.169.213.78:28803',
'218.95.123.125:11747',
'113.218.222.164:20864',
'114.104.185.239:14029',
'171.40.18.158:21600',
'223.166.104.80:19850',
]

psoxy = {
    'http':'http://'+ ip[random.randint(0,9)]
}

data_list = []

def getPage():
    url = 'http://yz.kaoyan365.cn/baolubi/'
    response = requests.get(url, headers=headers)
    response = response.text
    etreehtml = etree.HTML(response)
    pages = int("".join(filter(str.isdigit, etreehtml.xpath('//ul[@id="yw0"]/li[9]/a/@href')[0])))
    return pages

def getReportingRatio(page):
    url = 'http://yz.kaoyan365.cn/baolubi/list/_0_0_0_'+str(page)+'.html'
    response = requests.get(url, headers = headers)
    response = response.text
    etreehtml = etree.HTML(response)
    messages = etreehtml.xpath('//*[@id="clearfix"]/div[1]/table/tr')
    list=[]
    for message in messages:
        for msg in message.xpath('./td'):
            m = msg.xpath('.//text()')
            if m:
                list.append(m[0])
            else:
                list.append('/')
    list = list_split(list,10)
    for l in list[1:]:
        data_dict = {}
        if (l[6]=='/' and l[7]=='/' and l[8]=='/' and l[9]=='/'):
            continue
        data_dict['年份'] = l[0]
        data_dict['地区'] = l[1]
        data_dict['院校名称'] = l[2]
        data_dict['院系名称'] = l[3]
        data_dict['专业代码'] = l[4]
        data_dict['专业名称'] = l[5]
        data_dict['报名人数'] = l[6]
        data_dict['录取人数'] = l[7]
        data_dict['报录比'] = l[8]
        data_dict['推免人数'] = l[9]
        data_list.append(data_dict)

def list_split(items, n):
    return [items[i:i+n] for i in range(0, len(items), n)]

def main():
    pool = []
    for i in range(3640,getPage()):
        t1 = threading.Thread(target=getReportingRatio, args=(i,))
        pool.append(t1)
    pool = list_split(pool,20) # 同时运行多个
    i=1
    for thread_list in pool:
        for t in thread_list:
            t.start()
        for t in thread_list:
            t.join()
    save()

def save():
    with open('学校报录比1.csv', 'w', encoding='utf-8', newline='') as f:
        title = data_list[0].keys()
        writer = csv.DictWriter(f, title)
        writer.writeheader()
        writer.writerows(data_list)
    print('csv文件写入完成')