import pytesseract #图片转文字
from PIL import Image#处理图片
import time#计算时间
import xlwt#操作excel
import os#遍历文件夹
import matplotlib.pyplot as plt#处理图片
import matplotlib.image as mpimg#处理图片
import numpy as np#处理图片
from scipy import misc#处理图片
import xlutils.copy#操作excel
import xlrd#操作excel
import requests#爬取网站
from bs4 import BeautifulSoup#爬取网站
import urllib.request#爬取网站
import re#正则
import sys
import json#python转json json转python
import pymongo#操作数据库
from pymongo import MongoClient#操作数据库

a1 = '企业注册码'
a2 = '企业名称'
a3 = '类型'
a4 = '住所'
a5 = '法定代表人'
a6 ='成立时间'
a7 = '注册资本'
a8 = '营业期限'
a9 = '经营范围'
a10 = '登记机关'
o = 0

def get_Image(tupian):
    url = 'http://140.143.121.215:8080/'#爬取地址
    html = requests.get(url)#发送requests请求，获得地址源代码
    soup = BeautifulSoup(html.text, 'lxml')#做一碗汤，以lxml为标准
    img = soup.findAll('li')#获得源代码中的l标签
    content = r'<li> <img src="(.*?)"/></li>'#正则规则，匹配到括号内的内容

    for i in range(len(img)):#循环li标签的长度
        img[i] = str(img[i])#获得img[i]内的内容并转成字符串形式
        ans = re.findall(content, img[i], re.S | re.I)#正则匹配img[i]，以content为flag，找到所有符合要求的字符串
        dizhi = 'http://140.143.121.215:8080/' + ans[0]#因为图片地址前面地址内容固定，顾需要正则匹配到的字符串加固定字符串等于该图片的源地址
        urllib.request.urlretrieve(dizhi, tupian+'/'+ str(i + 1) + '.png')#图片保存到本地


def file_name(filename):   #指定文件夹下排序
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)#建立一个excel文件，
    sheet = book.add_sheet('photo', cell_overwrite_ok=True)#在新建的excel中添加一个sheet，名叫photo
    sheet.write(0, 0, a1)#在坐标0，0添加内容a1
    sheet.write(0, 1, a2)
    sheet.write(0, 2, a3)
    sheet.write(0, 3, a4)
    sheet.write(0, 4, a5)
    sheet.write(0, 5, a6)
    sheet.write(0, 6, a7)
    sheet.write(0, 7, a8)
    sheet.write(0, 8, a9)
    sheet.write(0, 9, a10)
    book.save(filename + 'test.xls')#保存该excel文件，该文件的保存形式是除该内容其他内容全是空白
    for a,b,c in os.walk(filename):#遍历传入的文件夹
        # print(a) #当前路径
        # print(b) #当前路径下的所有子目录
        # print(c) #当前路径下的所有非目录子文件
        list1=[]#建立列表list1
        list2=[]
    for i in c:
        temp = re.compile(r'\d+')#因为图片的保存是以数字为名保存的，利用正则匹配文件夹中的以数字命名的图片，以temp为flag匹配字符串
        res = re.findall(temp,i)#正则的匹配，匹配i中符合temp规则的字符串
        for j in res:
            list1.append(j)#把匹配到的字符串添加到列表list1中

    for i in list1:#遍历列表list1
        sum=int(i)#文件名默认是字符串格式，要转成int才能进行数字的比较，因为字符串的11<2，所以图片的识别不是顺序的，导致识别出来的信息不是顺序的
        list2.append(sum)#把sum的值赋给列表list2
        sum=sorted(list2)#利用sorted自动令list2排序
    for i in sum:
        temp = str(i)+'.png'#此时的sum是顺序的，但要把数字再次转成字符串格式才能匹配到文件夹中的文件
        temp = filename+'/'+temp#图片的文件名字加本地的地址，形成图片的绝对地址，图片打开用

        text = pytesseract.image_to_string(Image.open(temp), lang='chi_sim')#图片转文字，
        b = text[12:30]  # 企业注册号号码
        d = text[42:68]  # 名称
        e = text[76:110] #类型
        f = text[118:152]#住所
        g = text[164:170]#法定代表人
        h = text[180:192] # 成立时间
        m = text[201:216]#注册资本
        j = text[236:440]#经营范围
        k = text[450:470]#登记机关
        x = h+'至今'



        rb = xlrd.open_workbook(filename+'test.xls')#以xlrd打开一个excel文件
        wb = xlutils.copy.copy(rb)#问了不覆盖原来的信息，需要copy原来的文件，获取原来文件的内容
        ws = wb.get_sheet(0)#获得打开excel，获得该excel中的第一个sheet
        ws.write(i, 0, b)#在i，0地址存入b的内容
        ws.write(i, 1, d)
        ws.write(i, 2, e)
        ws.write(i, 3, f)
        ws.write(i, 4, g)
        ws.write(i, 5, h)
        ws.write(i, 6, i)
        ws.write(i, 7, x)
        ws.write(i, 8, j)
        ws.write(i, 9, k)
        wb.save(filename + r'/test.xls')#保存excel，覆盖原来的excel文件，但依然能保留原来的信息
    return


def file_name1(filename1):   #指定文件夹下排序
    # book = xlwt.Workbook(encoding='utf-8', style_compression=0)#建立一个excel文件，
    # sheet = book.add_sheet('photo', cell_overwrite_ok=True)#在新建的excel中添加一个sheet，名叫photo
    # sheet.write(0, 0, a1)#在坐标0，0添加内容a1
    # sheet.write(0, 1, a2)
    # book.save(filename1+'test.xls')#保存该excel文件，该文件的保存形式是除该内容其他内容全是空白

    for a,b,c in os.walk(filename1):
        # print(a) #当前路径
        # print(b) #当前路径下的所有子目录
        # print(c) #当前路径下的所有非目录子文件
        list1=[]
        list2=[]
    for i in c:
        temp = re.compile(r'\d+')#因为图片的保存是以数字为名保存的，利用正则匹配文件夹中的以数字命名的图片，以temp为flag匹配字符串
        res = re.findall(temp,i)#正则的匹配，匹配i中符合temp规则的字符串
        for j in res:
            list1.append(j)#把匹配到的字符串添加到列表list1中

    for k in list1:#遍历列表list1
        sum=int(k)#文件名默认是字符串格式，要转成int才能进行数字的比较，因为字符串的11<2，所以图片的识别不是顺序的，导致识别出来的信息不是顺序的
        list2.append(sum)#把匹配到的字符串添加到列表list1中
        sum=sorted(list2)#利用sorted自动令list2排序
    for j in sum:
        temp = str(j)+'.png'#此时的sum是顺序的，但要把数字再次转成字符串格式才能匹配到文件夹中的文件
        temp = filename1+temp#图片的文件名字加本地的地址，形成图片的绝对地址，图片打开用
        le = mpimg.imread(temp)#读取图片
        le = le[0:76, 0:500, :]#根据图片的像素截取图片，只取前两行，
        le2 = misc.imresize(le, 0.99)#比例调整图片
        plt.imshow(le2)#show图片
        plt.axis('off')#把图片中的横纵坐标关闭，不显示
        plt.savefig('test.png')#保存该图片
        plt.show()
        # 二值处理：彩色转灰度，灰度转二值，二值图像识别
        im = Image.open('test.png')#打开要是别的图片
        imgry = im.convert('L')#灰度处理图片
        imgry.show()
        threshold = 140#设置中间值
        table = []#元组
        for wo in range(256):
            if wo < threshold:
                table.append(0)
            else:
                table.append(1)

        out = imgry.point(table, '1')#二值形成图片 1代表RGB
        out.save('test.png')#保存图片
        out.show()


        text = pytesseract.image_to_string(Image.open('test.png'), lang='chi_sim')#图片转文字，
        d = text[12:30]  # 企业注册号号码
        f = text[40:]  # 名称

        rb = xlrd.open_workbook(filename1 + 'test.xls')#以xlrd打开一个excel文件
        wb = xlutils.copy.copy(rb)#问了不覆盖原来的信息，需要copy原来的文件，获取原来文件的内容
        ws = wb.get_sheet(0)#获得打开excel，获得该excel中的第一个sheet
        ws.write(j, 0, d)#在i，0地址存入d的内容
        ws.write(j, 1, f)
        wb.save(filename1 + r'/test.xls')#保存excel，覆盖原来的excel文件，但依然能保留原来的信息
        plt.close('all')#关闭图片，否则循环每次识别图片会形成重叠
    return


def cunku():
    # 连接数据库
    client = MongoClient('localhost', 27017)#连接数据库，地址+端口
    db = client['test']#连接test数据库

    ta = db['student']#连接student集合
    ta.drop()#删除集合

    data = xlrd.open_workbook('E:/meishi/test.xls')#打开要存入的excel文件
    table = data.sheets()[0]#获得excel文件中的第一个sheet
    rowstag = table.row_values(0)#获得该sheet下的第一行作为key
    nrows = table.nrows#获得该sheet的所有行
    returnData = {}#字典
    for i in range(1, nrows):#循环1到行数（不包括行数的当前值）
        returnData[i] = json.dumps(dict(zip(rowstag, table.row_values(i))))#将python的数据类型转成json，形成一个字典
        returnData[i] = json.loads(returnData[i])#将json格式的信息转成python的数据类型  也叫json解码
        ta.insert(returnData[i])#将数据插入到数据库中


def yemian():
    print('---------------------------------')
    print('-----1-----------爬虫--------------')
    print('-----2--------识别图片全部---------')
    print('-----3------识别图片部分----------')
    print('-----4-----选择存储到数据库-------')


if __name__ == '__main__':
    yemian()
    shuzi = int(input('请输入你心仪的数字'))
    if shuzi == 1:
        tupian = input('麻烦在输入一下图片保存地址')
        get_Image(tupian)
    if shuzi == 2:
        filename = input('这就牛逼了，你输个地址就能把你地址里的文字转成图片')
        file_name(filename)
    if shuzi == 3:
        filename1 = input('这个比上一个稍微虚点，只能识别部分')
        file_name1(filename1)
    if shuzi == 4:
        y = input('你要不要存数据库啊，mongodb很牛逼的啊(y/n)')
        if y == 'y':
            cunku()
        else:
            print('不存还选我，浪费时间')