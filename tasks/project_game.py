import random


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    # Ссылка на список и ссылка
    def hit(self, boss, heroes):
        pass

    def __str__(self):
        return f'Name: {self.__name} Health: {self.health} Damage: {self.damage}'


# __ health обращение к конструктору health обпащение к гет


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        GameEntity.__init__(self, name, health, damage)

    def hit(self, boss, heroes):
        for hero in heroes:
            if boss.health > 0 and hero.health > 0:
                hero.health = hero.health - boss.damage
                if hero.health <= 0:
                    hero.health = 0


class Hero(GameEntity):
    def __init__(self, name, health, damage, super_ability):
        GameEntity.__init__(self, name, health, damage)
        self.__super_ability = super_ability

    @property
    def super_ability(self):
        return self.__super_ability

    def apply_super_ability(self, boss, heroes):
        pass

    def hit(self, boss):
        if boss.health > 0 and self.health > 0:
            boss.health = boss.health - self.damage
            if boss.health <= 0:
                boss.health = 0


class Berserk(Hero):
    def __init__(self, name, health, damage, super_ability=0):
        Hero.__init__(self, name, health, damage, 'ULTA')
        self.__super_ability = super_ability

    @property
    def super_ability(self):
        return self.__super_ability

    @super_ability.setter
    def super_ability(self, value):
        self.__super_ability = value

    def apply_super_ability(self, boss, heroes):
        if boss.health > 0 and self.health > 0:
            if beresrk

class Warrior(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, 'CRITICAL_DAMAGE')

    def apply_super_ability(self, boss, heroes):
        pass


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        Hero.__init__(self, name, health, damage, 'HEAL')
        self.__heal_points = heal_points

    def apply_super_ability(self, boss, heroes):
        if boss.health > 0 and self.health > 0:
            for hero in heroes:
                if hero.health > 0 and self != hero:
                    hero.health = hero.health + self.__heal_points


class Magic(Hero):

    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, 'BOOST')

    def apply_super_ability(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0:
                hero.damage = hero.damage + 5


# функции

round_number = 0


def print_statistics(boss, heroes):
    print(f'{round_number} ROUND -----------------')
    print(boss)
    for hero in heroes:
        print(hero)


def is_game_finished(boss, heroes):
    if boss.health <= 0:
        print('Heroes won')
        return True

    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print('Boss Won!!!')
    return all_heroes_dead


def round(boss, heroes):
    global round_number
    round_number += 1
    boss.hit(boss, heroes)
    for hero in heroes:
        hero.hit(boss)
        hero.apply_super_ability(boss, heroes)
    print_statistics(boss, heroes)


def start():
    # вызов контруктора внутри функции
    boss = Boss('OverLord', random.randint(700, 1000), 50)

    warrior = Warrior('Soup', random.randint(230, 300), 4)
    berserk = Berserk('Berserk', 155, 5)
    medic = Medic('Dog', random.randint(180, 260), 5, 15)
    medic1 = Medic('pavel', random.randint(250, 260), 15, 5)
    magic = Magic('Samuel', random.randint(250, 300), 20)
    heroes = [warrior, berserk, medic, medic1, magic]

    print_statistics(boss, heroes)

    while not is_game_finished(boss, heroes):
        round(boss, heroes)


start()