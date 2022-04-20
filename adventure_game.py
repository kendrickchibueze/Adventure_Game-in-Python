import time
import random
from colorama import Fore

magical_weapon = []


def random_enemy():
    Game_enemies = ["dragon", "gorgon", "pirate", "troll", "wicked fairie"]
    global enemy
    enemy = random.choice(Game_enemies)


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def intro():
    random_enemy()
    print_pause(Fore.CYAN + "You find yourself standing in an open" +
                "field, filled with grass and yellow wild flowers ")
    print_pause(f"Rumor has it that a {enemy} is somewhere around here," +
                "and has been terrifying the nearby village")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand, you hold a "
                + "trusty (but not an effective one) dagger.")


def knock_door():
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door " +
                f"opens and out steps a {enemy} ")
    print_pause(f"Eep!, this is the {enemy} house!")
    print_pause(f"The {enemy} attacks you!")


def house():
    if "sword" not in magical_weapon:
        knock_door()
        print_pause("You feel a little under-prepared for this, "
                    "what with only having a tiny dagger ")
    else:
        knock_door()


def cave():
    print_pause("You peer cautiously into the cave.")
    print_pause("It turns out to be only a small cave.")
    print_pause("Your eye catches a glint of metal behind a rock")
    print_pause("You have found the magical sword of Ogoroth!")
    print_pause("You discard your silly old dagger" +
                " and take the sword with you.")
    print_pause("You walk back out to the field.")
    magical_weapon.append("sword")


def empty_cave():
    if "sword" not in magical_weapon:
        cave()
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("You have been here before," +
                    "and gotten all the good stuff." +
                    "Its just an empty cave now")
        print_pause("You walk back into the field")


def win_game():
    print_pause(f"As the {enemy} moves to attack," +
                "you unsheath you new sword.")
    print_pause("The Sword of Ogoroth shines brightly in your hand" +
                "as you brace yourself for the attack")
    print_pause(f"But the {enemy} takes one look" +
                " at your shiny new toy and runs away")
    print_pause("You have rid the town of the " +
                f"{enemy}.You are victorious!")


def loose_game():
    print_pause("You do your best...")
    print_pause(f"but your dagger is no match for the {enemy}.")
    print_pause("You have been defeated!")


def escape_to_field():
    print_pause("You run back into the field." +
                "Luckily, you don't seem to have been followed ")


def fight():
    action = valid_input("\nWould you like to (1) fight or" +
                         "(2) run away?", ['1', '2'])
    if action == '1':
        if "sword" in magical_weapon:
            win_game()
            play_again()
        else:
            loose_game()
            play_again()
    elif action == '2':
        escape_to_field()
        adventure()
    else:
        fight()


def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print_pause(f'Sorry, the option "{option}" is invalid. Try again!')


def play_again():
    action_next = valid_input("\nWould you like to play again?" +
                              "(y/n) ", ['y', 'n']).lower()
    if action_next == 'y':
        print_pause("Excellent!, Restarting the game...")
        intro()
        adventure()
    elif action_next == 'n':
        print_pause("Thanks for playing, see you next time")
        exit()
    else:
        play_again()


def adventure():
    activity = valid_input("\nEnter 1 to knock at the door of the house.\n"
                           "Enter 2 to peer into the cave.\n"
                           "what would you want to do?\n"
                           "(please enter 1 or 2)\n", ['1', '2'])
    if activity == '1':
        house()
        fight()
    elif activity == '2':
        empty_cave()
        adventure()

    else:
        adventure()
    return activity


def play_game():
    intro()
    adventure()


play_game()
