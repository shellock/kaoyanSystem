import requests
from bs4 import BeautifulSoup
from lxml import etree
import json
import csv

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
}

data_list = []#设置全局变量来存储数据

def getSchoolRank():
    nowpage = 1
    while(True):
        print(2)
        if nowpage == 1:
            url = 'https://m.dxsbb.com/news/list_135.html'
        else:
            url = 'https://m.dxsbb.com/news/list_135_'+str(nowpage)+'.html'
        response = requests.get(url, headers=headers)
        response.encoding = 'gb2312'
        html = response.text
        etreehtml = etree.HTML(html)
        major_url = etreehtml.xpath('//div[@class="a"]/..//@href')
        name = etreehtml.xpath('//ul/li/a/div[2]/h3/text()')
        if nowpage == 1:
            page = len(etreehtml.xpath('//option/text()'))
        for i in range(len(major_url)):
            major_url[i] = 'https://m.dxsbb.com/' + major_url[i].split('.')[2] + '.html'
            if (name[i].find('排名') >= 0):
                getRanking(major_url[i],name[i])
        if nowpage == page:
            break
        nowpage = nowpage + 1

def getRanking(major_url,major):
    list1 = []
    list2 = []
    list3 = []
    response = requests.get(major_url, headers=headers)
    response.encoding = 'gb2312'
    response = response.text
    soup = BeautifulSoup(response, 'html.parser')
    html = str(soup.find('tbody'))
    soup = BeautifulSoup(html, 'html.parser')
    school_num = len(soup.findAll('tr'))
    soup = BeautifulSoup(str(soup.findAll('tr')), 'html.parser')
    newhtml = soup.findAll('td')
    all_num = len(newhtml)
    a = 0
    for item in newhtml:
        if (a % (all_num/school_num) == 0):
            list1.append(item.get_text())
        if (a % (all_num/school_num) == 1):
            list2.append(item.get_text())
        if (a % (all_num/school_num) == 2):
            list3.append(item.get_text())
        a=a+1
    for i in range(1,len(list1)):
        data_dict = {}
        data_dict['标题'] = major
        data_dict['排名'] = list1[i]
        data_dict['学校'] = list2[i]
        try:
            data_dict['评估'] = list3[i]
        except:
            data_dict['评估'] = '无'
        data_list.append(data_dict)
    print(data_list)

def save():
    content = json.dumps(data_list, ensure_ascii=False, indent=2)
    with open('专业排名.json', "a+", encoding="utf-8") as f:
        f.write(content)
        print('json文件写入成功')
    with open('专业排名.csv', 'w', encoding='utf-8', newline='') as f:
        title = data_list[0].keys()
        writer = csv.DictWriter(f, title)
        writer.writeheader()
        writer.writerows(data_list)
    print('csv文件写入完成')

def main():
    getSchoolRank()
    save()