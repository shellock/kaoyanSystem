import requests
from lxml import etree
import os
import glob
from multiprocessing import Pool
import math
import csv
import random

ip =['218.73.117.118:3617',
     '36.4.84.162:3617',
    '180.122.119.233:5412',
    '59.63.67.198:23564',
    '58.255.7.168:23564',
    '59.62.103.27:23564',
    '114.97.242.245:766',
    '117.64.225.70:894',
    '27.40.110.174:3617',
    '117.67.245.123:5412',
    '114.98.31.84:894',
    '60.187.54.19:23564',
    '106.87.84.96:766',
    '112.113.154.163:23564',
    '183.163.175.235:5412',
    '122.246.93.98:23564',
    '112.114.88.204:36410',
    '116.55.140.181:5412',
    '114.227.163.96:894',
    '114.104.128.153:894',
    '117.69.170.95:23564',
    '223.215.175.86:23564',
    '49.87.247.126:3617',
    '182.32.103.49:894',
    '112.237.119.120:23564',
    '114.238.101.253:5412',
    '49.87.79.181:23564',
    '59.63.67.127:23564',
    '117.64.251.229:5412',
    '117.69.47.179:23564',
    '113.231.202.3:766',
    '218.74.78.8:3617',
    '36.59.202.244:5412',
    '219.130.171.160:894',
    '182.86.8.49:3617',
    '112.237.48.113:3617',
    '27.204.94.192:3617',
    '125.123.125.142:766',
    '117.43.175.106:766',
    '113.64.164.201:894']

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
}

psoxy = {
    'http':'http://'+ ip[random.randint(0,39)]
}

def getReportingratio(num):
    data_list = []
    url = 'https://souky.eol.cn/HomePage/index_' + str(num) + '.html'
    response = requests.get(url, headers=headers,proxies = psoxy)
    if response.status_code == 200:
        for year in range(2020,2021):
            url = 'https://souky.eol.cn/web/school/school_score/?school_id=' + str(num) + '&year=' + str(year) + '&degree_type=&area_type='
            response = requests.get(url, headers = headers, proxies = psoxy)
            response.encoding = 'utf-8'
            html = response.text
            etreehtml = etree.HTML(html)
            school_name = etreehtml.xpath('//div[@class="school"]/text()')
            items = etreehtml.xpath('//h3[@class="fl"]/i[1]/text()')
            if school_name != []:
                try:
                    allpage = math.ceil(int(items[0])/10)
                except:
                    allpage = 1
                for nowpage in range(1, allpage + 1):
                    url = 'https://souky.eol.cn/web/school/school_score/'+ str(nowpage) + '?school_id=' + str(num) + '&year=' + str(year) + '&degree_type=&area_type='
                    response = requests.get(url, headers=headers, proxies = psoxy)
                    response.encoding = 'utf-8'
                    html = response.text
                    etreehtml = etree.HTML(html)
                    all = etreehtml.xpath('//tbody/tr/td/text()')
                    item_num = len(etreehtml.xpath('//tbody/tr[2]/td'))
                    all = [x for x in all if x!='\n                                    ']
                    try:
                        all = list_split(all,item_num)
                    except:
                        item_num = 0
                        break
                    if item_num == 7:
                        for a in all:
                            if len(a) < 7 or a[1] == '0':
                                break
                            data_dict = {}
                            data_dict['年份'] = str(year)
                            data_dict['学校'] = school_name[0]
                            data_dict['类型'] = a[0]
                            data_dict['科目'] = a[1]
                            data_dict['总分'] = a[2]
                            data_dict['政治'] = a[3]
                            data_dict['英语'] = a[4]
                            data_dict['业务课一'] = a[5]
                            data_dict['业务课二'] = a[6]
                            data_list.append(data_dict)
                    elif item_num == 5:
                        for a in all:
                            data_dict = {}
                            data_dict['年份'] = str(year)
                            data_dict['学校'] = school_name[0]
                            data_dict['类型'] = a[0]
                            data_dict['科目'] = a[1]
                            data_dict['总分'] = a[2]
                            data_dict['分数线单科等于100'] = a[3]
                            data_dict['分数线单科大于100'] = a[4]
                            data_list.append(data_dict)
                    #print(data_list)
            try:
                if item_num == 5 or item_num == 7:
                    save(school_name[0],item_num,data_list)
                    print(1)
            except:
                None

def list_split(items, n):
    return [items[i:i+n] for i in range(0, len(items), n)]

def save(school_name,item_num,data_list):
    if not os.path.exists('./学校分数线/' + str(item_num)):
        os.makedirs('./学校分数线/' + str(item_num))
    with open('./学校分数线/' + str(item_num)+ '/'+ school_name +'.csv', 'w', encoding='utf-8', newline='') as f:
        title = data_list[0].keys()
        writer = csv.DictWriter(f, title)
        writer.writeheader()
        writer.writerows(data_list)
    print('csv文件写入完成')

def merge_csv(the_dir):
    try:
        csv_list = glob.glob('./学校分数线/'+str(the_dir)+'/*.csv')
        print('总共发现%s个CSV文件' % len(csv_list))
        fr = open(csv_list[0], 'r').read()
        with open('学校分数线' + str(the_dir) + '.csv', 'a') as f:
            f.write(fr)
        for the_csv in csv_list[1:]:
            fr = open(the_csv, 'r').read()
            fr = fr.split('\n',1)[1]
            with open('学校分数线'+str(the_dir)+'.csv', 'a') as f:
                f.write(fr)
        print('学校分数线' + str(the_dir) + '.csv'+'写入成功！')
    except:
        print('学校分数线' + str(the_dir) + '.csv'+'写入失败！')

def main():
    pool=Pool(32)
    pool.map(getReportingratio,[num for num in range(1,1500)])
    pool.close()
    pool.join()
    merge_csv(5)
    merge_csv(7)