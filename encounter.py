import rpg2
from random import randrange


goblin = rpg2.Creature("goblin", 4, 4, 2, 2, 4, 3, 1, 1)
giant_rat = rpg2.Creature("giant rat", 3, 3, 2, 2, 5, 2, 1, 1)
wolf = rpg2.Creature("wolf", 5, 5, 2, 2, 6, 3, 1, 1)


encounter_1_pool = [goblin, giant_rat, wolf]

mimic = rpg2.Creature("mimic", 6, 6, 2, 2, 6, 4, 1, 4)
skeleton = rpg2.Creature("skeleton", 5, 5, 2, 2, 6, 6, 4, 1)
orc = rpg2.Creature("orc", 8, 8, 2, 2, 7, 5, 2, 1)


encounter_2_pool = [mimic, skeleton, orc]

troll = rpg2.Creature("troll", 10, 10, 2, 2, 9, 6, 1, 2)
wyvern = rpg2.Creature("wyvern", 12, 12, 2, 2, 8, 5, 1, 4)

third_encounter = [troll, wyvern]

boss = rpg2.Dragon_lord("Dragon lord")

def play():
    name = input("First step of the journey. Choose your name: ")
    choice = rpg2.get_number("Select class: 1 for warrior, 2 for wizard: ", 1, 2)
    if choice == 1:
        player = rpg2.Warrior(name)
    else:
        player = rpg2.Wizard(name)
    player.display_stats()
    print(f"{player.name} begins his journey to save the world")

    while True:
        opponent = encounter_1_pool[randrange(len(encounter_1_pool))]
        print(f"Your 1st encounter is with a {opponent.name} ")
        if player.hp <= 0:
            break
        rpg2.encounter(player,opponent)
        second = encounter_2_pool[randrange(len(encounter_2_pool))]
        print(f"Your 2nd encounter is with a {second.name} ")
        rpg2.encounter(player,second)
        if player.hp <= 0:
            break
        third = third_encounter[randrange(len(third_encounter))]
        print(f"Your next encounter is with a {third.name} ")
        rpg2.encounter(player, third)
        if player.hp <= 0:
            break
        print(f"You won your encounter with {third.name}!")
        print(f"{player.name} rests before the final encounter")
        player.hp = player.max_hp
        player.mp = player.max_mp
        print("You reach the Dragon lord")
        print("He offers you a choice side with him and rule half the world or die")
        final_choice = rpg2.get_number("Side with me  or die (1 for yes , 2 for no): ", 1, 2)
        if final_choice == 1:
            print("You succumbed to evil, the world is now doomed...")
            break
        else:
            print("\nYou defy him and the final battle begins!\n")
        rpg2.final_encounter(player,boss)
        if player.hp <= 0:
            print("All is lost...")
            break
        if boss.hp <= 0:
            print("Congratulations! You saved the world! \n end of the game")
            break


play()