import datetime

dt1 = datetime.datetime(2024,5,15,10,30,0)
dt2 = datetime.datetime(2024,5,18,15,0,0)

timestamp = dt2.timestamp() - dt2.timestamp()

dt = datetime.datetime.fromtimestamp(timestamp)

print(f"时间差为: {datetime.datetime.strftime(dt,'%d %H:%M')}")