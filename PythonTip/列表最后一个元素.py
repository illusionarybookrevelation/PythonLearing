def last_element(my_list):
    # 在此处编写代码
    for i in my_list:
        value = i
    return value

# 获取整数输入，并将其转换为列表
input_list = list(map(int, input().split()))

# 调用函数
print(last_element(input_list))