import os
import mysql.connector
from mysql.connector import errorcode


class FileProcesses(object):

    def __init__(self):
        # target files address
        self.work_dir = '/Users/tongjia/Desktop/test/'

        # replace information
        self.d = {'dvloans': 'fuck', 'tformmetadata': 'you'}

        # db config
        self.username = 'root'
        self.password = 'password'
        self.host = '127.0.0.1'
        self.port = '3306'
        self.database = 'mytest'

    def Replace(self):
        global result
        file_data = ""
        # db Connect
        dbhandle = self.ConnectDB()
        cursor = dbhandle.cursor(buffered=True)

        for parent, dirnames, filenames in os.walk(self.work_dir, followlinks=True):
            for filename in filenames:
                file_path = os.path.join(parent, filename)
                print('文件名：%s' % filename)
                print('文件完整路径：%s\n' % file_path)
                print(self.d.keys())
                with open(file_path, "r") as f:
                    for line in f:
                        for old, new in self.d.items():
                            getCNTsql = "select sercnt from tmp_serno where keyword = '%s' " % old
                            cursor.execute(getCNTsql)
                            try:
                                result = cursor.fetchone()
                            except Exception as e:
                                print("New Record found !")
                                result[0] = 0
                            suffix = result[0] + 1
                            line = line.replace(old, new + str(suffix))
                        file_data += line
                    with open(file_path, "w", encoding="utf-8") as v:
                        v.write(file_data)
                        file_data = ""

                        #TODO Change place to have execute this sql for list of keyword
                        print(suffix)
                        print(old)
                        updatesql = "update tmp_serno set sercnt='%d'  where keyword = '%s' " % (suffix, old)
                        cursor.execute(updatesql)
                        dbhandle.commit()

    def ConnectDB(self):
        try:
            _cnx = mysql.connector.connect(user=self.username, password=self.password, host=self.host,
                                           database=self.database, port=self.port)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("ERROR: Something is wrong with your user name or password")
                return -1
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("ERROR: Database does not exist")
                return -1
            else:
                print(err)
                return -1
        return _cnx


if __name__ == '__main__':

    fx = FileProcesses()
    try:
        fx.Replace()
    except Exception as e:
        print("Error when replace String in file !")

