import smtplib
from email.mime.text import MIMEText

smtp_ssl_host = 'smtp.mxhichina.com'
smtp_ssl_port = 465
username = 'tong.jia@detvista.com'
password = 'Tong12121212'
sender = 'tong.jia@detvista.com'
targets = ['tong.jia@detvista.com']

msg = MIMEText('Hi, how are you today?')
msg['Subject'] = 'Hello'
msg['From'] = sender
msg['To'] = ', '.join(targets)

server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
server.login(username, password)
server.sendmail(sender, targets, msg.as_string())
server.quit()