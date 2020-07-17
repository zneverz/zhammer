import poplib

# 输入邮件地址, 口令和POP3服务器地址:
from email.parser import Parser

from notebook.notebookapp import raw_input

email = "tong.jia@detvista.com"
password = "123123123"
pop3_server = "pop3.mxhichina.com"

# 连接到POP3服务器:
server = poplib.POP3(pop3_server)
# 可以打开或关闭调试信息:
# server.set_debuglevel(1)
# 可选:打印POP3服务器的欢迎文字:
print(server.getwelcome())
# 身份认证:
server.user(email)
server.pass_(password)
# stat()返回邮件数量和占用空间:
print('Messages: %s. Size: %s' % server.stat())
# list()返回所有邮件的编号:
resp, mails, octets = server.list()
# 可以查看返回的列表类似['1 82923', '2 2184', ...]
print(mails)
server.quit()