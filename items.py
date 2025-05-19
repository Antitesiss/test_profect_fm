from random import randint

# Еда
APPLE = {
    'type': 'food',
    'name': 'яблоко',
    'value': randint(5, 10),
}

BREAD = {
    'type': 'food',
    'name': 'хлеб',
    'value': randint(10, 15),
}

MEAT = {
    'type': 'food',
    'name': 'мясо',
    'value': randint(20, 30),
}

# Строительные материалы
WOODEN = {
    'type': 'build',
    'name': 'древесина',
    'value': randint(1, 10)
}

STONE = {
    'type': 'build',
    'name': 'камень',
    'value': randint(5, 20),
}

NAILS = {
    'type': 'build',
    'name': 'гвозди',
    'value': randint(3, 8),
}

# Оружие для атаки
SWORD = {
    'type': 'attack',
    'name': 'меч',
    'value': randint(20, 100),
}

BOW = {
    'type': 'attack',
    'name': 'лук',
    'value': randint(25, 70),
}

DAGGER = {
    'type': 'attack',
    'name': 'кинжал',
    'value': randint(15, 40),
}

# Защита
SHIELD = {
    'type': 'defend',
    'name': 'щит',
    'value': randint(10, 50),
}

ARMOR = {
    'type': 'defend',
    'name': 'доспехи',
    'value': randint(30, 60),
}

HELMET = {
    'type': 'defend',
    'name': 'шлем',
    'value': randint(10, 30),
}

class Item:
    def __init__(self, name):
        self.name = name
        self.__value = 0

    def use(self):
        return self.__value

class BuildItem(Item):
    def __init__(self, name, value):
        super().__init__(name)
        if value is None:
            value = randint(1, 20)
        self.__value = value

    def use(self):
        return self.__value

wood = BuildItem("Дерево", 10)
print(wood.use())

class Person:
    def __init__(
        self,
        name: str,
        health: int = 100,
        attack: int = 10,
        armor: int = 5,
        money: float = 0.0,
        inventory: list = None,
        character_class: str = "commoner",
    ):
        self.name = name
        self.health = max(health, 0)  # Здоровье не может быть отрицательным
        self.attack = attack
        self.armor = armor
        self.money = money
        self.inventory = inventory if inventory is not None else []
        self.character_class = character_class
        self.alive = self.health > 0  # Автоматически определяется на основе здоровья


    def increase_money(self, value):
        self.value = value
        self.money = self.money + value
        print(f"Заработано {value} руб. Осталось: {self.money} руб.")

    def decrease_money(self, value):
        self.value = value
        if value > self.money:
            print("У тебя нет денег.")
        else:
            self.money = self.money - self.value
            print(f"Потрачено {value} руб. Осталось: {self.money} руб.")

    def __str__(self):
        return (
            f"Person(name='{self.name}', "
            f"health={self.health}, "
            f"attack={self.attack}, "
            f"armor={self.armor}, "
            f"money={self.money}, "
            f"inventory={self.inventory}, "
            f"character_class='{self.character_class}', "
            f"alive={self.alive})"
        )

character = Person(
    name="Ичиго",
    health=150,
    attack=100,
    armor=20,
    money=0.0,
    inventory=["дзанпакто","удостоверение шинигами"],
    character_class="shinigami",
)

print(character)