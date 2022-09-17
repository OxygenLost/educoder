import requests
from bs4 import BeautifulSoup
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import re
from win10toast import ToastNotifier  # 导入系统通知对象
import time  # 系统时间模块
import datetime
from threading import Timer  # 定时器模块

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
web = webdriver.Chrome(chrome_options=chrome_options)

web.get('https://www.educoder.net/classrooms/J5A7CM4T/shixun_homework?tabs=1')

f = open('D:\ProgramCode\spider-educoder\cookiesss.txt', 'r')
listcookie = json.loads(f.read())  # 读取文件中的cookies数据

for cookie in listcookie:
    web.add_cookie(cookie)  # 将cookies数据添加到浏览器
web.refresh()  # 刷新网页

time.sleep(2)

html = web.page_source
soup = BeautifulSoup(html, 'lxml')

# 时间的正则表达
name = soup.find_all('span', class_='name___3IcSf')
datatime = soup.find_all('span', class_='ml20 c-grey-999')
endtime = []

for i in range(len(name)):
    # print(name[i].text)
    # print(datatime[i].text)
    # print(re.findall(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}', datatime[i].text)[1])
    endtime.append(re.findall(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}', datatime[i].text)[1])

# 时间转化
endtime = [time.strptime(i, '%Y-%m-%d %H:%M') for i in endtime]
endtime = [time.mktime(i) for i in endtime]

classname = {}
# 把name和time放到一个字典里面一一对应
for i in range(len(name)):
    classname[name[i].text] = endtime[i]

# 对字典按照时间排序
classname = sorted(classname.items(), key=lambda x: x[1], reverse=False)

# 时间转化
classname = [(time.strftime('%Y-%m-%d %H:%M', time.localtime(i[1])), i[0]) for i in classname]

# 打印出来第一个
# print(classname[0])
print("距离截止时间最近的是：", classname[0][1], "时间是：", classname[0][0])

notify = ToastNotifier()  # 初始化系统通知对象
notify_head = '主人，来通知啦！'
notify_text = '距离截止时间最近的是：' + classname[0][1] + '时间是：' + classname[0][0]
notify.show_toast(f"{notify_head}", f"{notify_text}", duration=5, threaded=True)
