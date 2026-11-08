from random import randint
from aggregation import Creature
from aggregation import damage_calculation


class Goblin(Creature):
    def __init__(self, name, max_hp,hp,max_mp,mp,strength,endurance,intelligence,wisdom):
        super().__init__(name, max_hp, hp, max_mp, mp, strength, endurance, intelligence, wisdom)

    def attack_pattern(self,other):
        attack = randint(1,100)
        if attack > 60:
            print("The goblin flails wildly!!")
            hit = randint(1,100)
            if hit >= 50:
                damage = damage_calculation(self.damage*2,other.defence)
                other.take_damage(damage)
            else:
                print("It misses you and hurts it self as it falls")
                self.hp -=1
        else:
            print("The goblin attacks")
            damage = damage_calculation(self.damage, other.defence)
            other.take_damage(damage)


class Wolf(Creature):
    def __init__(self, name, max_hp,hp,max_mp,mp,strength,endurance,intelligence,wisdom):
        super().__init__(name, max_hp, hp, max_mp, mp, strength, endurance, intelligence, wisdom)

    def attack_pattern(self,other):
        attack = randint(1, 100)
        if attack > 60:
            print("The wolf goes for the jugular!")
            damage = damage_calculation(self.damage*1.5,other.defence)
            other.take_damage(damage)
        else:
            print("The wolf attacks")
            damage = damage_calculation(self.damage, other.defence)
            other.take_damage(damage)

class Giant_rat(Creature):
    def __init__(self, name, max_hp,hp,max_mp,mp,strength,endurance,intelligence,wisdom):
        super().__init__(name, max_hp, hp, max_mp, mp, strength, endurance, intelligence, wisdom)

    def attack_pattern(self, other):
        damage = damage_calculation(self.damage, other.defence)
        other.take_damage(damage)


class Banshee(Creature):
    def __init__(self, name, max_hp,hp,max_mp,mp,strength,endurance,intelligence,wisdom):
        super().__init__(name, max_hp, hp, max_mp, mp, strength, endurance, intelligence, wisdom)

    def attack_pattern(self, other):
        if self.mp > 4:
            attack = randint(1, 100)
            if attack > 70:
                print("The banshee casts a cold spell!")
                damage = damage_calculation(self.magic+2,other.m_defence)
                other.take_damage(damage)
                self.mp -=4
            else:
                print("The banshee tries to grab you!")
                damage = damage_calculation(self.magic*0.8,other.m_defence)
                other.take_damage(damage)
                if damage > 0:
                    print(f"She drains your mp!")
                    other.mp -= 1
        else:
            print("The banshee tries to grab you!")
            damage = damage_calculation(self.magic * 0.8, other.m_defence)
            other.take_damage(damage)
            if damage > 0:
                print(f"She drains your mp!")
                other.mp -= 1


class Skeleton(Creature):
    def __init__(self, name, max_hp,hp,max_mp,mp,strength,endurance,intelligence,wisdom):
        super().__init__(name, max_hp, hp, max_mp, mp, strength, endurance, intelligence, wisdom)

    def attack_pattern(self, other):
        attack = randint(1, 100)
        if attack > 50:
            print("The skeleton slams on you !")
            damage = damage_calculation(self.damage+2,other.defence)
            other.take_damage(damage)
        else:
            print("The skeleton attacks!")
            damage = damage_calculation(self.damage, other.defence)
            other.take_damage(damage)


class Orc(Creature):
    def __init__(self, name, max_hp, hp, max_mp, mp, strength, endurance, intelligence, wisdom):
        super().__init__(name, max_hp, hp, max_mp, mp, strength, endurance, intelligence, wisdom)

    def attack_pattern(self, other):
        print("The orc attacks in rage! It's going berserk!")
        damage = damage_calculation(self.damage,other.defence)
        other.take_damage(damage)
        self.strength +=1
        if damage <=0:
            print("It's attack did nothing for now")


class Lich(Creature):
    def __init__(self, name, max_hp, hp, max_mp, mp, strength, endurance, intelligence, wisdom):
        super().__init__(name, max_hp, hp, max_mp, mp, strength, endurance, intelligence, wisdom)

    def attack_pattern(self, other):
        if self.mp < 4:
            print("The lich tries to grab you with it's bony hands")
            damage = damage_calculation(self.damage, other.defence)
            other.take_damage(damage)
        else:
            attack = randint(1, 100)
            if attack > 70:
                print("The lich tries to drain your energy")
                damage = damage_calculation(self.magic*0.8,other.m_defence)
                other.take_damage(damage)
                self.mp -=5
                if damage >0:
                    if self.hp + damage >= self.max_hp:
                        self.hp = self.max_hp
                    else:
                        self.hp += damage
            elif 20 <= attack <= 70:
                print("The lich launches a dark orb at you")
                damage = damage_calculation(self.magic*1.3,other.m_defence)
                self.mp -=6
                other.take_damage(damage)
            else:
                print("Ice spells are flying all around")
                damage = damage_calculation(self.magic, other.m_defence)
                self.mp -= 4
                other.take_damage(damage)

class Troll(Creature):
    def __init__(self, name, max_hp, hp, max_mp, mp, strength, endurance, intelligence, wisdom):
        super().__init__(name, max_hp, hp, max_mp, mp, strength, endurance, intelligence, wisdom)

    def attack_pattern(self, other):
        if self.hp < self.max_hp:
            print("The troll can regenerate lost health")
            if self.hp +2 >= self.max_hp:
                self.hp = self.max_hp
            else:
                self.hp += 2
        attack = randint(1, 100)
        if attack >80:
            print("It throws a huge boulder at you ")
            damage = damage_calculation(self.damage*1.4, other.defence)
            other.take_damage(damage)
        else:
            print("It attacks with it's club")
            damage = damage_calculation(self.damage, other.defence)
            other.take_damage(damage)

class Wyvern(Creature):
    def __init__(self, name, max_hp, hp, max_mp, mp, strength, endurance, intelligence, wisdom):
        super().__init__(name, max_hp, hp, max_mp, mp, strength, endurance, intelligence, wisdom)

    def attack_pattern(self, other):
        attack = randint(1, 100)
        if attack >60:
            print("The wyvern belches out flames")
            damage = damage_calculation(self.damage+2, (other.defence + other.m_defence)/2)
            other.take_damage(damage)
        else:
            print("The wyvern attacks you with it's claws")
            damage = damage_calculation(self.damage, other.defence)
            other.take_damage(damage)


class Dragon(Creature):
    def __init__(self, name, max_hp, hp, max_mp, mp, strength, endurance, intelligence, wisdom):
        super().__init__(name, max_hp, hp, max_mp, mp, strength, endurance, intelligence, wisdom)
        self.charge = False

    def attack_pattern(self, other):
        if self.charge:
            self.charge = False
            self.endurance -=2
            self.wisdom -=2
            print("The dragon breaths a torrent of flame!")
            damage = damage_calculation((self.damage+self.magic), (other.defence + other.m_defence)/2)
            other.take_damage(damage)
            if damage <=0:
                print("You took cover in time")
        else:
            attack = randint(1, 100)
            if attack > 75:
                print("The dragon takes a deep breath")
                self.charge = True
                self.endurance +=2
                self.wisdom +=2
            elif 25 <= attack <=75:
                print("It attacks with it's claws")
                damage = damage_calculation(self.damage, other.defence)
                other.take_damage(damage)
            else:
                print("It attacks with it's tail")
                damage = damage_calculation(self.damage*1.2, other.defence)
                other.take_damage(damage)



