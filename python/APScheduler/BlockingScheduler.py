from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()


@sched.scheduled_job('interval', seconds=3)
def timed_job():
    print('This job is run every three seconds.')


@sched.scheduled_job('cron', day_of_week='mon-fri', hour='0-9', minute='30-59', second='*/3')
def scheduled_job():
    print('本任务模仿cron来执行的，在周一到周五其间，每天的０点到９点直接，在３０分到５９分之间执行，执行频次为３秒.')


print('before the start funciton')
sched.start()
print("let us figure out the situation")
