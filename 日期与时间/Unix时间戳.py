import time
from datetime import datetime

timestamp = time.time()

dt_object = datetime.utcfromtimestamp(timestamp)

dt = datetime.strftime(dt_object,"%Y-%m-%d %H:%M:%S")

print(dt)