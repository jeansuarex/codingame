s = input().split()
month, day, weekday = s[0], int(s[1]) * -1, s[-1]
final_day = 30 if month in ["April", "June", "September", "November"] else 31
days = "Monday Tuesday Wednesday Thursday Friday Saturday Sunday".split()
index = days.index(weekday)
count_days = 1 
if weekday in ["Sunday", "Saturday"] and day == -1:
    count_days = 2 if weekday == "Sunday" else 3
    weekdays = 0
weekdays = (7+(day+1+index)) % 7
if days[weekdays] in ["Sunday", "Saturday"]:
    count_days = 2 if days[weekdays] == "Sunday" else 3
    weekdays = 0
while count_days <= final_day:
    firstday = days[weekdays]
    print(f"{firstday}, {month} {count_days}")
    weekdays+=1
    count_days += 1
    if weekdays > 4:
        weekdays = 0
        count_days += 2

#This code is not the best solution, so I hope you can do it better than me.