from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.base import BaseScheduler

sched = BlockingScheduler()



@sched.scheduled_job('interval', seconds=3)
def timed_job():
    print('This job is run every three seconds.')


# @sched.scheduled_job('interval', seconds=5)
# def show_jobs():
#     basesch = BaseScheduler()
#     print('print jobs vvvvvvvvvv ')
#     basesch.print_jobs()
#     print('print jobs ^^^^^^^^^^ ')
#     print('get jobs   vvvvvvvvvv ')
#     basesch.get_job()
#     print('get jobs   ^^^^^^^^^^ ')
#     print('This job is run every 5 seconds.')


@sched.scheduled_job('cron', day_of_week='mon-fri', hour='0-9', minute='30-59', second='*/3')
def scheduled_job():
    print('本任务模仿cron来执行的，在周一到周五其间，每天的０点到９点直接，在３０分到５９分之间执行，执行频次为３秒.')


print('before the start funciton')
sched.start()
print("let us figure out the situation")
