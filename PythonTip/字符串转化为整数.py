def convert_to_int(str_number):
    # 在此处编写你的代码
    string=int(str_number)
    return string

# 获取字符串输入
input_string = input()

result = convert_to_int(input_string)

# 打印结果的类型
print(type(result))