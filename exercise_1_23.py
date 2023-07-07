# Input - 5000
# Otput_hours - 1
# Otput_minutes - 23
# Otput_seconds - 20
time = int(input('Enter time '))
hours = time // 3600
time -= hours * 3600
minut = time // 60
seconds = time % 60
print(f'Output_hours {hours}\nOutput_minutes {minut}\nOutput_seconds {seconds}')