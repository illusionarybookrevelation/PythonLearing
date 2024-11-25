def MyYield(n):
    while n > 0:
        print("开始生成.....:")
        yield n
        print("生成完毕.....:")
        n -= 1
if __name__ == '__main__':
    for i in MyYield(6):
        print("遍历值: ",i)
    print()
    my_yield = MyYield(3)
    print("已经实例化生成器对象")
    my_yield.__next__()
    print("第二次调用__next__()方法")
    my_yield.__next__()