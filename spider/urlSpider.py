import requests
from lxml import etree
import csv
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
}

def getSchool(url):
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    response = response.text
    etreehtml = etree.HTML(response)
    urls = etreehtml.xpath('//a')
    with open('学校链接.csv', 'a', newline='')as csv_file:
        writer = csv.writer(csv_file)
        for url in urls:
            school = url.xpath('.//text()')
            if school:
                if(school[0].find('研究生院')>=0):
                    rows = [[school[0], url.xpath('./@href')[0]]]
                    writer.writerows(rows)

def getLocation():
    url = 'http://www.kaoyan.com/beijing/'
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    response = response.text
    etreehtml = etree.HTML(response)
    urls = etreehtml.xpath('//ul[@class="yzAreaList"]/li/@rel')
    for url in urls:
        getSchool(url)

def main():
    getLocation()
