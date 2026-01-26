from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()

scheduler.add_job(
    lambda: print("Hello, World!"),
    "interval",
    seconds=10,
)

scheduler.start()
