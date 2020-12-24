#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#
import pymysql

# 原始数据的数据连接
db1 = pymysql.connect('172.168.1.202', 'appuser', 'Qgy@815133', 'datapoint_k36')
cursor1 = db1.cursor()
# 定义查询语句
len1 = cursor1.execute("select * from tstream_dp_2_0_2001_101 where coltime BETWEEN '2020-10-30 13:00:00' and '2020-10-31 13:00:00' LIMIT 1")
results = cursor1.fetchone()

print("Results = ", results);

# 迁移库的数据连接
db2 = pymysql.connect('10.0.16.19', 'appuser', 'Qgy@815133', 'k36_source')
cursor2 = db2.cursor()
# 批量插入语句
sql = 'insert into tstream_dp_2_0_2001_101 values (%s) ' % results

print("sql =", sql)

cursor2.execute(sql)

# # 每次循环导入的数据量
# num = 11
#
# for i in range(int(len1/num)):
#     print(i)
#     data1 = cursor1.fetchmany(num)
#     cursor2.executemany(sql, data1)
#
# # 把剩下的数据一次性导入
# data2 = cursor1.fetchall()
# cursor2.executemany(sql, data2)

# 这种可以全部导入
# data2 = cursor1.fetchall()
# cursor2.executemany(sql, data2)

# 提交到数据库
db2.commit()

# 关闭数据库连接
db1.close()
db2.close()