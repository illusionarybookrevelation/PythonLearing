def join_first_last(input_str):
    # 在此处编写你的代码
    str1=input_str[0]
    num=len(input_str)
    str2=input_str[num-1]
    return str1 + str2

# 输入字符串
given_string = input()

# 调用函数
print(join_first_last(given_string))