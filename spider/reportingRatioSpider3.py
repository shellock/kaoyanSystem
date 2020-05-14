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

def getUrl():
    url = 'http://www.kaoyan.com/baolubi/'
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    response = response.text
    etreehtml = etree.HTML(response)
    urls = etreehtml.xpath('//a[contains(@title,"报录比")]/@href')
    print(len(urls))
    return urls[1:]

def getUrl2(url):
    for i in range (1,getPage(url)+1):
        new_url = url
        if i != 1:
            new_url = url + 'index_'+str(i)+'.html'
        response = requests.get(new_url, headers=headers)
        response.encoding = 'utf-8'
        response = response.text
        etreehtml = etree.HTML(response)
        urls = etreehtml.xpath('//a[contains(@title,"报录比")]/@href')
        urls = list(set(urls))
        try:
            urls.remove(url)
        except:
            None
    for u in urls:
        response = requests.get(u, headers=headers)
        response.encoding = 'utf-8'
        response = response.text
        etreehtml = etree.HTML(response)
        try:
            school = etreehtml.xpath('//div[@class="position"]/a[3]/text()')
        except:
            continue
        try:
            year = "".join(filter(str.isdigit, etreehtml.xpath('//h1[@class="articleTitle"]/text()')[0]))[:4]
        except:
            continue
        messages=[]
        try:
            messages = etreehtml.xpath('//tbody/tr')
        except:
            continue
        list2 = []
        list3 = []
        if messages:
            long = len(messages[0].xpath('./td'))
            for msg in messages[0].xpath('./td'):
                m = msg.xpath('.//text()')
                if m:
                    if(len(m)==1):
                        list2.append(m[0])
                    else:
                        list2.append(m[1])
                else:
                    list2.append('/')
            for l in list2:
                list3.append(l.replace("\r", "").replace("\t", "").replace("\n", "").replace("\xa0","").replace("\u3000",""))
            list4 = []
            list5 = []
            for message in messages[1:]:
                for msg in message.xpath('./td'):
                    m = msg.xpath('.//text()')
                    if m:
                        list4.append(m[0])
                    else:
                        list4.append('/')
            for l in list4:
                list5.append(l.replace("\r", "").replace("\t", "").replace("\n", "").replace("\xa0","").replace("\u3000",""))
            list5 = list_split(list5, long)
            yx = [yx for yx in list3 if '院系名称' in yx]
            if not yx:
                yx = [yx for yx in list3 if '学院' in yx]
            zk = [zk for zk in list3 if '准考人数' in zk]
            if not zk:
                zk = [zk for zk in list3 if '报名人数' in zk]
            if not zk:
                zk = [zk for zk in list3 if '报录人数' in zk]
            if not zk:
                zk = [zk for zk in list3 if '报考' in zk]
            lq = [lq for lq in list3 if '录取' in lq]
            zymc = [zymc for zymc in list3 if '专业名称' in zymc]
            if not zymc:
                zymc = [zymc for zymc in list3 if '专业' in zymc]
            zydm = [zydm for zydm in list3 if '专业代码' in zydm]
            blb = [blb for blb in list3 if '报录比' in blb]
            tmrs = [tmrs for tmrs in list3 if '推免' in tmrs]
            for ls in list5:
                if ls[0]:
                    data_dict = {}
                    data_dict['年份'] = year + "年"
                    data_dict['院校名称'] = school[0]
                    if yx:
                        data_dict['院系名称'] = ls[list3.index(yx[0])]
                    else:
                        data_dict['院系名称'] = '/'
                    if zydm:
                        data_dict['专业代码'] = ls[list3.index(zydm[0])]
                    else:
                        data_dict['专业代码'] = '/'
                    if zymc:
                        data_dict['专业名称'] = ls[list3.index(zymc[0])]
                    else:
                        data_dict['专业名称'] = '/'
                    if zk:
                        data_dict['报名人数'] = ls[list3.index(zk[0])]
                    else:
                        data_dict['报名人数'] = '/'
                    if lq:
                        data_dict['录取人数'] = ls[list3.index(lq[0])]
                    else:
                        data_dict['录取人数'] = '/'
                    if blb:
                        data_dict['报录比'] = ls[list3.index(blb[0])]
                    else:
                        try:
                            data_dict['报录比'] = str(round(float(ls[list3.index(lq[0])]) / float(ls[list3.index(zk[0])]),3)) + '%'
                        except:
                            data_dict['报录比'] = '/'
                    if tmrs:
                        data_dict['推免人数'] = ls[list3.index(tmrs[0])]
                    else:
                        data_dict['推免人数'] = '/'
                    data_list.append(data_dict)

def getPage(url):
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    response = response.text
    etreehtml = etree.HTML(response)
    try:
        page = etreehtml.xpath('//div[@class="tPage"]/a/text()')
        page = int(page[len(page)-2])
    except:
        page = 1
    return page

def list_split(items, n):
    return [items[i:i+n] for i in range(0, len(items), n)]

def save():
    with open('学校报录比3.csv', 'w', encoding='utf-8', newline='') as f:
        title = data_list[0].keys()
        writer = csv.DictWriter(f, title)
        writer.writeheader()
        writer.writerows(data_list)
    print('csv文件写入完成')

def main():
    pool = []
    for url in getUrl():
        t1 = threading.Thread(target=getUrl2, args=(url,))
        pool.append(t1)
    pool = list_split(pool, 20)  # 同时运行多个
    for thread_list in pool:
        for t in thread_list:
            t.start()
        for t in thread_list:
            t.join()
    save()