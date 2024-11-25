import time

def timer(func):
    def war(*args,**kwargs):
        last = time.time()
        result = func(*args,**kwargs)
        after = time.time()
        print(f'函数{func.__name__}，执行时间{after - last:.4f}')
        return result
    return war

@timer
def good_time():
    time.sleep(4)
    print("函数执行完毕")

if __name__ == '__main__':
    good_time()