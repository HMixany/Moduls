from datetime import datetime, date, timedelta


def get_birthdays_per_week(users):
    week = ['Понеділок', 'Вівторок', 'Середа', 'Четвер', "П'ятниця", 'Субота', 'Неділя']
    for user in users:
        print(user['birthday'].weekday())
        print(week[user['birthday'].weekday()])
    today = date.today()



users = [{"name": "Bill Gates", "birthday": datetime(1955, 10, 28).date()},
         {'name': 'Misha', 'birthday': datetime(1983, 9, 6).date()},
         {'name': 'Rafaella', 'birthday': datetime(1985, 2, 25).date()},
         {'name': 'Sofiya', 'birthday': datetime(2016, 2, 1)},
         {'name': 'Katya', 'birthday': datetime(2007, 3, 3).date()}]

print()
get_birthdays_per_week(users)