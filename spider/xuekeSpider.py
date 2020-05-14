import csv
from selenium import webdriver

def getXueke():
    url = 'https://yz.chsi.com.cn/zsml/zyfx_search.jsp'
    driver = webdriver.Chrome()
    driver.get(url)
    xueke = driver.find_elements_by_xpath('//optgroup')[1].text.split('\n')
    with open('学科.csv', 'a', newline='')as csv_file:
        writer = csv.writer(csv_file)
        for i in range(1,len(xueke)+1):
            driver.find_element_by_xpath('//select[@id="mldm"]//option[@value="'+str(i).zfill(2)+'"]').click()
            menlei = driver.find_elements_by_id('yjxkdm')
            for m in menlei[0].text.split('\n')[1:]:
                rows=[[xueke[i-1], m]]
                writer.writerows(rows)

def main():
    getXueke()