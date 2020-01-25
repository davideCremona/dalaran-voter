from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('interval', seconds=3)
def timed_job():
    print('This job is run every three seconds.')
