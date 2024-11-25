from datetime import datetime

date1_str = input("请输入第一个日期(格式：YYYY-MM-DD):")
date2_str = input("请输入第二个日期(格式：YYYY-MM-DD):")

try :
    date1 = datetime.strptime(date1_str,"%Y-%m-%d").date()
    date2 = datetime.strptime(date2_str,"%Y-%m-%d").date()
except ValueError:
    print("输入的日期格式错误，请按照 YYYY-MM-DD 格式输入")
    exit()

difference = abs((date2-date1).days)

print(f"两个日期之差为{difference}天")


