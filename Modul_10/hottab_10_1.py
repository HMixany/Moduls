class Character:
    name = None
    x = None
    y = None
    xp = 100
    mp = 100

    def identify(self):
        return self


char = Character()  # сохраняем в char экземпляр класса Character
print(char)
print(char.name)
char_1 = Character()
print(char_1)
char.name = 'Edelveis'
Character.name = 'Other'  # Присваеваем классовому полю значение. Если в экземпляре значение не менялось, то будет таким
print(char.name)
print(char_1.name)
# --------------------------------------------------------------------------------------------
print(char)
print(char.identify())
