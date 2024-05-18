# Шаг 1: Создаем абстрактный класс для оружия
from abc import ABC, abstractmethod


class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


# Шаг 2: Реализуем конкретные типы оружия
class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."


class Bow(Weapon):
    def attack(self):
        return "Боец наносит удар из лука."


# Шаг 3: Модифицируем класс Fighter
class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def changeWeapon(self, weapon):
        self.weapon = weapon

    def attack(self):
        if self.weapon:
            return self.weapon.attack()
        else:
            return "Боец не имеет оружия."


# Шаг 4: Реализация боя
class Monster:
    def __init__(self, name):
        self.name = name

    def is_defeated(self):
        return True  # Для упрощения всегда побежден


# Демонстрация
def main():
    # Создаем бойца и монстра
    fighter = Fighter("Герой")
    monster = Monster("Дракон")

    # Боец выбирает меч
    sword = Sword()
    fighter.changeWeapon(sword)
    print(fighter.attack())
    if monster.is_defeated():
        print("Монстр побежден!\n")

    # Боец выбирает лук
    bow = Bow()
    fighter.changeWeapon(bow)
    print(fighter.attack())
    if monster.is_defeated():
        print("Монстр побежден!\n")

    # Можно легко добавить новое оружие без изменения существующего кода бойца и механизма боя
    class Axe(Weapon):
        def attack(self):
            return "Боец наносит удар топором."

    # Боец выбирает топор
    axe = Axe()
    fighter.changeWeapon(axe)
    print(fighter.attack())
    if monster.is_defeated():
        print("Монстр побежден!\n")


if __name__ == "__main__":
    main()
