

import mysql.connector as mysql


conn = mysql.connect(host='127.0.0.1',user='root',password='password',database='dmp')
cursor = conn.cursor()
cursor.execute("select table_name from information_schema.tables where table_schema='dmp' and table_type='base table'")
tables = cursor.fetchall()

markdown_table_header = """### %s 
FieldName , Type , Default , Remark
---- , ---- , ---- , ---- 
"""
markdown_table_row = """%s , %s , %s , %s
"""
#保存输出结果
f = open('DataDictionaryDef.csv','w')
for table in tables:
    cursor.execute("select COLUMN_NAME,COLUMN_TYPE,COLUMN_DEFAULT,COLUMN_COMMENT from information_schema.COLUMNS where "
                   "table_schema='dmp' and table_name='%s'"% table)
    tmp_table = cursor.fetchall()
    p = markdown_table_header % table;
    for col in tmp_table:
        p += markdown_table_row % col
    #print p
    f.writelines(p)
f.close()
