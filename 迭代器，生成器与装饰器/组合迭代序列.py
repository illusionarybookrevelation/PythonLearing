import itertools

# 全排列
for i in itertools.product(["你好呀","你干嘛"],["拜只拜我千秋","荒唐这一回"]):
    print(i)

# 迭代序列中元素排列组合
for j in itertools.permutations("ABC",3):
    print(j)

#迭代序列中元素的组合
for g in itertools.combinations("ABCD",4):
    print(g)
