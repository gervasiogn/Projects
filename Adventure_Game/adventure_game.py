import random
import time


animals = random.choice(['lion', 'tiger', 'bear', 'cheetah'])
animal = random.choice(animals)
animal_possessive = animal + "'s"
weapons = []


def forest_first_time():
    if "stick" in weapons:
        forest_already_visited()
    else:
        print_pause("You peer cautiously into the forest.")
        print_pause("It turns out to be a dense forest with beautiful trees "
                    "and shrubbery.")
        print_pause("Your eye catches something on the ground underneath a "
                    "pile of leaves.")
        print_pause("You have found a large stick that broke apart from a "
                    "ginormous tree nearby.")
        weapons.append("stick")
        print_pause("You discard your silly old flashlight and take the stick "
                    "with you.")
        print_pause("You walk back out to the open area between the dense "
                    "forest and the shack.")
        options()


def options():
    decision = valid_input("Enter 1 to explore the forest.\n"
                           "Enter 2 to go to the shack.\n"
                           "What would you like to do?\n"
                           "(Please enter 1 or 2.) ", ['1', '2'])
    if decision == '1':
        explore()
        if 'stick' in weapons:
            forest_already_visited()
        else:
            forest_first_time()
    else:
        shack()


def play_game():
    print_pause("You find yourself standing in the wilderness.")
    print_pause(f'Rumor has it that a {animal} is somewhere around here, and '
                'is vicious!')
    print_pause("In front of you is a forest.")
    print_pause("To your right is a shack.")
    print_pause("In your hand you hold a flashlight that you found nearby.")
    options()


def print_pause(prompt):
    print(prompt)
    time.sleep(1)


def valid_input(prompt, options):
    while True:
        choice = input(prompt).lower()
        if choice in options:
            return choice
        print_pause(f'Sorry, the option "{option}" is invalid. Try again!')


def shack():
    print_pause("You go to the shack. Luckily, you don't seem to have "
                "been followed.")
    print_pause("In the shack, you find a map of the forest and "
                "strategically plan a route to explore.")
    print_pause("After some time, you decide to go back outside.")
    alternate_options()


def alternate_options():
    alternate_choice = valid_input("Would you like to search for resources? "
                                   "(y/n) ", ['y', 'n'])
    if alternate_choice[0] == 'y':
        forest_first_time()
        if 'stick' in weapons:
            forest_already_visited()
    else:
        explore()


def forest_already_visited():
    print_pause("You look around the forest.")
    print_pause("You've been here before, and have picked up what you can see "
                "on the outskirts of the forest.")
    print_pause("You walk back out to the open area.")
    options()


def win_fight():
    if 'stick' in weapons:
        print_pause(f'As the {animal} movs to attack, you unsheath your new '
                    'stick.')
        print_pause("The stick is held firmly in your hand as you "
                    "brace yourself for the attack.")
        print_pause(f'But the {animal} takes one look at the stick '
                    'and runs away.')
        print_pause(f'You have rid the town of the {animal}. You are '
                    'victorious!')
        play_again()
    else:
        defeated(animal)


def play_again():
    decision = valid_input("Would you like to play again? (y/n) ", ['y', 'n'])
    if decision[0] == 'y':
        print_pause("Excellent! Restarting the game...")
        global animal, animal_possessive, weapons
        animal = random.choice(animals)
        animal_possessive = animal + "'s"
        weapons = []
        play_game()
    else:
        print_pause("Thanks for playing! See you next time.")
        quit()


def defeated():
    print_pause('You do your best...\nbut your flashlight is no match for '
                f'the {animal}.')
    print_pause("You have been defeated!")


def explore():
    print_pause("You listen for sounds, watch for movement, and decide to go "
                "into the forest.")
    print_pause('All the sudden, you see a pair of eyes. As it walks toward '
                f'you, you notice it is a {animal}.')
    print_pause(f'Eep! This is the {animal_possessive} territory!')
    print_pause(f'The {animal} gets closer to you!')
    if 'stick' in weapons:
        fight_or_run()
    else:
        defeated()
        play_again()


def fight_or_run():
    second_choice = valid_input("Would you like to (1) fight or (2) run away? "
                               ,['1', '2'])
    if second_choice == '1':
        if 'stick' in weapons:
            win_fight()
        else:
            print_pause("You feel a bit under-prepared for this, what with "
                        "only having a flashlight.")
            defeated(animal)
    else:
        shack()


play_game()
