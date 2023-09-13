class Character:
    def __init__(self, name, x=0, y=0):
        self.left_hand = None
        self.right_hand = None
        self.name = name
        self.x = x
        self.y = y

    def pick_weapon(self, weapon):
        if self.left_hand is None:
            self.left_hand = weapon
        elif self.right_hand is None:
            self.right_hand = weapon
        else:
            print('I am full')

    def show_weapon(self):
        return self.left_hand, self.right_hand

    def move(self):
        print('I am moving')

    def damage_left(self):
        self.left_hand.kick_ass()

    def damage_right(self):
        self.right_hand.kick_ass()

    def die(self):
        return self.left_hand, self.right_hand


class Weapon:
    def __init__(self):
        self.damage = 10

    def kick_ass(self):
        return self.damage


class Knife(Weapon):
    def __init__(self):
        self.damage = 5

    def throw(self):
        return self.damage - 2

    def kick_ass(self):
        print('Chik-chik')
        return self.damage


class Sword(Weapon):
    def __init__(self):
        self.damage = 15

    def kick_ass(self):
        print('Slash-slash')
        return self.damage


class Axe(Weapon):
    def __init__(self):
        self.damage = 20

    def kick_ass(self):
        print('Herak')
        return self.damage


class Gun(Weapon):
    def __init__(self):
        self.damage = 50

    def kick_ass(self):
        print('Baaam')
        return self.damage


char = Character('char')  # создаем персонажа
knife = Knife()  # появляется оружие(ножик)
char.pick_weapon(knife)  # персонаж подбирает оружие
print(char.left_hand)  # что находится в левой руке персонажа
char.damage_left()  # персонаж наносит урон оружием в левой руке
