import itertools

# 多参返单
for i in itertools.chain(["红尘来去散无痕","对酒当歌思故人"],["不见千里万里","悲欢与爱恨"]):
    print(i)

# 定向输出
ns = itertools.compress(["苹果","香蕉","橙子","西瓜"],[1,False,0,3])
for j in ns:
    print(j)

# 以假乱真
for f in itertools.dropwhile(lambda x:x>10,[20,30,10,8,3,6]):
    print(f)
print()
for h in itertools.filterfalse(lambda x:x>9,[20,30,10,8,3,6]):
    print(h)
print()

# 以真为真
for f in itertools.takewhile(lambda x:x>10,[20,30,10,8,3,6]):
    print(f)

# 重复
for its in itertools.tee([20,30,10],4):
    for it in its:
        print(it)


