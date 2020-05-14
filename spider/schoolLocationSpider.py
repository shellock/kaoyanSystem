import threading

import requests
from lxml import etree
import json
import csv
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
}

data_list = []
def getPage():
    url = 'https://yz.chsi.com.cn/sch/search.do?ssdm=&yxls='
    response = requests.get(url, headers=headers)
    response = response.text
    # print(response)
    etreehtml = etree.HTML(response)
    pages = int(etreehtml.xpath('//form[@method="post"]/ul/li[8]/a/text()')[0])
    return pages

def getLocation(page):
    url = 'https://yz.chsi.com.cn/sch/search.do?start=' + str(page*20)
    response = requests.get(url, headers=headers)
    response = response.text
    etreehtml = etree.HTML(response)
    schools = etreehtml.xpath('//tbody/tr/td//text()')
    for i in range(len(schools)):
            schools[i] = "".join(schools[i].split())
    schools = [x for x in schools if x != "" and x != "\ue664" and x != "进入" and x != "查询" and x != "查看"]
    schools = list_split(schools,3)
    for schoolmsg in schools:
        data_dict = {}
        data_dict['学校'] = schoolmsg[0]
        data_dict['所在地'] = schoolmsg[1]
        data_dict['院校隶属'] = schoolmsg[2]
        data_list.append(data_dict)

def list_split(items, n):
    return [items[i:i+n] for i in range(0, len(items), n)]

def main():
    for i in range(getPage()):
        t = threading.Thread(target=getLocation, args=(i,))
        t.start()
        t.join()
    save()

def save():
    with open('学校地区.csv', 'w', encoding='utf-8', newline='') as f:
        title = data_list[0].keys()
        writer = csv.DictWriter(f, title)
        writer.writeheader()
        writer.writerows(data_list)
    print('csv文件写入完成')