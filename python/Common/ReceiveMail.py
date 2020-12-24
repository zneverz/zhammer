import poplib

# 输入邮件地址, 口令和POP3服务器地址:
from email.parser import Parser

from notebook.notebookapp import raw_input

email = "iridium_301@163.com"
password = "KUURFSRTDXPFNIQA"
pop3_server = "pop3.163.com"

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
print(mails)
server.quit()