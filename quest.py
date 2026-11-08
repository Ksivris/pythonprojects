from random import randrange

import aggregation
import enemies


goblin = enemies.Goblin("goblin",10,10,1,1,6,5,1,1)
wolf = enemies.Wolf("wolf",9,9,1,1,7,5,2,1)
giant_rat = enemies.Giant_rat("giant_rat",7,7,1,1,5,4,1,1)
banshee = enemies.Banshee("banshee",12,12,9,9,5,4,8,4)
skeleton = enemies.Skeleton("skeleton",13,13,1,1,8,5,1,4)
orc = enemies.Orc("orc",15,15,10,10,7,5,1,3)
lich = enemies.Lich("lich",18,18,16,16,5,5,8,6)
troll = enemies.Troll("troll",22,22,10,10,11,7,1,4)
wyvern = enemies.Wyvern("wyvern",19,19,10,10,10,6,1,6)
dragon = enemies.Dragon("dragon",30,30,10,10,14,10,12,8)

first_encounter_pool = [goblin,wolf,giant_rat]
second_encounter_pool = [banshee,skeleton,orc]
third_encounter_pool = [lich,troll,wyvern]

short_sword = aggregation.Weapon("short sword",3,1)
chainmail = aggregation.Armor("chainmail",3,1)
staff = aggregation.Weapon("staff",2,3)
robe = aggregation.Armor("robe",2,3)

long_sword = aggregation.Weapon("long sword",4,1)
gambeson = aggregation.Armor("gambeson",4,1)
staff2 = aggregation.Weapon("staff vol2",2,4)
robe2 = aggregation.Armor("robe vol2",2,4)

claymore = aggregation.Weapon("claymore",5,2)
plate_mail = aggregation.Armor("plate mail",5,2)
long_staff = aggregation.Weapon("long staff",3,5)
wizard_robe = aggregation.Armor("wizard robe",3,5)

final_sword =aggregation.Weapon("final sword",7,3)
final_armor = aggregation.Armor("final armor",6,4)
final_staff = aggregation.Weapon("final staff",4,7)
final_robe = aggregation.Armor("final robe",3,7)

first_reward =[long_sword,gambeson,staff2,robe2]
second_reward =[claymore,plate_mail,long_staff,wizard_robe]
final_reward = [final_sword,final_armor,final_staff,final_robe]

def loot(instance,player):
    loot_table = []
    for i in range(2):
        loot_table.append(instance.pop(randrange(len(instance))))
    print("You found loot, you can only get one piece")
    for i in range(2):
        print(f"{i+1}: {(loot_table[i])}")
    choice = (aggregation.get_number("Make a choice 1 or 2, 3 if you want nothing: ",1,3))-1
    if choice ==2:
        print("You want nothing")
    else:
        if isinstance(loot_table[choice], aggregation.Weapon):
            player.weapon = loot_table[choice]
        else:
            player.armor = loot_table[choice]

def player_dead(player):
    if player.hp <= 0:
        return True
    else:
        return False


def play():
    print("First step of the journey. Choose your name and class")
    name = input("Give your name: ")
    choice = aggregation.get_number("1-Warrior , 2- Wizard: ",1,2)
    if choice == 1:
        player = aggregation.Warrior(name,short_sword,chainmail)
    elif choice == 2:
        player = aggregation.Wizard(name,staff,robe)
    player.display_stats()
    print("The journey begins")

    while True:
        first_opponent = first_encounter_pool[randrange(len(first_encounter_pool))]
        print(f"Your 1st encounter is with {first_opponent.name} ")
        aggregation.encounter(player,first_opponent)
        if player_dead(player):
            break
        loot(first_reward,player)
        second_opponent = second_encounter_pool[randrange(len(second_encounter_pool))]
        print(f"Your 2nd encounter is with {second_opponent.name}")
        aggregation.encounter(player,second_opponent)
        if player_dead(player):
            break
        loot(second_reward,player)
        third_opponent = third_encounter_pool[randrange(len(third_encounter_pool))]
        print(f"Third encounter is with {third_opponent.name}")
        aggregation.encounter(player,third_opponent)
        if player_dead(player):
            break
        loot(final_reward,player)
        print("You finally reach the dragons lair.You rest outside before continuing")
        player.hp = player.max_hp
        player.mp = player.max_mp
        print("You attack the dragon!")
        aggregation.encounter(player,dragon)
        if player_dead(player):
            print("game over")
            break
        print("You vanquished the dragon!")
        print("Fin")
        break
play()
