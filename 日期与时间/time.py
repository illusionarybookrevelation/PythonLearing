import time

# 获取当前时间的时间戳
timestamp = time.time()
print(timestamp)

# 将时间戳转换为本地时间元组
local_time = time.localtime(timestamp)
print(local_time)

# 格式化时间输出
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
print(formatted_time)

# 睡眠2秒
time.sleep(2)

# 测量代码执行时间
start_time = time.perf_counter()
# ... 执行一些代码 ...
end_time = time.perf_counter()
print(f"代码执行时间：{end_time - start_time}秒")