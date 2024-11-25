import itertools

# 无限计数
for i in itertools.count(10,2):
    if i > 30:
        break
    print(i)

# 循环列表
count = 0
for j in itertools.cycle(["apple","banana","orange"]):
    if count >= 6:
        break
    print(j)
    count += 1

# 循环定格
for f in itertools.repeat(["梦中熙熙笑阵阵，梦外凄凄风冷冷"],4):
    print(f)
