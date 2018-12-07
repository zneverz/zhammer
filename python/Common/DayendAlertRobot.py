import datetime
import imaplib
import email
import subprocess
import traceback
import time


class MailRobot(object):

    def __init__(self):
        self.imap_host = 'imap.mxhichina.com'
        self.imap_port = '993'
        self.login_id = 'tong.jia@detvista.com'
        self.login_pass = 'Tong12121212'
        self.conn = ''
        self.login()
        self.appscript = '''
            do shell script "open facetime://+8618939933901"
            tell application "System Events"
                repeat while not (button "呼叫" of window 1 of application process "FaceTime" exists)
                    delay 1
                end repeat
                click button "呼叫" of window 1 of application process "FaceTime"
            end tell
            '''

    def callfacetime(self):
        args = [item for x in [("-e", l.strip()) for l in self.appscript.split('\n') if l.strip() != ''] for item in x]
        subprocess.Popen(["osascript"] + args, stdout=subprocess.PIPE)

    def login(self):
        try:
            self.conn = imaplib.IMAP4_SSL(port=self.imap_port, host=self.imap_host)
            print(str(datetime.datetime.now()) + '  Connect MailServer Success')
            self.conn.login(self.login_id, self.login_pass)
            print(str(datetime.datetime.now()) + '  Login MailBox Success')
        except Exception as e:
            print(str(datetime.datetime.now()) + '  Login Failed', traceback.format_exc())

    def check(self):
        self.conn.select(mailbox='GafcDayEnd')
        typ, data = self.conn.search(None, 'UNSEEN')
        newlist = data[0].split()

        typ, data = self.conn.fetch(newlist[0], '(RFC822)')

        msg = email.message_from_string(data[0][1].decode('utf-8'))
        sub = msg.get('subject')
        subdecode = email.header.decode_header(sub)[0][0].decode('utf-8')

        print('subject', subdecode)

        self.conn.store(newlist[0], '+FLAGS', '\Seen')
        return subdecode


if __name__ == '__main__':
    print('Hello Im Mail Robot')
    while True:
        robot = MailRobot()
        subjectstr = ''

        try:
            subjectstr = robot.check()
        except IndexError as e:
            print(str(datetime.datetime.now()) + '  *** There is no unread mail ... ')

        if subjectstr.upper().find('ERROR') >= 0:
            robot.callfacetime()

        time.sleep(10)
