import calendar,datetime

print(calendar.month(2024,5))

print(calendar.isleap(2024))

day_of_week = calendar.weekday(2024,11,19)
print(day_of_week)
def get_nth_monday(year, n):
    for week_number, week in enumerate(calendar.monthcalendar(year, 1), 1):
        if week[0] != 0 and week_number == n:
            return datetime.date(year, 1, week[0])
