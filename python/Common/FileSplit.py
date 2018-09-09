# -*- coding:utf-8 -*-
from datetime import datetime


def Main():
    source_dir = '/Users/tongjia/Desktop/test/all.sql'
    target_dir = '/Users/tongjia/Desktop/test/'

    # 计数器
    flag = 0

    # 文件名
    name = 1

    # 存放数据
    dataList = []

    print("开始。。。。。")
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    with open(source_dir, 'r') as f_source:
        for line in f_source:
            flag += 1
            dataList.append(line)
            print('line = ', line)
            if line.find(';') >= 0:
                print('bingo !!!!!')
                with open(target_dir + dataList[1] + ".sql", 'w+') as f_target:
                    for data in dataList:
                        f_target.write(data)
                name += 1
                flag = 0
                dataList = []

    # 处理最后一批行数少于200万行的
    with open(target_dir + "sql_split" + str(name) + ".txt", 'w+') as f_target:
        for data in dataList:
            f_target.write(data)

    print("完成。。。。。")
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


if __name__ == "__main__":
    Main()

