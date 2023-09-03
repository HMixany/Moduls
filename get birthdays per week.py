from datetime import datetime, date, timedelta
from collections import defaultdict


def get_birthdays_per_week(users):
    #    result = {}
    week = ['Понеділок', 'Вівторок', 'Середа', 'Четвер', "П'ятниця", 'Субота', 'Неділя']
    result = defaultdict(list)

    today = date.today()
    final_date = today + timedelta(weeks=1)

    for user in users:
        curent = datetime(today.year, user['birthday'].month, user['birthday'].day).date()
        print(curent)
        print(curent.strftime('%A'))
        if today <= curent < final_date:
            if curent.strftime('%A') in ('Saturday', 'Sunday'):
                if today.strftime('%A') == 'Monday':
                    continue
                result['Monday'].append(user['name'])
            #                if 'Monday' in result:
            #                    result['Monday'].append(user['name'])
            #                else:
            #                    result['Monday'] = [(user['name'])]
            else:
                result[curent.strftime('%A')].append(user['name'])
    #                if curent.strftime('%A') in result:
    #                    result[curent.strftime('%A')].append(user['name'])
    #                else:
    #                    result[curent.strftime('%A')] = [(user['name'])]

    return result


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
         {'name': 'Vasya', 'birthday': datetime(1977, 8, 28).date()},
         {'name': 'Petya', 'birthday': datetime(1971, 8, 29).date()},
         {'name': 'Slava', 'birthday': datetime(1980, 8, 30).date()},
         {'name': 'Sasha', 'birthday': datetime(1990, 8, 31).date()},
         {'name': 'Vova', 'birthday': datetime(1979, 9, 1).date()},
         {'name': 'Oleg', 'birthday': datetime(1980, 9, 2).date()},
         {'name': 'Dima', 'birthday': datetime(1980, 9, 3).date()},
         {'name': 'Evgen', 'birthday': datetime(1980, 9, 4).date()},
         {'name': 'Vitaliy', 'birthday': datetime(1980, 9, 5).date()}]

print(get_birthdays_per_week(users))
