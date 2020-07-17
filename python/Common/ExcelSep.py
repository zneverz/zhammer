"""
将一个excel工作表根据条件拆分为多个工作表
"""

import openpyxl
import pandas as pd
#import numpy as np

#str = object保留excel表数据原格式，防止保存excel时数值以科学计数格式保存造成信息丢失
df = pd.DataFrame(pd.read_excel('测试数据.xlsx',sheet_name = 'Sheet1',dtype = object))

writer = pd.ExcelWriter('测试数据.xlsx')

#在原工作簿基础上新增工作表
wb = openpyxl.load_workbook('测试数据.xlsx')
writer.book = wb

#缺失值填充为'无班级'
df['班级'] = df['班级'].fillna('无班级')

for groupname,groupdf in df.groupby('班级'):
    if groupname == '无班级':
        #将填充为'无班级'的值再改为缺失值
        groupdf['班级'] = None
        groupdf.to_excel(writer,sheet_name = groupname,index = False)
    else:
        groupdf.to_excel(writer,sheet_name = groupname,index = False)

writer.save()
writer.close()
wb.close()
