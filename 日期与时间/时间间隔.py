import datetime

now = datetime.datetime.now()

time_delta = datetime.timedelta(days=3)

force = now + time_delta

print(f"三天后: {datetime.datetime.strftime(force,'%Y-%m-%d %H:%M:%S')}")
