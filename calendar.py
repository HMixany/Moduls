from datetime import datetime, date, timedelta

week = {'Пн': [], 'Вт': [], 'Ср': [], 'Чт': [], 'Пт': [], 'Сб': [], 'Вс': []}
oclad = 10146
# today = date.today()
today = datetime(2023, 10, 1)
start_date = datetime(today.year, 1, 1).date()
end_date = datetime(today.year, 12, 31).date()
current = datetime(today.year, today.month, 1).date()

current_month = current.month
# print(current.strftime('%W'))
start_week = current.strftime('%W')
while current_month == current.month:
    match current.weekday():
        case 0:
            if len(week['Пн']) == 0 and current.strftime('%W') != start_week:
                week['Пн'].append(' ')
            week['Пн'].append(current.day)
        case 1:
            if len(week['Вт']) == 0 and current.strftime('%W') != start_week:
                week['Вт'].append(' ')
            week['Вт'].append(current.day)
        case 2:
            if len(week['Ср']) == 0 and current.strftime('%W') != start_week:
                week['Ср'].append(' ')
            week['Ср'].append(current.day)
        case 3:
            if len(week['Чт']) == 0 and current.strftime('%W') != start_week:
                week['Чт'].append(' ')
            week['Чт'].append(current.day)
        case 4:
            if len(week['Пт']) == 0 and current.strftime('%W') != start_week:
                week['Пт'].append(' ')
            week['Пт'].append(current.day)
        case 5:
            if len(week['Сб']) == 0 and current.strftime('%W') != start_week:
                week['Сб'].append(' ')
            week['Сб'].append(current.day)
        case 6:
            if len(week['Вс']) == 0 and current.strftime('%W') != start_week:
                week['Вс'].append(' ')
            week['Вс'].append(current.day)
    current += timedelta(days=1)

# print(week)
head_month = today.strftime('%B')
print(head_month.center(20, ' '))
for key, value in week.items():
    if len(value) < 5:
        value.append(' ')
    print('{:<3} {:^2} {:^2} {:^2} {:^2} {:^2}'.format(key, value[0], value[1], value[2], value[3], value[4]))
# print('{:<3} {:^10} {:>10}'.format('Пн', 'center', 'right'))  # |left      |**center**|     right
current = today
day = []
night = []
start_date = datetime(2023, 1, 1).date()
start_night = datetime(2023, 1, 3).date()
current = start_date
while current.year == today.year:
    # print(current)
    day.append(current)
    current = current + timedelta(days=4)
    night.append(start_night)
    start_night += timedelta(days=4)
print(day)
print(night)
print(start_date)
current_days_month = list(filter(lambda x: x.month == today.month, day))
current_nights_month = list(filter(lambda x: x.month == today.month, night))
total_hours_plan = len(current_days_month) * 12 + len(current_nights_month) * 12
# current_days_month.remove(datetime(2023, 8, 17).date())
# current_days_month.remove(datetime(2023, 8, 21).date())
# current_nights_month.remove(datetime(2023, 8, 19).date())
# print(datetime(2023, 8, 19).date() in current_days_month)
print([f'{d.day}' for d in current_days_month])
print([f'{n.day}' for n in current_nights_month])
total_hours = len(current_days_month) * 12 + len(current_nights_month) * 12
total_evening = len(current_days_month) * 1 + len(current_nights_month) * 3
total_night = len(current_nights_month) * 8
print(f'{total_hours_plan = }')
print(f'{total_hours = }')
print(f'{total_evening = }')
print(f'{total_night = }')
sum_oclad = (oclad / total_hours_plan) * total_hours
sum_night = (oclad / total_hours_plan) * 0.4 * total_night
sum_evening = (oclad / total_hours_plan) * 0.2 * total_evening
print(sum_oclad)
print(sum_night)
print(sum_evening)
