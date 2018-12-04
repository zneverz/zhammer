class FileHandleApi:

    def ReadFileGbk(self, path):
        fp = open(path, 'r', encoding='gbk')
        return fp

    def ReadFileUtf8(self, path):
        fp = open(path, 'r', encoding='utf8')
        return fp

    def WriteFileGbk(self, path):
        fp = open(path, 'w', encoding='gbk')
        return fp

    def WriteFileUtf8(self, path):
        fp = open(path, 'w', encoding='utf8')
        return fp

    def AddFileGbk(self, path):
        fp = open(path, 'a', encoding='gbk')
        return fp

    def AddFileUtf8(self, path):
        fp = open(path, 'a', encoding='utf8')
        return fp