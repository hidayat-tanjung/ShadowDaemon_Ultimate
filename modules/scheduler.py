import schedule
import time

def run_at(hour, minute, command):
    schedule.every().day.at(f"{hour:02d}:{minute:02d}").do(
        lambda: execute_command(command)
    )

def run_every(interval, unit, command):
    if unit == "seconds":
        schedule.every(interval).seconds.do(lambda: execute_command(command))
    elif unit == "minutes":
        schedule.every(interval).minutes.do(lambda: execute_command(command))
    elif unit == "hours":
        schedule.every(interval).hours.do(lambda: execute_command(command))

def scheduler_loop():
    while True:
        schedule.run_pending()
        time.sleep(1)