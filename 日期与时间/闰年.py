from datetime import datetime

date_str = "2024-11-18 10:21:24"

date_year = datetime.strptime(date_str,"%Y-%m-%d %H:%M:%S")
def is_leap_year(year):
    if year % 4 == 0 and year % 100 !=0 or year % 400 == 0:
        print(f"{year}是闰年")
    else:
        print(f"{year}不是闰年")

is_leap_year(date_year.year)