from python.Common.EWB.FileHandleApi import FileHandleApi as fh


if __name__ == '__main__':
    count = 0
    page_no = 0
    cur_currency = ''
    cur_gl = ''
    page_change = 0
    data_find = ''
    data_set_tmp = []
    data_set = []
    tmp_line = ''
    row_count = 0
    fp = fh().ReadFileUtf8(r'C:\Users\90688\Documents\WeChat Files\d906889002\Files\PAT DVL AGLR1013_R1726889.TXT')
    # fp = fh().ReadFileUtf8(r'C:\Users\90688\Desktop\1.txt')
    all_lines = fp.readlines()
    fp.close()

    for line in all_lines:
        if line.find('East West Bank') >= 0:
            page_no = line[line.find('PAGE'):].split(' ')[2].replace('\n', '')
            page_change = 1
            data_find = 0
            print('page_no:' + str(page_no))
            count += 1
            print('count:' + str(count))

        elif (page_change == 1) & (line.find('CURRENCY') >= 0):
            page_change = 0
            cur_currency = line[line.find('CURRENCY'):].split(' ')[3].replace('\n', '')
            print(cur_currency)
            data_find = 1

        elif (data_find == 1) & (line.find('GLNO') >= 0):
            cur_gl = line[line.find('GLNO'):].split(' ')[4].replace('\n', '')
            data_find += 1
            print('gl_code:' + cur_gl)

        elif data_find == 2:
            data_find += 1

        elif (data_find == 3) & (row_count == 0):
            if line.find('----------------------  ---------------------') >= 0:
                data_find = 0
            else:
                row_count += 1
                tmp_line = cur_currency + '    ' + cur_gl + '    ' + line.replace('\n', '')

        elif (data_find == 3) & (row_count == 1):
            row_count = 0
            # find line 2 first 2 elements
            la = line.strip().split(' ')
            lb = []
            for elem in la:
                if elem != '':
                    lb.append(elem)

            tmp_line += '    ' + lb[0] + '    ' + lb[1]
            list_tmp = tmp_line.split('  ')
            list_final = []
            for elem in list_tmp:
                elem = elem.strip()
                if elem != '':
                    list_final.append(elem)
            if list_final[0] in ('RMB', 'USD'):
                data_set.append(list_final)

    print(data_set)

    fpw = fh().WriteFileUtf8(r'C:\Users\90688\Desktop\10.txt')
    for elem in data_set:
        data_set_tmp = ''
        for i in elem:
            data_set_tmp += i + ','
        if len(elem) < 11:
            print(elem)
        fpw.write(data_set_tmp[:len(data_set_tmp)-1])
        fpw.write('\n')
    fpw.close()