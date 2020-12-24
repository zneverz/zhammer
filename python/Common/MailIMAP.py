import base64
import imaplib
import email  # 导入两个库22222
mail_user = "irrn_301@hotmail.com"  # 用户名
mail_pass = "doss301301"  # 口令
conn = imaplib.IMAP4_SSL(port='993', host='imap-mail.outlook.com')
print('已连接服务器')
conn.login(mail_user, mail_pass)
print('已登陆')


conn.select()
email_count = len(conn.search(None, 'ALL')[1][0].split())
# email_count = 4
print('邮件数量: ', email_count)
conn.select()
typ, email_content = conn.fetch(f'{email_count}'.encode(), '(RFC822)')

# 将邮件内存由byte转成str
email_content = email_content[0][1].decode()

print(email_content)
# print(base64.b64decode(email_content))

# 关闭select
conn.close()

# 关闭连接
conn.logout()