from exchangelib import Account, Credentials, DELEGATE, Configuration


class MailExchange(object):
    def test(self):
        cred = Credentials('ewcn_app@eastwestbank.com.cn', 'abcd@1234')
        conf = Configuration(credentials=cred, server='outlook.office365.com')
        account = Account('ewcn_app@eastwestbank.com.cn',
                          credentials=cred,
                          config=conf,
                          autodiscover=False,
                          access_type=DELEGATE)

        for item in account.inbox.all().order_by('-datetime_received')[:100]:
            print(item.subject, item.sender, item.datetime_received)


if __name__ == "__main__":
    MailExchange().test()
