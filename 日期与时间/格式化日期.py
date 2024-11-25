from datetime import datetime

date_str = "2024-11-17 14:30:45"

dt = datetime.strptime(date_str,"%Y-%m-%d %H:%M:%S")

def get_day__suffix(day):
    if 11 <= day <= 13:
        return "th"
    elif day % 10 == 1:
        return "st"
    elif day % 10 == 2:
        return "nd"
    elif day % 10 ==3:
        return "rd"
    else:
        return "th"

day_suffix = get_day__suffix(dt.day)

formatted_date = f"{dt.day}{day_suffix} {dt.strftime('%B %Y')},{dt.strftime('%I:%M %p')}"

print(formatted_date)