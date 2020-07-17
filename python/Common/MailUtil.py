#!/usr/bin/python3

import smtplib
from email.mime.text import MIMEText
from email.header import Header


mail_host = "smtp.office365.com"  # 设置服务器
mail_user = "ewcn_app@eastwestbank.com.cn"  # 用户名
mail_pass = "abcd@1234"  # 口令

sender = 'ewcn_app@eastwestbank.com.cn'
receivers = ['ewcn_app@eastwestbank.com.cn']

message = MIMEText('test...', 'plain', 'utf-8')
message['From'] = Header("test", 'utf-8')
message['To'] = Header("test", 'utf-8')

subject = 'Python 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 443)
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