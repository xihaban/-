import xlrd
import sys
import json
import pymongo
from pymongo import MongoClient

# 连接数据库
client = MongoClient('localhost', 27017)
db =client['test']

ta=db['student']
ta.drop()

data=xlrd.open_workbook('E:/meishi/test.xls')
table=data.sheets()[0]
rowstag=table.row_values(0)
nrows=table.nrows
returnData={}
for i in range(1,nrows):
    returnData[i] = json.dumps(dict(zip(rowstag, table.row_values(i))))
    returnData[i] = json.loads(returnData[i])
    ta.insert(returnData[i])