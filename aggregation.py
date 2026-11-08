from random import randrange

class Creature:
    def __init__(self,name,max_hp,hp,max_mp,mp,strength,endurance,intelligence,wisdom):
        self.name = name
        self.max_hp = max_hp
        self.hp = hp
        self.strength = strength
        self.endurance = endurance
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.max_mp = max_mp
        self.mp = mp
    @property
    def damage(self):
        weapon_bonus = self.weapon.damage if hasattr(self,"weapon") else 0
        return self.strength + weapon_bonus

    @property
    def magic(self):
        weapon_bonus = self.weapon.magic if hasattr(self, "weapon") else 0
        return self.intelligence + weapon_bonus

    @property
    def defence(self):
        armor_bonus = self.armor.defence if hasattr(self, "armor") else 0
        return self.endurance + armor_bonus

    @property
    def m_defence(self):
        armor_bonus = self.armor.m_defence if hasattr(self, "armor") else 0
        return self.wisdom + armor_bonus

    def attack(self,other):
        damage  = damage_calculation(self.damage,other.defence)
        other.take_damage(damage)

    def take_damage(self,amount):
        if amount <=0:
            print(f"{self.name} takes no damage")
        else:
            self.hp -= amount
            print(f"{self.name} takes {amount} damage")

class Weapon:
    def __init__(self,name,damage,magic):
        self.name = name
        self.damage = damage
        self.magic = magic

    def __str__(self):
        return f"{self.name} damage:{self.damage} magic:{self.magic}"

class Armor:
    def __init__(self,name,defence,m_defence):
        self.name = name
        self.defence = defence
        self.m_defence = m_defence

    def __str__(self):
        return f"{self.name} defence:{self.defence} magic defence:{self.m_defence}"

class Adventurer(Creature):
    def __init__(self,name,weapon , armor,max_hp,hp,max_mp,mp,strength,endurance,intelligence,wisdom,level=1, skill = "none",skill2 = "none"):
        super().__init__(name,max_hp,hp,max_mp,mp,strength,endurance,intelligence,wisdom)
        self.level = level
        self.weapon =weapon
        self.armor = armor
        self.skill = skill
        self.skill2 = skill2

    def display_stats(self):
        print("=" * 30)
        print(f"{self.name} (Level {self.level})")
        print("=" * 30)

        print("\n[ HP / MP ]")
        print(f"HP : {self.hp:>3} / {self.max_hp:<3}")
        print(f"MP : {self.mp:>3} / {self.max_mp:<3}")

        print("\n[ Attributes ]")
        print(f"STR: {self.strength:<3}  END: {self.endurance:<3}")
        print(f"INT: {self.intelligence:<3}  WIS: {self.wisdom:<3}")

        print("\n[ Equipment ]")
        print(f"Weapon : {self.weapon.name}")
        print(f"Armor  : {self.armor.name}")

        print("\n[ Combat Stats ]")
        print(f"ATK : {self.damage:<3}   MAG : {self.magic:<3}")
        print(f"DEF : {self.defence:<3}   MDEF: {self.m_defence:<3}")

        print("\n[ Skills ]")
        print(f"- {self.skill}")
        if self.level >= 3:
            print(f"- {self.skill2}")

        print("=" * 30)

class Warrior(Adventurer):
    def __init__(self,name,weapon , armor, max_hp = 10, hp =10, max_mp =4, mp =4 , strength =6, endurance =5, intelligence=3, wisdom=2, level=1, skill = "second wind", skill2 = "double attack",skill_cost =3):
        super().__init__(name,weapon,armor,max_hp, hp, max_mp, mp, strength, endurance, intelligence, wisdom,level,skill,skill2)
        self.skill_cost = skill_cost

    def use_skill(self,other):
        if self.mp < self.skill_cost:
            print("Not enough mp")
        else:
            if self.hp + 5 >= self.max_hp:
                self.hp = self.max_hp
                self.mp -=self.skill_cost
                print(f"{self.name} used second wind. Current hp is {self.hp}")
            else:
                self.hp += 5
                self.mp -=self.skill_cost
                print(f"{self.name} used second wind. Current hp is {self.hp}")

    def use_skill2(self,other):
        if self.mp < self.skill_cost:
            print("Not enough mp")
        else:
            self.attack(other)
            self.attack(other)
            self.mp -= self.skill_cost

    def level_up(self):
        print(f"{self.name} leveled up.")
        self.level += 1
        a = randrange(100)
        if a > 75:
            self.max_hp += 2
            self.hp += 2
            print(f"{self.name} gained 2 hp.")
        else:
            self.max_hp += 1
            self.hp += 1
            print(f"{self.name} gained 1 hp.")
        a = randrange(100)
        if a > 55:
            self.max_mp += 1
            self.mp += 1
            print(f"{self.name} gained 1 mp.")
        a = randrange(100)
        if a > 75:
            self.strength += 2
            print(f"{self.name} gained 2 strength.")
        else:
            self.strength += 1
            print(f"{self.name} gained 1 strength.")
        a = randrange(100)
        if a > 25:
            self.endurance += 1
            print(f"{self.name} gained 1 endurance.")
        a = randrange(100)
        if a > 85:
            self.intelligence += 1
            print(f"{self.name} gained 1 intelligence.")
        a = randrange(100)
        if a > 85:
            self.wisdom += 1
            print(f"{self.name} gained 1 wisdom.")



class Wizard(Adventurer):
    def __init__(self,name,weapon, armor, max_hp = 7, hp =7, max_mp =9, mp =9 , strength =4, endurance =3, intelligence=6, wisdom=4, level=1, skill = "fireball",skill2 = "thunder",skill_cost =3):
        super().__init__(name,weapon,armor,max_hp, hp, max_mp, mp, strength, endurance, intelligence, wisdom,level,skill,skill2)
        self.skill_cost = skill_cost

    def use_skill(self,other):
        if self.mp < self.skill_cost:
            print("You can't fire, not enough mp")
        else:
            if self.magic +4 - other.m_defence <= 0:
                self.mp -= self.skill_cost
                print("This did nothing")
            else:
                other.hp -= self.magic + 4 - other.m_defence
                self.mp -= self.skill_cost
                print(f"{self.name} cast fireball: it did {self.magic + 4 - other.m_defence} damage")

    def use_skill2(self,other):
        if self.mp < self.skill_cost:
            print("You can't fire, not enough mp")
        else:
            if (self.magic - other.m_defence)*1.2 <= 0:
                self.mp -= self.skill_cost
                print("Your lightning bolt was ineffective")
            else:
                print(f"{self.name} casts a lightning bolt. It did {(self.magic - other.m_defence)*1.2} damage")
                other.hp -= (self.magic - other.m_defence)*1.2
                self.mp -= self.skill_cost

    def level_up(self):
        print(f"{self.name} leveled up.")
        self.level += 1
        a = randrange(100)
        if a > 75:
            self.max_hp += 1
            self.hp += 1
            print(f"{self.name} gained 1 hp.")
        a = randrange(100)
        if a > 75:
            self.max_mp += 2
            self.mp += 2
            print(f"{self.name} gained 2 mp.")
        else:
            self.max_mp += 1
            self.mp += 1
            print(f"{self.name} gained 1 mp.")
        a = randrange(100)
        if a > 75:
            self.strength += 1
            print(f"{self.name} gained 1 strength.")
        a = randrange(100)
        if a > 65:
            self.endurance += 1
            print(f"{self.name} gained 1 endurance.")
        a = randrange(100)
        if a > 75:
            self.intelligence += 2
            print(f"{self.name} gained 2 intelligence.")
        else:
            self.intelligence += 1
            print(f"{self.name} gained 1 intelligence.")
        a = randrange(100)
        if a > 35:
            self.wisdom += 1
            print(f"{self.name} gained 1 wisdom.")


def get_number(prompt,low,high):
    while True:
        value = input(prompt)
        try:
            if  low <= int(value)< high+1:
                return int(value)
            else:
                print("Invalid number")
        except ValueError:
            print("numbers only")



def player_choice(player):
    if player.level <3:
        choice = get_number("Choose action: attack(1) or skill(2): ",1,2)
        return choice
    else:
        choice = get_number("Choose action: attack(1) or first skill(2) or second skill(3)",1,3)
        return choice

def check_death(entity):
    if entity.hp <= 0:
        print(f"{entity.name} has died!")
        return True
    return False

def encounter(player,other):
    while True:
        print(f"HP: {player.hp}, MP: {player.m_defence}")
        action = player_choice(player)
        if action == 1:
            player.attack(other)
            if check_death(other):
                print(f"{player.name} has won. Level up!")
                player.level_up()
                player.display_stats()
                break
            other.attack_pattern(player)
            if check_death(player):
                break
        if action ==2:
            player.use_skill(other)
            if check_death(other):
                print(f"{player.name} has won. Level up!")
                player.level_up()
                player.display_stats()
                break
            other.attack_pattern(player)
            if check_death(player):
                break
        if action == 3:
            player.use_skill2(other)
            if check_death(other):
                print(f"{player.name} has won. Level up!")
                player.level_up()
                player.display_stats()
                break
            other.attack_pattern(player)
            if check_death(player):
                break

def damage_calculation(attack,defence):
    return max(0, attack-defence)