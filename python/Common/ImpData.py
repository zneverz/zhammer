import os
from time import sleep

fm = 100
to = 1000
step = 100
for i in range(fm, to, step):
    a = "curl -d \"from=%d&to=%d\" \"http://128.196.65.193:8113/api/GRZHXX\" " % (i, i + step - 1)
    print a
    # os.system(a)
    print "finsihed" + a
    sleep(20)
