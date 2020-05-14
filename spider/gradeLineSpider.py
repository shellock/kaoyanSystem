import requests
from lxml import etree
import json
import csv
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
}
data_list = []#设置全局变量来存储数据
def getGradeLine():
    url = 'https://yz.chsi.com.cn/yzzt/kyfs2020'
    response = requests.get(url, headers=headers)
    response = response.text
    etreehtml = etree.HTML(response)
    new_url = etreehtml.xpath('//tbody/tr[1]/th/a/@href')
    for i in range(len(new_url)):
        new_url[i] = 'https://yz.chsi.com.cn' + new_url[i]
        response = requests.get(new_url[i], headers=headers)
        html = response.text
        etreehtml = etree.HTML(html)
        url_2 = etreehtml.xpath('//a[contains(@href,"/kyzx/kp/20")]/@href')
        url_2.remove('/kyzx/kp/201809/20180905/1718874229.html')
        for i in range(len(url_2)):
            if not url_2[i].startswith('http'):
                url_2[i] = 'http://yz.chsi.com.cn' + url_2[i]
            wholeCountryLine(url_2[i])

def wholeCountryLine(url):
    response = requests.get(url, headers=headers)
    response = response.text
    etreehtml = etree.HTML(response)
    name = etreehtml.xpath('//div/h2//text()')[0]
    try:
        name = name[:4] + name.split('(')[1].split(')')[0]
    except:
        None
    try:
        name = name[:4] + name.split('（')[1].split('）')[0]
    except:
        None
    print(name)
    rol = len(etreehtml.xpath('//tbody/tr'))
    for i in range(3,rol):
        grades = etreehtml.xpath('//tbody/tr['+ str(i)+']/td')
        list = []
        j = 0
        for grade in grades:
            if len(grade.xpath('string(.)').split("\n")) == 3:
                list.append(grade.xpath('string(.)').split("\n")[1])
            elif len(grade.xpath('string(.)').split("\n")) == 4 and j!=0:
                list.append(grade.xpath('string(.)').split("\n")[2])
            elif len(grade.xpath('string(.)').split("\n")) == 4:
                list.append(grade.xpath('string(.)').split("\n")[1])
            else:
                list.append(grade.xpath('string(.)').split("\n")[0])
            j = j + 1
        try:
            list = [list[i] for i in range(7)]
        except:
            None
        for i in range(len(list)):
            try:
                list[i] = "".join(list[i].split())
            except:
                None
        if len(list)==7:
            print(list)
            data_dict = {}
            data_dict['标题'] = name
            data_dict['学科'] = list[0]
            data_dict['A类:总分'] = list[1]
            data_dict['A类:单科(满分=100分)'] = list[2]
            data_dict['A类:单科(满分>100分)'] = list[3]
            data_dict['B类:总分'] = list[4]
            data_dict['B类:单科(满分=100分)'] = list[5]
            data_dict['B类:单科(满分>100分)'] = list[6]
            data_list.append(data_dict)

def save():
    content = json.dumps(data_list, ensure_ascii=False, indent=2)
    with open('国家分数线2.json', "a+", encoding="utf-8") as f:
        f.write(content)
        print('json文件写入成功')
    with open('国家分数线2.csv', 'w', encoding='utf-8', newline='') as f:
        title = data_list[0].keys()
        writer = csv.DictWriter(f, title)
        writer.writeheader()
        writer.writerows(data_list)
    print('csv文件写入完成')

def main():
    getGradeLine()
    save()