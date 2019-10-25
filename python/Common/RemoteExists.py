import subprocess

status = subprocess.call(['ssh', 'dmpapp@10.20.202.161', 'rm -rf /home/dmpapp/1.txt'])
if status == 0:
    print('成功')
else:
    print('有问题了')

