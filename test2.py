import pytesseract
from PIL import Image
import time
import xlwt
import os
import re
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from scipy import misc
import xlwt
import requests
import time
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

def file_name(filename):   #指定文件夹下排序
    for a,b,c in os.walk(filename):
        # print(a) #当前路径
        # print(b) #当前路径下的所有子目录
        # print(c) #当前路径下的所有非目录子文件
        list1=[]
        list2=[]
    for i in c:
        temp = re.compile(r'\d+')
        res = re.findall(temp,i)
        for j in res:
            list1.append(j)

    for i in list1:
        sum=int(i)
        list2.append(sum)
        sum=sorted(list2)
    for i in sum:
        temp = str(i)+'.png'
        temp = filename+'\\'+temp
        # 二值处理
        # im = Image.open('test.png')
        # imgry = im.convert('L')
        # threshold = 140
        # table = []
        # for i in range(256):
        #     if i < threshold:
        #         table.append(0)
        #     else:
        #         table.append(1)
        #
        # out = imgry.point(table, '1')
        # out.save('test.png')

        book = xlwt.Workbook(encoding='utf-8', style_compression=0)
        sheet = book.add_sheet('photo', cell_overwrite_ok=True)
        text = pytesseract.image_to_string(Image.open(temp), lang='chi_sim')
        b = text[12:30]  # 企业注册号号码
        d = text[42:68]  # 名称
        e = text[76:110] #类型
        f = text[118:152]#住所
        g = text[164:170]#法定代表人
        h = text[180:192] # 成立时间
        i = text[201:216]#注册资本
        j = text[236:440]#经营范围
        k = text[450:470]#登记机关
        x = h+'至今'
        sheet.write(0, 0, a1)
        sheet.write(0, 1, a2)
        sheet.write(0, 2, a3)
        sheet.write(0, 3, a4)
        sheet.write(0, 4, a5)
        sheet.write(0, 5, a6)
        sheet.write(0, 6, a7)
        sheet.write(0, 7, a8)
        sheet.write(0, 8, a9)
        sheet.write(0, 9, a10)

        sheet.write(1, 0, b)
        sheet.write(1, 1, d)
        sheet.write(1, 2, e)
        sheet.write(1, 3, f)
        sheet.write(1, 4, g)
        sheet.write(1, 5, h)
        sheet.write(1, 6, i)
        sheet.write(1, 7, x)
        sheet.write(1, 8, j)
        sheet.write(1, 9, k)
        book.save(r'E:/chang/test.xls')

    return

if __name__ == '__main__':
    file_name(r'E:\meishi')
