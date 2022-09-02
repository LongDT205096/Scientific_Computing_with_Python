def time_cal(start, duration, days = False):
    #example : time_cal("11:43 PM", "24:20", "Tuesday")
    # return time = 12:03 AM, Thursday (2 days later)

    days_of_week_index = {
        "Monday" : 0,
        "Tuesday": 1,
        "Wednesday": 2,
        "Thursday" : 3,
        "Friday": 4,
        "Saturday": 5,
        "Sunday": 6
    }

    days_of_week = [
        "Monday" ,
        "Tuesday",
        "Wednesday",
        "Thursday" ,
        "Friday",
        "Saturday",
        "Sunday",
    ]

    start_tuple = start.partition(":")
    start_hour = int(start_tuple[0])
    start_tuple_min = start_tuple[2].partition(" ")
    start_min = int(start_tuple_min[0])
    am_or_pm = start_tuple_min[2]
    am_or_pm_dict = {
        "AM" : "PM",
        "PM" : "AM"
    }

    duration_tuple = duration.partition(":")
    add_hour = int(duration_tuple[0])
    add_minnute = int(duration_tuple[2])

    end_minute = start_min + add_minnute
    if end_minute >= 60:
        end_minute = end_minute % 60
        start_hour = start_hour + 1
    end_minute = str(end_minute) if end_minute > 9 else "0" + str(end_minute)

    end_hour = (start_hour + add_hour) % 12
    end_hour = 12 if end_hour == 0 else end_hour
    end_hour = str(end_hour) if end_hour > 9 else "0" + str(end_hour)

    time = end_hour + ":" + end_minute + " " + am_or_pm

    amount_days = round(add_hour/24)
    if am_or_pm == "PM" and (start_hour + (add_hour % 12)) >= 12:
        amount_days += 1

    if days:
        index = days_of_week_index[days] + amount_days
        new_day = days_of_week[index]
        time += ", " + new_day

    if amount_days == 1:
        days_time = "(next day)"
    elif amount_days > 1:
        days_time = "(" + str(amount_days) + " day later" + ")" 

    am_or_pm = am_or_pm_dict[am_or_pm] if (int(start_hour) + int(add_hour)) >= 12 else am_or_pm
    time += " " + days_time
    return time

print(time_cal("10:10 PM", "3:30"))
print(time_cal("11:43 PM", "24:20", "Tuesday"))
print(time_cal("6:30 PM", "205:12"))