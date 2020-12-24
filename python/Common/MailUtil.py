#!/usr/bin/python3

import smtplib
from email.mime.text import MIMEText
from email.header import Header


mail_host = "smtp.163.com"  # 设置服务器
mail_user = "iridium_301@163.com"  # 用户名
mail_pass = "KUURFSRTDXPFNIQA"  # 口令

sender = 'iridium_301@163.com'
receivers = ['iridium_301@163.com']

message = MIMEText('test...', 'plain', 'utf-8')
message['From'] = Header("test", 'utf-8')
message['To'] = Header("test", 'utf-8')

subject = 'Python 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    print("Connect 1 ...")
    smtpObj.connect(mail_host, 465)
    print("Connect 2 ...")
    smtpObj.ehlo()
    smtpObj.starttls()
    print("Connect Success ...")
    smtpObj.login(mail_user, mail_pass)
    print("Login Success ...")
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("Mail Sent")
except smtplib.SMTPException as e:
    print(e)
    print("Error: Mail Send Failed")