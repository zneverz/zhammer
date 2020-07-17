from exchangelib import FileAttachment

credentials = ServiceAccount(username='域名\用户名', password='密码')
account = Account('邮箱', credentials=credentials, autodiscover=True)
print('1.邮箱连接成功')

for item in account.inbox.children:
    print('2.文件夹名称:'+item.name)
    if item.name=='Reports':#只要Reports文件夹下的附件
        index=0
        totalcount=0
        page=0
        while True:          
            for model in item.all()[page:page+50]:
                index=index+1
                print(str(index)+'-开始:'+model.subject)
                for attachment in model.attachments:
                    if isinstance(attachment, FileAttachment):
                        with open('/Users/cavin/Desktop/files/' + attachment.name, 'wb') as f:
                            f.write(attachment.content)
            if totalcount==index:
                break
            page=page+50
            totalcount=index