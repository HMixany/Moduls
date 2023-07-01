is_access = None
message = "Welcome" if is_access else "Forbidden" #значение message зависит от логической переменной is_access. 
#Если is_access = True, то message = Welcome,а если False, то Forbidden

some_data = None
message = some_data or "Not data" #короткий вариант. message содержит значение Not data пока some_data None 