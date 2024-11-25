def aa(fun):
    def ww(*args,**kwargs):
        print("开始运行...")
        fun(*args,**kwargs)
        print("运行结束！")
    return ww

@aa
def dd(x):
    a = []
    for i in range(x):
        a.append(i)
    print(a)

@aa
def hh(n):
    print("最喜欢的水果是:   ",n)

if __name__ == '__main__':
    dd(6)
    print()
    hh('苹果')