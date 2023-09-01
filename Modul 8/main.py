from datetime import datetime, date, timedelta


def get_birthdays_per_week(users):
    result = {}
    days_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', "Friday"]

    today = date.today()
#    today = datetime(2023, 12, 26).date()
    delta = datetime(2023, 10, 10).date() - datetime(2023, 10, 3).date()
    final_date = today + delta
    print(today)
    print(final_date)

    for user in users:
        if today.year != final_date.year and user['birthday'].month == 1:
            curent = datetime(final_date.year, user['birthday'].month, user['birthday'].day).date()
        else:
            curent = datetime(today.year, user['birthday'].month, user['birthday'].day).date()
        if today <= curent < final_date:
            if curent.weekday() == 5 or curent.weekday() == 6:
                if result.get(days_week[0]) is None:
                    result[days_week[0]] = [(user['name'])]
                else:
                    result[days_week[0]].append(user['name'])
            else:
                if result.get(days_week[curent.weekday()]) is None:
                    result[days_week[curent.weekday()]] = [(user['name'])]
                else:
                    result[days_week[curent.weekday()]].append(user['name'])
    users = result
    return users


#        print(user['birthday'].weekday())
#        print(week[user['birthday'].weekday()])
#    today = date.today()
#    final_date = today + timedelta(weeks=1)
#    print(today)
#    print(final_date)


users = [{"name": "Bill Gates", "birthday": datetime(1955, 10, 28).date()},
         {'name': 'Misha', 'birthday': datetime(1983, 9, 6).date()},
         {'name': 'Rafaella', 'birthday': datetime(1985, 2, 25).date()},
         {'name': 'Sofiya', 'birthday': datetime(2016, 2, 1).date()},
         {'name': 'Katya', 'birthday': datetime(2007, 3, 3).date()},
         {'name': 'Vasya', 'birthday': datetime(1977, 1, 2).date()},
         {'name': 'Petya', 'birthday': datetime(1971, 12, 29).date()},
         {'name': 'Slava', 'birthday': datetime(1980, 1, 1).date()},
         {'name': 'Sasha', 'birthday': datetime(1990, 8, 31).date()},
         {'name': 'Vova', 'birthday': datetime(1979, 9, 1).date()},
         {'name': 'Oleg', 'birthday': datetime(1980, 9, 2).date()},
         {'name': 'Dima', 'birthday': datetime(1980, 9, 3).date()},
         {'name': 'Evgen', 'birthday': datetime(1980, 9, 4).date()},
         {'name': 'Vitaliy', 'birthday': datetime(1980, 9, 5).date()}]


print(get_birthdays_per_week(users))

