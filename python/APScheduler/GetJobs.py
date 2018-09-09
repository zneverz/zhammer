from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.base import BaseScheduler

basesch = BaseScheduler()
print('print jobs vvvvvvvvvv ')
basesch.print_jobs()
print('print jobs ^^^^^^^^^^ ')
print('get jobs   vvvvvvvvvv ')
basesch.get_job()
print('get jobs   ^^^^^^^^^^ ')
print('This job is run every 5 seconds.')