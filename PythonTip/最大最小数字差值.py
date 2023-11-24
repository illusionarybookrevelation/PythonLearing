def difference_max_min(list_nums):
    # 在此处编写代码
    max = list_nums[0]
    min = list_nums[0]
    for i in list_nums:
        if i > max:
            max = i
        elif i < min:
            min = i
    sum = max - min
    return sum

# 输入整数，并将其转换为列表
numbers = list(map(int, input().split()))

# 调用函数
print(difference_max_min(numbers))