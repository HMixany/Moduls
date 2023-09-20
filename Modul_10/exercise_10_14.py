'''
Реалізуємо клас Contacts, який працюватиме з контактами. На першому етапі ми додамо два методи.

list_contacts повертає список контактів це змінна contacts з поточного екземпляра класу
add_contacts додає новий контакт до списку, який є змінною об'єкту - contacts
Клас Contacts містить змінну класу current_id. Ми будемо використовувати її при додаванні нового контакту як
унікального ідентифікатора контакту. Коли ми додаємо новий контакт, то передаємо такі аргументи в метод
add_contacts: name, phone, email та favorite. Метод повинен створити словник із зазначеними ключами та
значеннями параметрів функції. Також необхідно додати до словника новий ключ id, значенням якого є значення
змінної класу current_id.

Приклад отриманого словника:

    {
    "id": 1,
    "name": "Wylie Pope",
    "phone": "(692) 802-2949",
    "email": "est@utquamvel.net",
    "favorite": True,
}
Вказаний словник ми додаємо до списку contacts. Не забуваймо збільшувати змінну current_id на одиницю після кожного
виклику методу add_contacts для збереження унікальності ключа id для словника.
'''

class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        self.data = {'id': Contacts.current_id,
                     'name': name,
                     'phone': phone,
                     'email': email,
                     'favorite': favorite}
        self.contacts.append(self.data)
        Contacts.current_id += 1