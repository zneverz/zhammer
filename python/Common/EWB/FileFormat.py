# -*- coding:utf-8 -*-
from datetime import datetime


def Main():
    source_dir = '/Users/tongjia/Desktop/check/mov/TP.TXT'
    target_dir = '/Users/tongjia/Desktop/check/mov/'

    # 存放数据
    dataList = []
    dataListTmp = []

    print("开始。。。。。")
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    fuck = ''
    tmp = ''

    with open(source_dir, 'r') as f_source:
        for line in f_source:

            # print('***line = ', line)

            if line.find('PAGE:') >= 0 or line.find('AGLR1013') >= 0 or line.find('PRINT ON  :') >= 0 \
                    or line.find('------------') >= 0 or line.find('B/F:') >= 0 or line.find('TOTAL :') >= 0 \
                    or line.find('=======') >= 0 or line.find('&k2S') >= 0 or line.find('END OF REPORT') >= 0 \
                    or line.find('VOUCHER DATE') >= 0 or line.find('VOUCHER NO. SEQ.') >= 0 or line == '\n':
                continue

            if line.find('BRANCH') >= 0:
                line = line.replace('\n', '***')
            elif line.find('GLNO') >= 0:
                line = '|' + line.replace('\n', '###')
            else:
                line = line.replace('\n', '')

            if line.find('BRANCH') >= 0 or line.find('GLNO') >= 0:

                if fuck == '':
                    fuck = line
                    continue
                # print("***line mid = ", line)
                # print("***fuck mid = ", fuck)
                if fuck.find('BRANCH') >= 0 and line.find('BRANCH') >= 0:
                    fuck = fuck.replace(fuck[fuck.find('BRANCH')-1:fuck.find('***')], line)
                elif fuck.find('BRANCH') < 0 and line.find('BRANCH') >= 0:
                    fuck = fuck + line

                if fuck.find('GLNO') >= 0 and line.find('GLNO') >= 0:
                    fuck = fuck.replace(fuck[fuck.find('|GLNO'):fuck.find('###')], line)
                elif fuck.find('GLNO') < 0 and line.find('GLNO') >= 0:
                    fuck = fuck + line

                # fuck = line
                # print('***fuck aft = ', fuck)
                continue
            line = line + ' ' + fuck + '\n'
            # print("***line aft = ", line)
            dataList.append(line)
        # print(dataList[::1])
        j = 1
        for i in dataList:
            # print('***iiiii = ', i)
            i = i.replace('\n', '')
            if j % 2 == 0:
                tmp = tmp+'|'+i
                tmp.replace('\n', '')
                # print('j = ', j)
                # print('***tmp+i = ', tmp)

                dataListTmp.append(tmp+'\n')
                tmp = ''
            else:
                tmp = i
                tmp.replace('\n', '')
            j += 1
        # print('-------------------------')
        # print(dataListTmp)

    with open(target_dir + "fuck_all" + ".txt", 'w+') as f_target:
        for data in dataListTmp:
            data = data.replace('***', '')
            data = data.replace('###', '')
            data = data.replace('BRANCH', '|BRANCH')
            data = data.replace('CURRENCY', '|CURRENCY')
            f_target.write(data)

    with open(target_dir + "fuck_132_5010" + ".txt", 'w+') as f_target:
        for data in dataListTmp:
            data = data.replace('***', '')
            data = data.replace('###', '')
            data = data.replace('BRANCH', '|BRANCH')
            data = data.replace('CURRENCY', '|CURRENCY')
            if ((data.find('GLNO  :  132') >= 0 or data.find('GLNO  :  5010') >= 0) and data.find('DP') < 0 and
                    data.find('VT') < 0):
                f_target.write(data)

    print("完成。。。。。")
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


if __name__ == "__main__":
    Main()

