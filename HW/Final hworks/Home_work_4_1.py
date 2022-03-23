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

    def hit(self, boss, heroes):
        pass

    def __str__(self):
        return f'Name: {self.__name} Health: {self.health} Damage: {self.damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage, stan=0):
        GameEntity.__init__(self, name, health, damage)
        self.__stan = stan

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


class Warrior(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, 'CRITICAL_DAMAGE')

    def apply_super_ability(self, boss, heroes):
        pass





class Berserk(Hero):
    def __init__(self, name, health, damage, critic_damage=0):
        Hero.__init__(self, name, health, damage, 'CRITIC_DAMAGE')
        self.__critic_damage = critic_damage

    def apply_super_ability(self, boss, heroes):
        if self.health > 0:
            if self.health - boss.health:
                self.__critic_damage = self.damage + int(boss.damage / 2)
                self.damage = self.__critic_damage


class Thor(Hero):
    def __init__(self, name, health, damage, stan=0):
        Hero.__init__(self, name, health, damage, "Stan")
        self.__stan = stan

    def apply_super_ability(self, boss, heroes):
        if self.health > 0 and round_number % 2 != 0:
            self.damage = self.__stan
        if self.damage == self.__stan:
            boss.damage = 50
        else:
            boss.damage = 0


class Golem(Hero):
    def __init__(self, name, health, damage, protect=0):
        Hero.__init__(self, name, health, damage, "PROTECT")
        self.__protect = protect

    def apply_super_ability(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0:
                # if boss.damage >= 1:
                self.__protect = boss.damage // 5
                if boss.damage >= 1:
                    hero.health = hero.health + self.__protect
                else:
                    hero.health = hero.health - boss.damage


class Witcher(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, 'self')

    def apply_super_ability(self, boss, heroes):
        for hero in heroes:
            if hero.health <= 0:
                hero.health += self.health
                self.health = 0
                self.damage = 0
                break
            if self.damage >= 0:
                self.damage = 0


class Hacker(Hero):
    def __init__(self, name, health, damage, part_boss_heal=0):
        Hero.__init__(self, name, health, damage, 'self')
        self.__part_boss_heal = part_boss_heal

    def apply_super_ability(self, boss, heroes):
        if self.health > 0 and round_number % 2 == 0:
            self.__part_boss_heal = boss.health - random.randint(1300, 1450)

        for hero in heroes:
            if round_number % 2 != 0:
                self.__part_boss_heal + random.randint(hero.health, hero.health)


class TrickyBastard(Hero):
    def __init__(self, name, health, damage, super_ability=random.randint(0,3)):
        Hero.__init__(self, name, health, damage, 'UlTA')

    def apply_super_ability(self, boss, heroes):
        if self.health > 0:
            if self.super_ability == 2:
                self.health += boss.damage-10

#                 Hero Amantur who can hit boss with magic damage with super ability
#                 when hero hit boss then he can his health points up and boost his damage
#                 after hit boss


class Amantur(Hero):
    def __init__(self, name, health, damage, ultimate=0):
        Hero.__init__(self, name, health, damage, 'Ult')
        self.__ultimate = ultimate

    def apply_super_ability(self, boss, heroes):
        if self.health > 0:
            if self.health - boss.health:
                self.__ultimate = boss.health//90
                self.health = self.health + self.__ultimate


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

    boss = Boss('OverLord', random.randint(3300, 3400), 50)

    medic = Medic('Dog', random.randint(90, 100), 5, 10)
    magic = Magic('Samuel', random.randint(180, 220), 20)
    berserk = Berserk('Berserk', 200, 5)
    warrior = Warrior('Soup', random.randint(230, 300), 5)
    medic1 = Medic('pavel', random.randint(250, 260), 15, 5)
    thor = Thor('Thor', random.randint(220, 330), 5)
    golem = Golem('Golem', random.randint(550, 770), 1)
    witcher = Witcher('Witcher', 400, 0)
    hacker = Hacker('Hacker', 220, 1, 1)
    tricky_Bastard = TrickyBastard('TrickyBastard', 200, 5, 0)
    amantur = Amantur('Amantur', 180, 5)
    heroes = [medic, magic, warrior, medic1, berserk, thor, golem, witcher, hacker, tricky_Bastard, amantur]

    print_statistics(boss, heroes)

    while not is_game_finished(boss, heroes):
        round(boss, heroes)


start()


#  For teacher: Thanks for this very interesting task, it was so cool and so hard for me or for all i don't know
#  but it was so interesting and incredable, perhaps i have so many mistakes but i got very expensive thing in this task
#  experiences, it was so interesting that i was sitting on this task two days and one night without sleep
#  Thank you theacher)
